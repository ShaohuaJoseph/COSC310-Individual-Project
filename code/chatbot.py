#import urllib
from stanfordcorenlp import StanfordCoreNLP
import nltk
nltk.download("wordnet")
nltk.download("punkt")
from nltk.tag import pos_tag
import re, string
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from keras.models import load_model
model = load_model('model.h5')
import json
import random
import time
import wikipedia
from flickrapi import FlickrAPI
import os, io, requests
import re





#Load the intents
nlp = StanfordCoreNLP(r'/Users/jiangshaohua/Desktop/UBC/2020 Winter Term 2/COSC 310/Group Project/Chat-bot-team-20/code/stanford-corenlp-4.2.0')
intents = json.loads(open('intents.json').read())
sentiment = pickle.load(open("SentimentalAnalysis.pkl", "rb"))

#Load the words and classes files using pickle
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

saveData = ""
try:
    saveData = pickle.load(open("saveData.pkl", "rb"))
except IOError:
    saveData = [['',{}]]




def lemma(s):
    # Make an array by tokenizing the sentence
    array = nltk.word_tokenize(s)
    newArray = []
    # Lemmatize the words in the array
    for word in array:
        newArray.append(l.lemmatize(word.lower()))
    return newArray

# Return array of 0 or 1 which represents if a word exists or not

def word_bag(s, words):
    # Lemmatize the input sentence
    array = lemma(s)
    # empty array of 0
    bag = [0]*len(words)  
    for s in array:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word exists
                bag[i] = 1
                break
                
    return(np.array(bag))

def predict(s, model):
    # filter out predictions below a threshold
    test = nlp.pos_tag(s)
    testsen = ''
    for t in test:
        if t[1] == 'NNP' and t[0].lower() not in words:
            testsen = testsen + t[0] + " "
    
    if (testsen != ''):
        testnp = word_bag(testsen, words)
        testRes = model.predict(np.array([testnp]))[0]
        thresh = 0.25
        testresults = []
        for i,r in enumerate(testRes):
            if r>thresh:
                testresults.append([i,r])
                # sort in descending order of probabilities
        testresults.sort(key=lambda x: x[1], reverse=True)
        
        for r in testresults:
            if classes[r[0]] == "noanswer":
                return [{"intent": "noanswer", "probability": str(r[1])},word_tokenize(testsen)]
            else:
                break
        
    p = word_bag(s, words)
    res = model.predict(np.array([p]))[0]
    thresh = 0.25
    results = []
    #generate an array of probabilities
    for i,r in enumerate(res):
        if r>thresh:
           results.append([i,r])
    # sort in descending order of probabilities
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    return_list.append({"intent": classes[results[0][0]], "probability": str(results[0][1])})
    return_list.append('')
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_intents = intents_json['intents']

    # Added (tag at last)
    result = ['','','',tag]
    for i in list_intents:
        if(i['tag']== tag):
            result[0] = random.choice(i['responses'])
            if tag == 'goodbye':
                result[1] = 'save'
            elif tag == 'noanswer':
                result[1] = 'noanswer'
                if ints[1] != '':
                    result[2] = (ints[1])
            break
    return result

def gen_output(msg):
    ints = predict(msg, model)
    response = getResponse(ints, intents)
    return response


#Creating UI with tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image




# ------------------------------------------------------------------------------------------------------------
# The 'Key' and 'Secret' necessary for Flickr API
KEY = 'f0c52b029923ae1bac23554d7a58c8df'
SECRET = '7e79bc32ba395f64'

# Set the acceptable size for images
SIZES = ["url_q", "url_t", "url_s", "url_n"]  # in order of preference


# Search for a set of corresponding photoes with tags
def get_photos(image_tag):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    photos = flickr.walk(text=image_tag,  # it will search by image title and image tags
                            extras=extras,  # get the urls for each size we want
                            privacy_filter=1,  # search only for public photos
                            per_page=50,
                            sort='relevance')  # we want what we are looking for to appear first
    return photos

# Get the URL of a photo following the list of acceptable sizes.
def get_url(photo):
    for i in range(len(SIZES)):  # makes sure the loop is done in the order we want
        url = photo.get(SIZES[i])
        if url:  # if url is None try with the next size
            return url

# Get all the images with the acceptable size 'by tags'.
def get_urls(image_tag, max):
    photos = get_photos(image_tag)
    counter=0
    urls=[]

    for photo in photos:
        if counter < max:
            url = get_url(photo)  # get preffered size url
            if url:
                urls.append(url)
                counter += 1
            # if no url for the desired sizes then try with the next photo
        else:
            break

    return urls

# ------------------------------------------------------------------------------------------------------------






def recent():
    textbox.delete("0.0",END)
    for i in range(len(saveData)-1):
        output = str(i + 1) + ")\n"
        output = output + "Number turns: " + str(saveData[i][0]) + "\n\n"
        for key in saveData[i][1]:
            output = output + "User: " + "'" + key + "'" + "\n" + "Bot: " + saveData[i][1][key] + "\n\n"
        output = output + "-----------------------------------------------" + "\n"
        textbox.insert(END,output)

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def send():
    	    #Read the message from user and clear the message window
            msg = EntryBox.get("1.0",'end-1c').strip()
            EntryBox.delete("0.0",END)
            
            custom_token = remove_noise(word_tokenize(msg))
            for t in custom_token:
                    t = word_tokenize(t)
                    emotion = sentiment.classify(dict([token, True] for token in t))
                    if emotion == "Negative":
                        if nlp.pos_tag(t[0])[0][1] == "NN" or nlp.pos_tag(t[0])[0][1] == "VB":
                            if t[0].lower() in words:
                                emotion = "Positive"
                            else:
                                break
                        else:
                            emotion = "Positive"
                            break
            
            if msg != '':
                ChatLog.config(state=NORMAL)
        
                ChatLog.image_create(END, image = userimg)
                ChatLog.insert(END, " : " + msg + '\n\n')
                ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
                ChatLog.tag_configure("center", justify='center')
        
                res = gen_output(msg)
                ChatLog.image_create(END, image = botimg)
                if emotion == "Negative" and res[1] == "noanswer" and res[2] == '':
                    ChatLog.insert(END, " : I am sorry to hear that " )
                    ChatLog.image_create(END, image = sad)
                    ChatLog.insert(END, "\n\n")
                elif emotion == "Positive" and res[1] == "noanswer":
                    ChatLog.insert(END, " : " )
                    ChatLog.image_create(END, image = confused)
                    if res[2] != "":
                        for r in res[2]:
                            search = r + " "
                        res[0] = res[0].replace("%",search)
                        ChatLog.insert(END," " + res[0] + "\n")
                        ChatLog.insert(END,"This is what I found on Wikipedia about " + search + ":\n")
                        try:
                            ChatLog.insert(END, wikipedia.summary(search, sentences =3) + "\n\n")






                        except wikipedia.exceptions.DisambiguationError as e:
                            ChatLog.insert(END, wikipedia.summary(e.options[0], sentences =3) + "\n\n")




                        # Display an image about this topic
                        # Get URL
                        imgURL = get_urls(search, 5)[0]

                        # # Get and Download img
                        # #path = os.path.dirname(__file__) + "/image"
                        # urllib.request.urlretrieve(imgURL, "image/" + search + ".png")
                        # search_img = Image.open("image/" + search + ".png")
                        # #response = requests.get(imgURL)
                        # #search_img = Image.open(requests.get(imgURL, stream=True).raw)
                        # search_img = search_img.resize((150, 150), Image. ANTIALIAS)

                        # Get and Download img
                        #path = os.path.dirname(__file__) + "/image"
                        # urllib.request.urlretrieve(imgURL, "image/" + search + ".png")
                        # search_img = Image.open("image/" + search + ".png")





                        #response = requests.get(imgURL)
                        # search_img = Image.open(requests.get(imgURL, stream=True).raw)
                        # search_img = search_img.resize((150, 150), Image. ANTIALIAS)


                        # # convert to an image Tkinter can use
                        # tk_img = ImageTk.PhotoImage(search_img)




                        # Added
                        app.change_image(imgURL)

                        
                        
                        # # Display img
                        # ChatLog.image_create(END, image = tk_img)





                        # ChatLog.insert(END, "\n\n")
                        # #ChatLog.image_create(END, image = happy)


                        # # Try
                        # root = Tk()     
                        # canvas = Canvas(root, width = 200, height = 200)   
                        # #canvas.pack() 
                        # #ChatLog.window_create(END, window=Canvas(root, width = 200, height = 200))
                        # canvas.create_image(20,20, anchor=NW, image=tk_img)  
                        # ChatLog.insert(END, "\n\n")
                        # #root.destroy()

                        # #text = tk.Text(canvas, width=120, height=40)








                    else:
                        res[0] = res[0].replace("%",msg)
                        ChatLog.insert(END," " + res[0] + "\n\n")

                elif emotion == "Positive":
                    ChatLog.insert(END," : ")
                    ChatLog.image_create(END, image = happy)
                    ChatLog.insert(END," " + res[0] + "\n\n")

                    # Added
                    general_topic = ["Video Games", "About Jump Festa", "Anime Convention", "Otaku Culture", "About Manhwa", "Describe Konosuba"]
                    if re.search('Japanese', res[3] or res[3] in general_topic):
                        ChatLog.insert(END,"I also found a simple explanation from wikipedia about " + res[3] + ":\n")
                        ChatLog.insert(END, wikipedia.summary(res[3], sentences = 1) + "\n\n")

                elif emotion == "Negative" and res[1] != "noanswer":
                    ChatLog.insert(END, " : I am sorry to hear that " )
                    ChatLog.image_create(END, image = sad)
                    ChatLog.insert(END, "\n\n" + res[0] + "\n\n")
                elif emotion == "Negative" and res[1] == "noanswer" and res[2] != '':
                    ChatLog.insert(END, " : " )
                    ChatLog.image_create(END, image = confused)
                    res[0] = res[0].replace("%",res[2][0])
                    ChatLog.insert(END," " + res[0] + "\n")
                    ChatLog.insert(END,"This is what I found on Wikipedia about " + res[2][0] + ":\n")
                    ChatLog.insert(END, wikipedia.summary(res[2][0], sentences =3) + "\n\n")


                    # Display an image about this topic
                    # Get URL
                    imgURL = get_urls(res[2][0], 5)[0]

                    # # Get and Download img
                    # #path = os.path.dirname(__file__) + "/image"
                    # urllib.request.urlretrieve(imgURL, "image/" + res[2][0] + ".png")
                    # search_img = Image.open("image/" + res[2][0] + ".png")
                    # #response = requests.get(imgURL)
                    # #search_img = Image.open(requests.get(imgURL, stream=True).raw)
                    # search_img = search_img.resize((150, 150), Image. ANTIALIAS)


                    # Get images
                    #path = os.path.dirname(__file__) + "/image"
                    # urllib.request.urlretrieve(imgURL, "image/" + res[2][0] + ".png")
                    # search_img = Image.open("image/" + res[2][0] + ".png")




                    # #response = requests.get(imgURL)
                    # search_img = Image.open(requests.get(imgURL, stream=True).raw)
                    # search_img = search_img.resize((150, 150), Image. ANTIALIAS)

                    


                    # # convert to an image Tkinter can use
                    # tk_img = ImageTk.PhotoImage(search_img)



                    # Added
                    app.change_image(imgURL)




                    # # Display img
                    # ChatLog.image_create(END, image = tk_img)
                    # #ChatLog.image_create(END, image = happy)



                    # ChatLog.insert(END, "\n\n")


                    # # Try
                    # root = Tk()     
                    # canvas = Canvas(root, width = 0, height = 0)   
                    # #canvas.pack() 
                    # canvas.create_image(20,20, anchor=NW, image=tk_img)  
                    # ChatLog.insert(END, "\n\n")
                    # root.destroy()







                    





                
                
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                if saveData[-1][0] == "":
                    saveData[-1][0] = 0
                    saveData[-1][1][msg] = res[0]
                else:
                    saveData[-1][0] = saveData[-1][0] + 1
                    saveData[-1][1][msg] = res[0]
                if res[1] == 'save':
                    saveData[-1][0] = saveData[-1][0] + 1
                    saveData.append(['',{}])
                    pickle.dump(saveData,open('saveData.pkl','wb'))
                    print("SAVED")




LARGE_FONT= ("Verdana", 12)


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        image1 = Image. open("botpic.jpg")
        image1 = image1.resize((25, 25), Image. ANTIALIAS)
        image2 = Image. open("user-24.gif")
        image2 = image2.resize((25, 25), Image. ANTIALIAS)
        image3 = Image.open("sinchronize-32.gif")
        image3 = image3.resize((20, 20), Image. ANTIALIAS)
        image4 = Image.open("sad.png")
        image4 = image4.resize((20, 20), Image. ANTIALIAS)
        image5 = Image.open("confused.png")
        image5 = image5.resize((20, 20), Image. ANTIALIAS)
        image6 = Image.open("happy.png")
        image6 = image6.resize((40, 40), Image. ANTIALIAS)
        global happy
        happy = ImageTk.PhotoImage(image6)
        global confused
        confused = ImageTk.PhotoImage(image5)
        global sad
        sad = ImageTk.PhotoImage(image4)
        global refresh
        refresh = ImageTk.PhotoImage(image3)
        global botimg
        botimg = ImageTk.PhotoImage(image1)
        global userimg
        userimg = ImageTk.PhotoImage(image2)

        # Added
        global tk_img 
        tk_img = ImageTk.PhotoImage(image2)

        # Added
        global img_list
        img_list = []

        #Changing window image
        self.tk.call('wm', 'iconphoto', self._w,botimg )
        self.title("Anime Bot")
        self.geometry("400x500")
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Recent):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    # Added
    def change_image(self, imgURL):
        search_img = Image.open(requests.get(imgURL, stream=True).raw)
        search_img = search_img.resize((150, 150), Image. ANTIALIAS)


        # convert to an image Tkinter can use
        global tk_img
        tk_img = ImageTk.PhotoImage(search_img)

        ChatLog.image_create(END, image = tk_img)
        ChatLog.insert(END, "\n\n")


        
    
   
class Home(tk.Frame):
        

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global ChatLog
        ChatLog = Text(self, bd=2,relief = "ridge", bg="beige", height="100", width="50", font="Arial", wrap = WORD)
        ChatLog.config(state=NORMAL)
        
        SendButton = Button(self, font=("Verdana",12,'bold','italic'), text="Send", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= send )
        RecentButton = Button(self, font=("Verdana",12,'bold','italic'), text="Recent", width="12", height=5,
                    bd=0, bg="#030bfc", activebackground="#7373ff",fg='#ffffff',
                    command= lambda: controller.show_frame(Recent))
        global EntryBox
        EntryBox = Text(self, bd=2,relief = "ridge", bg="#e6e6e6",width="29", height="5", font="Arial",wrap = WORD)

        #Aranging the objects
        ChatLog.place(x=6,y=6, height=386, width=388)
        EntryBox.place(x=6, y=401, height=90, width=265)
        SendButton.place(x=290, y=401, height=45, width = 104)
        RecentButton.place(x=290, y=450, height=45, width = 104)
       


class Recent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Recent Conversation", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Back", command=lambda: controller.show_frame(Home),bg="#030bfc", activebackground="#7373ff", fg='#ffffff')
        re = tk.Button(self, image = refresh, command = recent)
        sb = Scrollbar(self)  
        global textbox
        textbox = Text(self, bd =2, relief = "ridge", bg="beige", height="100", width="40",yscrollcommand = sb.set, wrap = WORD)
        for i in range(len(saveData)-1):
            output = str(i + 1) + ")\n"
            output = output + "Number turns: " + str(saveData[i][0]) + "\n\n"
            for key in saveData[i][1]:
                output = output + "User: " + "'" + key + "'" + "\n" + "Bot: " + saveData[i][1][key] + "\n\n"
            output = output + "---------------------------------------------" + "\n"
            textbox.insert(END,output)
        
        sb.pack(side = RIGHT, fill = Y)
        sb.config(command = textbox.yview)
        re.place(x=360,y=9)
        textbox.place(x=6,y=40, height=450, width=370)
        button1.place(x=6,y=9)


app = GUI()
app.mainloop()

if saveData[-1][0] != '':
    saveData[-1][0] = saveData[-1][0] + 1
    saveData.append(['',{}])
    pickle.dump(saveData,open('saveData.pkl','wb'))
    print("SAVED")

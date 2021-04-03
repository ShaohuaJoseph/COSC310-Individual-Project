# from stanfordcorenlp import StanfordCoreNLP
# import nltk
# nltk.download("wordnet")
# nltk.download("punkt")
# from nltk.tag import pos_tag
# import re, string
# from nltk.stem import WordNetLemmatizer
# l = WordNetLemmatizer()
# import pickle
# import numpy as np
# from nltk.tokenize import word_tokenize
# from keras.models import load_model
# model = load_model('model.h5')
# import json
# import random
# import time
# import wikipedia


from tkinter import *
from typing import IO
from PIL import ImageTk, Image
import os
from flickrapi import FlickrAPI
import os
import urllib
import requests
import io
import numpy as np
import urllib
import cv2
import imghdr

#from progress.bar import Bar
import requests
import os
import sys
import time
#from downloader import download_images
import os

import urllib.request


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


def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)



def download_images(urls, path):
    create_folder(path)  # makes sure path exists

    for url in urls:
        image_name = url.split("/")[-1]
        image_path = os.path.join(path, image_name)

        if not os.path.isfile(image_path):  # ignore if already downloaded
            response=requests.get(url,stream=True).raw

            with open(image_path,'wb') as outfile:
                outfile.write(response.content)






root = Tk()
ChatLog = Text(root, bd=2,relief = "ridge", bg="beige",
    height="100", width="50", font="Arial", wrap = WORD)
ChatLog.config(state=NORMAL)
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack() 

# Display an image about this topic

search = 'Canada Flag'

# Get URL
imgURL = get_urls(search, 5)[0]

print(imgURL)

print(os.path.dirname(__file__))

#path = os.path.dirname(__file__) + "/image"
path = os.path.dirname(__file__)

print(path)

# Downloading images 
urllib.request.urlretrieve(imgURL, path + "/" + search + ".png")


# Get img
#search_img = ImageTk.PhotoImage(Image.open(imgURL))
# response = requests.get(imgURL)
# img = Image.open(io.BytesIO(response.content))
#img = Image.open(requests.get(imgURL, stream=True).raw)



#img = Image.open(path + "/" + search + ".png")
img = Image.open(os.path.join(path, "happy.png"))
img = img.resize((150, 150), Image.ANTIALIAS)
img.show()
# convert to an image Tkinter can use
search_img = ImageTk.PhotoImage(img)



#img.show()
#canvas.create_image(20,20, anchor=NW, image=search_img)  
ChatLog.image_create(END, image=search_img)    
mainloop()   

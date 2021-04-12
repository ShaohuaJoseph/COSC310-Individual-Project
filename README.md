# Chat-bot-team-20-ShaohuaJiang-IndividualProject
<br>

Name: Shaohua Jiang
=======

Github URL: <br><https://github.com/ShaohuaJoseph/COSC310-Individual-Project>
=======

**Link for the latest live demo (Individual Project)**:
<https://www.youtube.com/watch?v=sSWeNmJlRCk>
<br><br>
Link for the first live demo:
<https://drive.google.com/file/d/1r-Z9tOQUw9xpVBAXJCbN5R_DBIHX0QFv/view>
<br><br>
Link for the second live demo:
<https://drive.google.com/file/d/19O4-AgcyX_AJekY5BoluZdNu83gTw2fO/view>
=======

## Describe your topic/interest (context of the chatbot, who will use it, etc. )

In this project, we developed an interactive conversational agent that responds to user input. In response to the user, the agent generates sentences as output. There are 2 types of target users. The first type of target users includes anime and manga lovers who would love to talk about them and know more about it. The second type of target users includes anyone who are interested in Japanese culture. There are 2 types of topics as well. The first type of topic of the conversation is about the general information and personal preference of anime. The second type of topic of the conversation is about the general information of Japan such as people, religion, food, samurai and so on.

<br>

## How the code works

### **How to run it:**

To compile the code, we run in terminal these 2 lines of codes - “python train.py” and “python chatbot.py”. The first code is to train the model so that the GUI might function properlyl. The second code is to run the app. 
### **Stages of development:**

There are five stages of the development for the code: data importing and loading, data preprocessing, data training and testing, model building, and GUI developing.

### **How the classes are organized:**

There are 15 classes used in the code: nltk, json, pickle, numpy, keras, tkinter, Stanford Corenlp, Sentimental Analyser, GUI, Home, Recent, Wikipedia, WikipediaAPI, FlickrAPI, and requests.

- Class “nltk” contains a group of libraries which provide statistical processing for English Language and is commonly used for Natural Language Processing. It is used throughout all the developing stages except the model building stage and the GUI development stage. 

- There are 4 critical methods within this class: “nltk.stem.wordnetlemmatizer”, “nltk.word_tokenize”, “nltk.pos_tag” (instead of Stanfordnlp’s POS tagging to simplify the implementation) and “nltk.corpus” 

        1. The first method, “nltk.stem.wordnetlemmatizer”, converts a word into its lemma form, groups different words to be analyzed as a single item based on similar meaning, and then creates a pickle file to store the Python objects which we will use while predicting. 

        2. The second method, “nltk.word_tokenize”, is used to cleanup and break the whole text into small parts, such as words.

        3. The third method, “nltk.pos_tag”, tags every word as “Proper Nouns”, “Verb”, “Adjectives” etc. It is used for one of the new features we added - POS tagging - and it works in the similar pattern as Stanford Corenlp’s POS tagging. We will explain Stanford Corenlp later.

        4. The fourth method, “nltk.corpus”, is used to access “wordnet” which helps us to implement a new feature that we added to this code - synonym recognition. 

- Class “json” is the data file which predicts the user inputs and gives responses. It is used for importing and loading data, preprocessing data, and getting random responses for the GUI. Json is also used implicitly throughout the program as the fundamental data in chatbot - conversation patterns.

- Class “pickle” is to make the data operations more efficient by removing object hierarchy when dumping our data or when loading our data from the dataset as it converts/treats the data as a single stream. Pickle is used throughout the stages except the data importing stage and the GUI development stage. It was also used to save a model for one of the new features that we added to this code - sentiment analysis. 

- Class “numpy” is to increase the efficiency of the operation of lists in python. It is used in 2 stages - “creating data for training and testing” and “predicting classes for GUI”.

- Class “keras'' is to build and import the deep neural network model for the trained data. It is used in the stages of building and importing the model to GUI. 

- Class “tkinter” is used to develop a graphical user interface by powerful libraries and functions within the class. It is used to develop the final GUI.

- Class “Stanford Corenlp” is a service for natural language processing. Instead of creating a wrapper ourselves, we used a wrapper for this class called stanfordcorenlp. The link is put under the reference list at the end of the README file.

- “Sentimental Analyser” is a different python file created to help us with Sentiment Analysis. We create a naïve bayes model to decide between “Negative” and “Positive” Sentences. This model is used to analyze how users react to it.

- “GUI” is a class that is used to initialize everything related to our Graphical User Interface such as images, pages, etc.

- Class “Home” is the class for our home page in the Graphical User Interface and it contains all features present on that page.

- Class “Recent”, is used to record and store recent conversation dialogue in our recent conversation page in the Graphical User Interface. It contains all features present on that page.

- Class “Wikipedia” is used to initiate online searches on Wikipedia in real time. It is an additional feature for our chatbot that functions when the chatbot receives general questions or doesn’t recognize a “Proper Noun” that is found by one of the new features we added - POS tagging.

- Class "WikipediaAPI" is used as an advanced version of the original "Wikipedia" Class. It offers a few methods that have functionalities that are not provided in the "Wikipedia" class. With the help of the new functionalities, I added more features to our chatbot. More details are explained in the feature list below.

- Class "FlickrAPI" is used in our "charbot.py" file to search images from Flickr.com and add them to the conversations when users ask general questions or questions that our chatbot cannot understand. With the help of these images, users might have a better understanding of what they want to know **visually**

- Class "requests" is used in our "chatbot.py" file to get online images based on their URLs. With the help of this package, we can convert the image URLs obtained from the Flickr API into displayable images so that they can be displayed as outputs in the GUI.

<br>

## Data Flow Diagrams (DFD)

- Level 0: 

    - Image: ![Level-0 DFD](https://media.discordapp.net/attachments/798946362313408572/825163035822915614/Level_0.png)

    - Explain: This is our level 0 DFD, as you can see we have two entities namely, the user that is using the chatbot and the developers, which would be our entire team. The way the developers interact with the chatbot is by implementing new features fixing any bugs etc.


- Level 1: 

    - Image: ![Level-1 DFD](https://media.discordapp.net/attachments/798946362313408572/824776257337032764/DFD_Level_1.jpeg?width=942&height=718)

    - Explain: This right here is our level 1 DFD. Like the level 0 DFD we still have our developer and user as our entities. We have our synonym recognition, POS tagging and sentiment analysis as our processes. Our synonym recognition process works on the intents that is already in the dataset. Whereas the POS and sentimental works when only when the user has typed something on the UI and the bot prepares its response by picking required response from the dataset which is symbolized by the datastore at the bottom. We have another datastore that stores the conversation log named “conversation log”, the option to store this conversation comes from the UI.

<br>

## A List of 5 features that can be shared to others as API

- POS Tagging: includes the ability to searching on wikipedia and give responses based on that.

- Python file "SentimentalAnalyzer": a file that implements sentiment analysis

- Our chat bot: an application for others to view and modify.

- The method "remove_noise": removes all unnecessary words from a sentence

- Our Graphical User Interface

<br>

## New Features and APIs Added 

- **For Assignment 3** 

    - Synonym recognition

        - Function: It identifies synonyms within sentences and give corresponding answers. It allows users to make inputs more diversified and give correct answers at the same time

        - Snippet: ![Synonym Recognition](https://media.discordapp.net/attachments/798946362313408572/825077522916048986/Screen_Shot_2021-03-26_at_11.42.51_AM.png)

    - Sentiment analysis

        - Function: It recognizes user input that contains positive, negative, or neutral emotions and give corresponding answers without us having to code. It makes dialogue turns more lively and realistic.

        - Snippet: ![Sentiment Analysis](https://media.discordapp.net/attachments/798946362313408572/823878297989546004/unknown.png)

    - POS tagging

        - Function: It gets the information about Proper Nouns that our bot doesn't know and searching them real time on wikipedia. With this feature, our chatbot is able to answer topics that are outside of our designed topic and the users might get more satisfaction throughout conversations.

        - Snippet: ![POS Tagging](https://media.discordapp.net/attachments/829133684774928408/830252251247411240/POS_New.png?width=544&height=719)

    - Recent Conversation Page

        - Function: It saves dialogue information everytime our users say "bye" or close the app. With this feature, our users are able to check the dialogue history which is convenient.

        - Snippet: ![Recent Conversation Page](https://media.discordapp.net/attachments/798946362313408572/823879216525344768/unknown.png)

- **For Individual Project**

    - Flickr API

        - Function: Search images from Flickr.com and add them to the conversations when users ask general questions or questions that our chatbot cannot understand. With the help of these images, users might have a better understanding of what they want to know **visually**.

        - Code

          - Functions: ![Functions for FlickrAPI 1](https://media.discordapp.net/attachments/829133684774928408/831204989497507870/Code_for_FlickrAPI.png?width=666&height=791) <br> ![Functions for FlickrAPI 2](https://media.discordapp.net/attachments/829133684774928408/831206859339333684/Code_for_FlickrAPI2.png)

          <br>

          - Use of the function (It is implemented 3 times): ![Use of FlickrAPI](https://media.discordapp.net/attachments/829133684774928408/831205503605538876/Use_of_FlickrAPI.png)

        - Snippet: ![Flickr API](https://media.discordapp.net/attachments/829133684774928408/831187835008057354/Turn-28.png)

    - Wikipedia API

        - New Changes: This API was added as a part of the pos_tagging process but I have made a few changes to it: I used a new API package called Wikipediaapi, implemented this API to more conditions and topics, changed the unit of limiting the length of the output from sentences to characters, allowed searching with priority, and allowed the chatbot to inform the users when nothing is found in wikipedia.

        - Code

          - Function: ![Function for WikipediaAPI](https://media.discordapp.net/attachments/829133684774928408/831207286844162088/Code_for_WikipediaAPI.png?width=838&height=791)

          <br>

          - Use of WikipediaAPI (It is implemented 4 times): ![Use of WikipediaAPI](https://media.discordapp.net/attachments/829133684774928408/831207835269988442/Use_of_WikipediaAPI.png)

        - Explanation

            - **1. Imported a new API package called Wikipediaapi**

            <br>

            - **2. Implemented this API to more conditions and topics**

                - Before: works only when no answer can be found from the database (intent.json)

                - Now: works in general topics such as Japanese Food, Otaku Culture and so on.

                - Example

                    - Before this change: ![More Topics Assignment 3](https://media.discordapp.net/attachments/829133684774928408/830245517804044288/More_Topics_Assignment_3.png)

                    - After this change: ![More Topics Individual](https://media.discordapp.net/attachments/829133684774928408/829134317694484490/More_Topics_Individual.png?width=542&height=718)



        <br><br><br>

        - **3. Changed the unit of limiting the length of the output from sentences to characters ( use to be 3 sentence, not is like 300 words)**

            - Benefit: more control over the length of the output (sometimes sentences can get really long)

            - Example

                - Before: ![Lentgh Assignment 3](https://media.discordapp.net/attachments/829133684774928408/830245645645381662/Length_Assignment_3.png?width=544&height=718)

                - Now: ![Length Individual](https://media.discordapp.net/attachments/829133684774928408/830245786197032960/Length_Individual.png?width=538&height=717)



            <br><br><br>

        - **4. Search with priority**

            - Before this change: only use an integrated function and I don't know how it is used

            - After this change: designed a function by myself that search original input before generating 'recommended input'

            - Code change

                - Before this change: only a function from wikipedia package:  ![Priority A3](https://media.discordapp.net/attachments/829133684774928408/829135145613131876/Code_Priority_A3.png)

                - After this change: ![Priority Individual](https://media.discordapp.net/attachments/829133684774928408/829134808629903420/Code_Priority_Individual.png?width=768&height=719)

                <br><br><br>

        - **5. Inform the users when nothing is found in wikipedia**

            - Before this change: blank

            - After this change: a sentence that tells users about the situation

            - Example

                - Before this change: ![Not Found Assignment 3](https://media.discordapp.net/attachments/829133684774928408/830245945055903754/Not_Found_Assignment_3.png)

                - After this change: ![Not Found Individual](https://media.discordapp.net/attachments/829133684774928408/830246031684927508/Not_Found_Individual.png)

            <br><br><br>

<br>

## Team Members and nick name used in the project:
- **Khai Hung Luong (Hung)**: I'm 3rd year comsci student who loves reading books !
- **Anshul Dhariwal (Anshul)**: I am 3rd year COSC student and loves anything that is interesting to do!!
- **Jayant Puri (Jayant)**: I'm a 3rd year COSC student who loves watching anime!
- **Sirus Wang (Sirus)**: I'm a 3rd year COSC student who loves taking photos!
- **Shaohua Jiang (Joseph)**: I'm a 3rd year math student who loves snowboarding!

<br>

## References

Here is the link of an open-source program that helps us build our chatbot <br>
https://data-flair.training/blogs/python-chatbot-project/

Here is the link of stanfordcorenlp which is a Python wrapper for Stanford CoreNLP. <br>
https://github.com/Lynten/stanford-corenlp

Here is the link of a code guidance that help me build functions of Flickr API <br>
https://medium.com/@adrianmrit/creating-simple-image-datasets-with-flickr-api-2f19c164d82f

Here is the link of the documentation to WikipediaAPI package that helps me build the codes for this package <br>
https://pypi.org/project/Wikipedia-API/

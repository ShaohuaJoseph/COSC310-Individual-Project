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

## About Our Project: 
<br>

Our team chose incremental development as our SDLC model, generated a list of tasks based on each phase of the model, allocated time and manpower to each task based on duration and schedule with a WBS and a Gantt chart as explanation. Then, our team started planning for development. The role of the agent is Japan and anime expert and users are people who are interested in Japanese culture and anime and would love to talk and know more about Japanese culture and anime. The topics of the conversation are the general information and personal preferences of anime and the information of Japan such as people, religion, food, samurai and so on. The GitHub page of our project is this: https://github.com/shiro102/Chat-bot-team-20

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

<br>

## The Software Development Life Cycles:

<br>

### **Our Choice**: Incremental Development
<br>

### **Rationale**: 

<br>We choosed Incremental Development as our software development life cycle. Since more assignments about this project are expected to be published, some changes to this project might be required. As a result, we think that a model that is able to accommodate changes is most suitable for this project. Incremental development requires multiple versions of the project to be published frequently, so the model allows executable products to be generated earlier, and further modification can be done in later versions. In this way, modification is encouraged and the possibility of a complete failure of the product is reduced. The restriction of this model is that to rectify a task done in previous version requires modifications in all units and is time-consuming.

<br>

### Process: 
     1) Analyze requirements and Create Tasks:
 	 	i) Choosing a platform to publish the application
			a) Creating github account for each team member
			b) Creating  team github account
  		ii) Choose a software development cycle
  	 	iii) Creating WBS and Gantt charts.
		iv) Create Level-0 and Level-1 Data Flow Diagrams (DFDs)
  
    2) Establish design:
  		i) Choose a language and its corresponding IDE
 		ii) Choose two agents for the chatbot.
 		iii) Choose two topic for the chatbot
  		iv) Design the user interface for the chatbot

    3) Implementing design:
  		i) Build the dataset for the chatbot
  		ii) Implement the user interface. 
  		iii) Implement back-end (Training the chatbot)	
			a) Choose libraries
			b) Implement language toolkits
  		iv) Integrate the front end and back end.
  
    4) Testing:
  		i) Testing frequently asked questions and ambiguous questions.
  		ii) Testing and debugging language toolkits.
  		iii) Testing the interactive elements
  		iv) Record errors and fix them.
			a) Debugging
			b) Add code for error prevention
			c) Supplement and complete the dataset

    5) Publishing application:
 		i) Establish publishing date
 		ii) Synchronize each member’s work
		iii) Publish the application to GitHub
 	 	iv) New Presentation Video
	
--- 
## Old Work Breakdown Structure (WBS):
![WBS](https://cdn.discordapp.com/attachments/798946362313408572/817114483172442142/Final_1.jpg)
## New Work Breakdown Structure (WBS):
![WBS](https://media.discordapp.net/attachments/798946362313408572/825124672088834058/Final_1.jpg?width=1728&height=532)

## Old Gantt chart: 
![Gantt](https://cdn.discordapp.com/attachments/798946362313408572/818986258076401684/Gannt_Chart_Final.png)
## New Gantt chart: 
![Gantt](https://media.discordapp.net/attachments/798946362313408572/825142511991259162/Gannt_Chart_Final_2_r.png?width=1450&height=792)

<br>

## Insight of the contributors to this project

![Commit Branch](https://media.discordapp.net/attachments/829133684774928408/831287024556310538/Screen_Shot_2021-04-12_at_2.57.05_PM.png?width=1164&height=793)

<br>

## Limitations of the program submitted: 

-	The biggest limitation on the chatbot is that we don’t have a dataset that is large enough. We don’t have an enterprise-level development team and the dataset would be very limited and would only be applicable to certain situations.
-	The chatbot cannot really “understand” what the user is actually saying since overall, it’s a running algorithm.
-	All responses are randomized, and no certain output is determined.
-	There is no self-learning function implemented so the chatbot would not understand, or learn the user’s behavior, answers, patterns etc.
-	Fuzzy search is not supported so misspelling would lead to totally different answers.
-	The dialogues are not interconnected, and the chatbot would not make connections between them.
-	Assume the user only enters valid (no spelling errors) and “understandable” (within the scope of dataset) or otherwise the chatbot would reply with a response saying it doesn't understand your questions and would try to search an unknown Proper noun on wikipedia.

<br>

## Sample Outputs: 

### Possible Questions that you can ask from the chatbot:

1. Good day
2. What can you do?
3. Any anime to watch?
4. Top action anime?
5. What is the best adventure anime?
6. Any top-rated drama anime?
7. Best fantasy anime to recommend?
8. What are the top-rated comedy anime?
9. What is your favorite anime?
10.	Tell me about Konosuba!
11.	Who is your favorite character?
12.	What anime are you watching recently?
13.	Do you know about manga?
14.	Top-rated manga?
15.	What is your favorite manga?
16.	Tell me about Beserk!
17.	Who is your favorite Beserk character
18.	Manga that you read recently
19.	Recommend me manga
20.	Do you know about Manhwa?
21.	What are famous Manhwa?
22.	What is Otaku culture?
23.	What is anime convention?
24.	What are famous conventions?
25.	What convention do you want to vist?
26.	Tell me about Jump Festa!
27.	Tell me about Video games
28.	Tell me about Gacha
29.	What are famous gacha games?
30.	Tell me about Anime RPG
31.	What are famous Anime RPG?
32. That’s helpful
33. See you later!
34. Do you know about Jujutsu Kaisen?
35. I like Jujutsu Kaisen!

 <br>

### Text demo:

 

Turn-1  User : Good day!

  ![Turn-1](https://media.discordapp.net/attachments/829133684774928408/830984692912095282/Turn-1.png)

<br>	

Turn-2	User : What can you do?
	
  ![Turn-2](https://media.discordapp.net/attachments/829133684774928408/830985169690296401/Turn-2.png)

 <br>
Turn-3	User : Any anime to watch?

	Anime bot : Koe no Katachi
<br>
 
Turn-4	User : Top action anime?

	Anime bot : Top 5 Action Animes:
 	1) Fullmetal Alchemist: Brotherhood
 	2) Attack on Titans
 	3) Gintama
 	4) Hunter x Hunter
 	5) Code Geass
<br>
 
Turn-5	User : What is the best adventure anime?

	Anime bot : Top 5 Adventure Animes:
	1) Cowboy Bebop
 	2) Spirited Away
 	3) Mushishi
 	4) Made in Abyss
 	5) Vinland Saga
<br>
 
Turn-6	User : Any top-rated drama anime?

	Anime bot : Top 5 Drama Animes:
 	1) March Comes In Like A Lion
 	2) A Silent Voice
 	3) Clannad
 	4) Your Name.
 	5) Haikyuu!
<br>
 
Turn-7	User : Best fantasy anime to recommend?

	Anime bot : Top 5 Fantasy Animes:
 	1) Fate/Stay Night
 	2) RE:Zero
	3) One Piece
 	4) Weathering With You
	5) Mushoku Tensei: Jobless Reincarnation

 <br>
Turn-8	User : What are the top-rated comedy anime?

	Anime bot : Top 5 Comedy Animes:
 	1) Owarimonogatari
 	2) Grand Blue
 	3) Konosuba
 	4) Kaguya-Sama: Love is war
 	5) Horimiya

<br>
Turn-9	User : What is your favorite anime?

	Anime bot : I absolutely love Konosuba

<br>
Turn-10	User : Tell me about Konosuba!
	
  ![Turn-10](https://media.discordapp.net/attachments/829133684774928408/831185420837453874/Turn-10.png)

<br>
Turn-11	User : Who is your favorite character?

	Anime bot : I like Kazuma, the main protagantist of
	Konosuba, because he is really funny!

<br>
Turn-12	User : That's cool
	
	Anime bot : My pleasure

<br> 
Turn-13	User : What anime are you watching recently?

	Anime bot : Anime I am watching nowadays:
	1) Attack on Titans Final Season
	2) Dr. Stone: Stone Wars
 	3) Horimiya
 	4) Re:Zero Season 2 Part 2
 	5) Mushoku Tensei

 <br>
Turn-14 User : Do you know about manga?

 	Anime bot : Oh Yes! I love mangas too, they are
	just like comic books but japanese style.
	Many animes are adapted from manga.

<br>
Turn-15 User : Top-rated manga?

  	 Anime bot : Top 5 Mangas:
  	 1) Beserk
   	 2) JoJo's Bizarre Adventure
  	 3) One Piece
  	 4) Vagabond
  	 5) Monster

 <br>
Turn-16 User : What is your favorite manga?
 
 	Anime bot : Beserk is the best manga!

 <br>
Turn-17 User : Tell me about Beserk!

 	Anime bot : Plot for Beserk: Former mercenary,after
  	a tumultuous childhood, finally finds someone
   	he respects and believes he can trust, only to
	have everything fall apart when this person
	takes away everything important to him. Now
	marked for death he is relentlessly pursued
	by demonic beings.

<br>
Turn-18 User : Who is your favorite Beserk character

 	Anime bot : I like Guts, the main protagantist of
	Beserk, because he has a will of iron!

<br>
 Turn-19 User : Manga that you read recently

	 Anime bot : Manga I am reading nowadays:
	 1) Tokyo Ghoul
 	 2) Bleach
 	 3) Fairy Tail
 	 4) Solo Leveling
 	 5) Tower of God
 
<br>
 Turn-20 User: Recommend me manga

	 Anime bot : Nisekoi

<br>
 Turn-21 User : Do you know about Manhwa?

  ![Turn-21](https://media.discordapp.net/attachments/829133684774928408/831186118997049414/Turn-21.png)

 <br>
 Turn-22 User : What are famous Manhwa?
 
 	Anime bot : Famous Manhwa:
 	1) Solo Leveling
 	2) Tower of God
 	3) God of Highschool
 	4) Noblesse
 	5) Sweet Home
<br>

 Turn-23 User : What is Otaku culture?

  ![Turn-23](https://media.discordapp.net/attachments/829133684774928408/831186545687003156/Turn-23.png)

 <br>
 Turn- 24: What is anime convention?

  ![Turn-24](https://media.discordapp.net/attachments/829133684774928408/831186871261986816/Turn-24.png)

 <br>
 Turn-25 User : What are famous conventions?

 	Anime bot : Famous Conventions:
 	1) Comiket
 	2) Jump Festa
 	3) Tokyo Toy Show
 	4) AnimeJapan
 	5) World Cosplay Summit

 <br>
 Turn-26 User : What convention do you want to vist?

	 Anime bot : I really really want to visit Jump Festa,
	 to witness the glory of shounen.
<br>

 Turn-27 User : Tell me about Jump Festa!

  ![Turn-27](https://media.discordapp.net/attachments/829133684774928408/831187500990857246/Turn-27.png)
<br>
 
 Turn-28 User : Tell me about Video games

  ![Turn-28](https://media.discordapp.net/attachments/829133684774928408/831187835008057354/Turn-28.png)
<br>
 
 Turn-29 User : Tell me about Gacha

	 Anime bot : Gacha games are video games that
	 implement the gacha mechanic. Similar to
	 loot boxes in video games, gacha games
	 induce players to spend in-game currency to
	 receive a random virtual item.
<br>
 
 Turn-30 User : What are famous gacha games?

	 Anime bot : Popular Gacha Games:
	1) Genshin Impact
	2) Dragon Ball Legends
	3) Dragon Ball Dokkan Battle
	4) Fate/Stay Night
	5) Runterra

 <br>
Turn-31 User : Tell me about Anime RPG

	Anime bot : Anime RPGs are video games that
	allows players to take control of their favorite
	character from an anime and live their story.
	It ranges from open world games to hack &
	slash games.

 <br>
Turn-32 User : What are famous Anime RPG?

	Anime bot : Popular Anime RPG: 
	1) Person 5:Strikers
	2) Dragon Ball: Kakarot
	3) Final Fantasy 15
	4) Dragon Quest XI
	5) Dragon Ball: Xenoverse 2

<br>
Turn-33 User : Tell me about Japan?

  ![Turn-33](https://media.discordapp.net/attachments/829133684774928408/831188626729730118/Turn-33.png)
	
<br>
Turn-34 User : Tell me about People in Japan?

  ![Turn-34](https://media.discordapp.net/attachments/829133684774928408/831188893437132800/Turn-34.png)
	
<br>
	
Turn-35 User : Tell me about Religion in Japan?

  ![Turn-35](https://media.discordapp.net/attachments/829133684774928408/831189208357404682/Turn-35.png)
	
<br>
Turn-36 User : Tell me about food in Japan?

  ![Turn-36](https://media.discordapp.net/attachments/829133684774928408/831189515103240252/Turn-36.png)
	
<br>
Turn-37 User : Tell me about Samurais?

	Anime bot : In Japanese history, samurai culture and the role this
	military class played in shaping Japan is a fascinating one.
	Although samurai no longer exist, the influence of these great 
	warriors still manifests itself deeply in Japanese culture and
	samurai heritage can be seen all over Japan - be it a great castle,
	a carefully planned garden, or beautifully preserved samurai
	residences. It is also deeply ingrained in the psyche of the Japanese
	people.
	
 <br>
Turn-38 User : That's helpful!

	Anime bot : My pleasure

 <br>
Turn-39 User : See you later

	Anime bot : Bye! Come back again soon
	
	
	
	
### Here are two unique cases where the chatbot doesn't work as intended:

#### Case 1:

Turn-1 User : Explain to me what Computer Science is

  ![Fail2-Incomplete Search](https://media.discordapp.net/attachments/829133684774928408/831201770311123014/Fail2.png)



#### Case 2:

Turn-2 User:  Tell me about cat?
       
 ![Fail1-Cannot Understand](https://media.discordapp.net/attachments/829133684774928408/831200888403394580/Fail1.png)



<br><br><br>



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

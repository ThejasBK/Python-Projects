import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant
import sys

'''
The below code must be stored in a JSON file so that the python program can access it whenver needed.
{"intents": [
  {
    "tag": "greeting",
    "patterns": ["Hey", "Hello", "Hi", "What's up?", "Good Day"],
    "responses": ["Hello there!", "Hello, what can I do for you?"]
  },
  {
    "tag": "create_note",
    "patterns": ["New note", "Create a note"],
    "responses": [""]
  },
  {
    "tag": "add_todo",
    "patterns": ["New item", "Add an item"],
    "responses": [""]
  },
  {
    "tag": "show_todos",
    "patterns": ["Show my todos", "What is on my list"],
    "responses": [""]
  },
  {
    "tag": "exit",
    "patterns": ["Bye", "See you", "Quit", "Exit"],
    "responses": ["Thank you for spending time with me."]
  },
]}
'''

recognizer = speech_recognizer.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150) #rate is property, 150 is the value
#Creating an object to access the todo list
todo_list = ['Go Shopping', 'Clean Room']

#Greeting the user
def greeting():
  speaker.say("Hello, What can I do for you?")
  speaker.runAndWait()
  
  #Function to create and add new note
def create_note():
  global recognizer   #Making the variable global
  speaker.say("What do you want to write as note?")
  speaker.runAndWait()    #Asking for user input
  done = True
  #The try block is used in case the microphone fails  
  while done:
    try:         
      with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        #Accepting user voice input
        audio = recognizer.listen(mic)
        note = recognizer.recognize_google(audio)
        note = note.lower()
        speaker.say("Choose a filename!")
        speaker.runAndWait()
        recognizer.adjust_for_ambient_noise(mic, duration = 0.2) 
        #Accepting user filename
        audio = recognizer.listen(mic)
        filename = recognizer.recognize_google(audio)
        filename = filename.lower()
      with open(filename, 'w') as f:
        f.write(note)
        done = False
        #Terminating the while loop if listened properly
        speaker.say("New note successfully created")
        speaker.runAndWait()
    except speech_recognition.UnknownValueError:
      recognizer = speech_recognizer.Recognizer()
      speaker.say("I did not understand you. Please try again!")
      speaker.runAndWait()
      
#Speaking out the list
def show_todo():
  speaker.say("Your list contains the following elements")
  for item in todo_list:
    speaker.say(item)
  speaker.runAndWait()
  
#Adding elements to a todo list
def add_todo();
  global recognizer
  speaker.say("What item do you want to add?")
  speaker.runAndWait()
  done = True
  while done:
    try:
      with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration = 0.3)
        audio = recognizer.listen(mic)
        item = recognizer.recognize_google(audio)
        item = item.lower()
        todo_list.append(item)
        done = False
        speaker.say(item+" was added to the list!")
        speaker.runAndWait()
    except speech_recognition.UnknownValueError:
      recognizer = speech_recognition.Recognizer()
      speaker.say("I'm sorry, can you repeat it again!")
      speaker.runAndWait()
      
#Exiting from your assistant
def close():
  speaker.say("Bye. Coming back soon!")
  speaker.runAndWait()
  sys.exit(0)

mappings = {
  "greeting": hello,
  "create_node": create_node,
  "add_todo": add_todo,
  "show_todo": show_todo,
  "exit": close
}

#Training a model to recognize the intents
assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()
assistant.request()

while True:
  try:
    with speech_recognition.Microphone() as mic:
      recognizer.adjust_for_ambient_sound9mic, duration = 0.2)
      audio = recognizer.listen(mic)
      message = recognizer.recognize_google(audio)
      message = message.audio()
    assistant.request(message)
  except speech_recogniton.UnkownValueError:
    recognizer = speech_recognition.Recognizer()

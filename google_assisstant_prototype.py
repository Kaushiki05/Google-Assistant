import nltk
from nltk.chat.util import Chat, reflections

import pyttsx3
sp=pyttsx3.init()
sp.setProperty('rate',90)

import speech_recognition as sr
r=sr.Recognizer()

import webbrowser as wb

qapairs = (
    (r'(.*)search(.*)for me',
     ('Yeah sure', 'Yes I am searching%2for you')
    ),
  )  
cb = Chat(qapairs, reflections)

while True:
    with sr.Microphone() as source:
        print('say: ')
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if text == 'exit':
                break
            print('You said: ',text)
            resp = cb.respond(text)
            sp.say(resp)
            sp.runAndWait()
            if 'search' in text and 'for me' in text:
                t1 = text.split('search')[-1]
                t2 = t1.split('for me')[0].strip()
                #print(t2)
                url = 'https://www.flipkart.com/search?q=%s'%(t2)
                wb.open_new(url)
            print('-'*20)
        except Exception as e:
            print('Error')
            print('e')

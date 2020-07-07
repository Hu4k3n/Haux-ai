import speech_recognition as sr 
from googlesearch import search
import urllib
from bs4 import BeautifulSoup
import os
from playsound import playsound
from os import listdir
from os.path import isfile, join
import random
import urllib.request
import time

# mic_name = "HDA Intel PCH: ALC255 Analog (hw:0,0)"
mic_name="default"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 

def accept_speech ():
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source: 
        r.adjust_for_ambient_noise(source)
        play_sound(0)
        print ("How can I help, Huraken ?")
        audio = r.listen(source) 
        try: 
            text = r.recognize_google(audio) 
            print(text)
            return text
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

def youtube_search(search):
    textToSearch = str(search)
    query = textToSearch.replace(' ','+').replace('-','+')
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    i=str(html).find("\"/watch?v=")
    html=str(html)
    final=html[i+1:i+21]
    url='https://www.youtube.com'+str(final)
    print(url)
    os.system('firefox '+url)

def info(search_text):
    os.system('firefox https://google.com/search?q='+search_text.replace(' ', '+').replace('-', '+'))
    # i = 1
    # query = search_text
    # for url in search(query, stop=1):
    #     a = google_scrape(url)
    #     print (str(i) + ". " + a)
    #     os.system('firefox '+url)
def play_sound(i):
    i=int(i)
    dir='Documents/stuff/Ox/'
    if i==0 :
        u=([f for f in listdir(str(dir)+"audio/start/") if isfile(join(str(dir)+"audio/start/", f))])
        u=random.choice(u)
        playsound(str(dir)+"audio/start/"+str(u))
    elif i== 1 :
        u=([f for f in listdir(str(dir)+"audio/mid/") if isfile(join(str(dir)+"audio/mid/", f))])
        u=random.choice(u)
        playsound(str(dir)+"audio/mid/"+str(u))
    elif i==2 :
        u=([f for f in listdir(str(dir)+"audio/end/") if isfile(join(str(dir)+"audio/end/", f))])
        u=random.choice(u)
        playsound(str(dir)+"audio/end/"+str(u))
        
def main():
    flag=True
    while flag:
        cmd=accept_speech()
        if "search" in str(cmd) :
            print(cmd[7:])
            play_sound(1)
            info(cmd[7:])
        if "open" in str(cmd):
            play_sound(1)
            if "terminal" in str(cmd):
                os.system("gnome-terminal")
                print(cmd[5:])
                info(cmd[5:])
        if "close" in str(cmd):
            play_sound(1)
            if "browser" in str(cmd):
                os.system('pkill firefox')
            if "terminal" in str(cmd) :
                os.system('pkill gnome-terminal')
        if "play" in str(cmd):
            print (cmd[5:])
            play_sound(1)
            youtube_search(cmd[5:])
        if "kill yourself" in str(cmd) :
            play_sound(2)
            os.system('pkill python3')
        flag=False
    play_sound(2)
if __name__ == '__main__':
    main()
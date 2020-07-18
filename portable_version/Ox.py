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
        os.system("pkill gnome-terminal")
        # os.system("gnome-terminal -e \"cava\" --hide-borders --hide-toolbar --hide-menubar --title=desktopconsole")
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
    query = textToSearch.replace(' ','+').replace('-','+').replace("\'", "")
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
    os.system('firefox https://google.com/search?q='+search_text.replace("\'", "").replace(' ', '+').replace('-', '+'))
def play_sound(i):
    os.system("gnome-terminal -e \"vis -c .audiovis/cli-visualizer/examples/config\"")
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
    os.system("pkill gnome-terminal")
        
def main():
    flag=True
    found=True
    cmd=""
    while flag and found:
        found=False
        cmd=accept_speech()
        if "search" in str(cmd) :
            print(cmd[7:])
            play_sound(1)
            info(cmd[7:])
            found=True
        if "find" in str(cmd) :
            print(cmd[5:])
            play_sound(1)
            info(cmd[5:])
            found=True
        if "to do" in str(cmd) or "remind me" in str(cmd) :
            play_sound(1)
            os.system("todoist")
            found=True
        elif "open" in str(cmd):
            play_sound(1)
            if "terminal" in str(cmd):
                os.system("xfce4-terminal --hide-borders --hide-toolbar --hide-menubar --title=desktopconsole")
                found=True
            elif "telegram" in str(cmd) :
                os.system("telegram-desktop")
                found=True
            elif "discord" in str(cmd) :
                os.system("discord")
                found=True
            elif ("class" in str(cmd) or "classes" in str(cmd) or "classrooms" in str(cmd) or "classes" in str(cmd) or "classrooms" in str(cmd)) :
                os.system("firefox https://classroom.google.com/u/2/h")
                found=True
            elif ("youtube" in str(cmd) or "Youtube" in str(cmd)):
                os.system("firefox https://www.youtube.com/")
                found=True
            # else:
            #     print(cmd[5:])
            #     info(cmd[5:])
        if "close" in str(cmd):
            play_sound(1)
            if "browser" in str(cmd):
                os.system('pkill firefox')
                found=True
            if "terminal" in str(cmd) :
                os.system('pkill xfce4-terminal')
                os.system('pkill gnome-terminal')
                found=True
            if "telegram" in str(cmd) :
                os.system("pkill telegram-desktop")
                found=True
            if "discord" in str(cmd) :
                os.system("pkill discord")
                found=True
        if "Play" in str(cmd) or "play" in str(cmd):
            print (cmd[5:])
            play_sound(1)
            youtube_search(cmd[5:])
            found=True
        if "kill yourself" in str(cmd) or "bye" in str(cmd) :
            play_sound(2)
            os.system('pkill python3')
            found=True
        flag=False
    if not found:
        play_sound(1)
        info(cmd)    
    play_sound(2)

if __name__ == '__main__':
    main()
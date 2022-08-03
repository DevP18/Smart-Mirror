import tkinter as tk
from tkinter import Image, Label
import configparser
from tkinter.constants import TRUE
import traceback
from typing import Counter
import requests
from PIL import ImageTk,Image
from alexa import yt, ggsearch, wiki, date, timer, take_command
from calanderforDev import get_events
from Spotify import player
import datetime
import re
import urllib.request
import vlc
import pafy
import time
import os
import threading
import random



config = configparser.RawConfigParser()

config.read('C://Users//ashish//AppData//Local//Programs//Python//Python39//Doc//smart mirror//config.ini')
api_key = config['api_key']['key']
Long = config['api_key']['Long']
Lat = config['api_key']['Lat']


urls = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&exclude=current&appid={}'


master = tk.Tk()
master.title("Digital CLock")

Width_Screen = master.winfo_screenwidth()
Height_Screen = master.winfo_screenheight()

display = tk.Canvas(master, height=Height_Screen, width=Width_Screen, bg="black")
display.grid(columnspan=1000, rowspan= 1000)

counter = 0
counter1 = 0
musicPosition = 0
voice_dead = False
weather_checker = False
clockers = False
clocker_created = False



def get_Weather():
    result = requests.get(urls.format(Long, Lat, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_F = 9/5 * (temp_kelvin - 273.15) + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_F, icon, weather)
        return final

    else:
        return None    
def create_clock():
    global clock
    if clocker_created == False:
        clock = Label(master, font=("Calibri",50), bg="black",fg="white")
        clocker_created == True

def get_time():
    global clock
    if clockers == False:
            clock.grid(column=500, row=30)
            timeVar = datetime.datetime.now().strftime("%I:%M:%S:%p")
            clock.config(text=timeVar)
            clock.after(200,get_time)
    elif clockers == True:
            clock.destroy()


def reminders():
    events = get_events()
    countermax = 10
    counter = 0
    counter1 = 0
    event1 = []
    event_Description = []
    while countermax > counter:
        if counter == 0:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])           
            reminder1time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder1time.grid(column=10, row=50)
            reminder1Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder1Desc.grid(column=10, row=51)
            event1 = [] 
            event_Description = []
        elif counter == 1:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder2time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder2time.grid(column=10, row=65)
            reminder2Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder2Desc.grid(column=10, row=66)
            event1 = [] 
            event_Description = []
        elif counter == 2:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder3time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder3time.grid(column=10, row=80)
            reminder3Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder3Desc.grid(column=10, row=81)
            event1 = [] 
            event_Description = []
        elif counter == 3:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder4time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder4time.grid(column=10, row=95)
            reminder4Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder4Desc.grid(column=10, row=96)
            event1 = [] 
            event_Description = []
        elif counter == 4:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder5time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white", bd=1)
            reminder5time.grid(column=10, row=110)
            reminder5Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder5Desc.grid(column=10, row=111)
            event1 = []
            event_Description = [] 
        elif counter == 5:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder6time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder6time.grid(column=10, row=125)
            reminder6Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder6Desc.grid(column=10, row=126)
            event1 = [] 
            event_Description = []
        elif counter == 6:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder7time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white",)
            reminder7time.grid(column=10, row=140)
            reminder7Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder7Desc.grid(column=10, row=141)
            event1 = []
            event_Description = []
        elif counter == 7:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder8time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder8time.grid(column=10, row=155)
            reminder8Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder8Desc.grid(column=10, row=156)
            event1 = []
            event_Description = []
        elif counter == 8:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder9time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder9time.grid(column=10, row=170)
            reminder9Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder9Desc.grid(column=10, row=171)
            event1 = []
            event_Description = []

        elif counter == 9:
            event1.append(events[0][counter])
            event1.append(events[1][counter])
            event_Description.append(events[2][counter])
            reminder10time = Label(master, text=event1, font=("Calibri",20), bg="black", fg="white")
            reminder10time.grid(column=10, row=185)
            reminder10Desc = Label(master, text=event_Description, font=("Calibri",22), bg="black", fg="white")
            reminder10Desc.grid(column=10, row=185)
            event1 = []
            event_Description = []
        counter = counter + 1
        # if command == "stop":
        #     for e in events:
        #         if counter == 0:
        #             reminder1 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder1.destroy()
        #         elif counter == 1:
        #             reminder2 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder2.destroy()
        #         elif counter == 2:
        #             reminder3 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder3.destroy()
        #         elif counter == 3:
        #             reminder4 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder4.destroy()
        #         elif counter == 4:
        #             reminder5 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder5.destroy()
        #         elif counter == 5:
        #             reminder6 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder6.destroy()
        #         elif counter == 6:
        #             reminder7 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder7.destroy()
        #         elif counter == 7:
        #             reminder8 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder8.destroy()
        #         elif counter == 8:
        #             reminder9 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder9.destroy()
        #         elif counter == 9:
        #             reminder10 = Label(master, text=e, font=("Calibri",50), bg="black", fg="white")
        #             reminder10.destroy()
        #     exit()

def Music():
      global players
      global songs
      musicPosition = random.randint(0, 27)
      if MusyicOn == True:
            songs = os.listdir("C:/Users/ashish/Desktop/THesongs")
            players = vlc.MediaPlayer("C:/Users/ashish/Desktop/THesongs/" + songs[musicPosition])
            pass
      if MusyicOn == True:
            print("playing")
            players.play()
      elif MusyicOn == False:
            print("stopping")
            players.stop()

def playlist():
      global musicPosition, players, songs
      while MusyicOn == True:
            if players.is_playing() == 1:
                  time.sleep(3)
            elif players.is_playing() == 0:
                  musicPosition = random.randint(1, 27)
                  players = vlc.MediaPlayer("C:/Users/ashish/Desktop/THesongs/" + songs[musicPosition])
                  players.play()
                  time.sleep(2)
            elif MusyicOn == False:
                print("stopping")
                players.stop()
      else:
            return None

def pause(command):
    if "pause" in command:
        if YoutubeOn == True:
            player.pause()
            time.sleep(0.1)
        elif MusyicOn == True:
            players.pause()
            time.sleep(0.1)

def Music_stopper(command):
    if "stop" in command:
        if YoutubeOn == True:
            player.stop()
            time.sleep(0.1)
        elif MusyicOn == True:
            players.stop()
            time.sleep(0.1)


def show_yt(command):
    if 'stop' in command:
        exit()
    else:
        if 'play' in command and YoutubeOn == True:
            global player
            global Media
            Font = 30
            yt_Tub = tk.Frame(master, width=800, height=600, bg="black")
            yt_Tub.grid(column=500, row= 500)

            yt_Tub2 = tk.Frame(yt_Tub, bd=5)
            yt_Tub2.place(relwidth=1, relheight=1)
            Yt_Search = 'https://www.youtube.com/results?search_query=' + yt(command)

            html = urllib.request.urlopen(Yt_Search)
            search_results = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = ("https://www.youtube.com/watch?v=" + search_results[0])

            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url
 

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            player.set_media(Media)
            player.set_hwnd(yt_Tub2.winfo_id())
            player.play()
            time.sleep(0.2)
            return Font
        
def volume(command):
    if "volume" in command:
            command = command.replace('volume', '')
            command = int(command)
            if command <= 100 and command >= 0:
                if YoutubeOn == True:
                    player.audio_set_volume(command)
                    time.sleep(0.1)
                    print ("Hello cunts")
                elif MusyicOn == True:
                    print ("Hello cunt")
                    players.audio_set_volume(command)
                    time.sleep(0.1)


def full_screen(command):
    if 'full screen' in command and YoutubeOn == True:

        full_tub = tk.Frame(master, width=1000, height=900, bg="black")
        full_tub.grid(column=500, row= 500)

        Full_screen = tk.Frame(full_tub, bd=5)
        Full_screen.place(relwidth=1, relheight=1)


        time_stomp = player.get_position()
        time.sleep(0.1)
        player.stop()
        print (time_stomp)
        player.set_media(Media)
        player.set_hwnd(Full_screen.winfo_id())
        player.play()
        player.set_position(time_stomp)



def search(Fontt):
    global counter
    while weather_checker == True:
        weather = get_Weather()
        if weather and counter == 1:
                print (weather[1])
                location_Label = Label(master, text='Location', font=("Calibri",Fontt), bg="black",fg="white")
                location_Label.grid(column=499, row=500)

                weather_L = Label(master, bitmap='', font=("Calibri",Fontt), bg="black",fg="white")
                weather_L.grid(column=500, row=501)

                temp_Label = Label(master, text='Temperature', font=("Calibri",Fontt), bg="black", fg="white")
                temp_Label.grid(column=500, row=502)
                temp_Label['text'] = '{:.2f}°F'.format(weather[2])

                location_Label['text'] = '{}'.format(weather[0])

                image1 = Image.open("C:\\Users\\ashish\\AppData\\Local\\Programs\\Python\\Python39\\Doc\\smart mirror\\Weather_Icon\\" + weather[3] + ".png")
                photo = ImageTk.PhotoImage(image1)
                photogrid = Label(master, image=photo, bg="#263D42")
                photogrid.image = photo
                photogrid.grid(column=500, row=503)

                weather_L['text'] = weather[4]
                time.sleep(3)
                counter = 2

    location_Label.destroy()
    weather_L.destroy()
    temp_Label.destroy()
    location_Label.destroy()
    photogrid.destroy()
    return None


def reseta():
    Fontt = 40
    global counter, MusyicOn, YoutubeOn
    global musicPosition
    global weather_checker
    global voice_dead
    global clocker_created
    global clockers
    while voice_dead == False:
        time.sleep(2)
        print("speak")
        command = take_command()
        weathers = threading.Thread(target=search, args=[Fontt])
        if (counter == 0):
            MusyicOn = False
            YoutubeOn = False
            counter = 1
        if "search" in command:
            ggsearch(command)
        elif "what is" in command:
            ggsearch(command)
        elif 'play some music' in command:
            MusyicOn = True
            Music()
            musicPosition = 0
            time.sleep(2)
            YoutubeOn = False
            songlist = threading.Thread(target=playlist)
            songlist.start()
        elif 'play spotify' in command:
            player()
        elif "play" in command:
            MusyicOn = False
            YoutubeOn = True
            weather_checker = False
            try:
                show_yt(command)
            except NameError or traceback:  
                show_yt(command)
        elif "resume" in command:
            pause(command)
        elif "pause" in command:
            pause(command)
        elif "reminders" in command:
            reminders(command)
        elif "what's the date" in command:
            if clocker_created == False:
                create_clock()
            get_time()
            date()
        elif "what's the time" in command:
            search(command, Fontt)
            if clocker_created == False:
                create_clock()
            get_time()
            time.sleep(0.2)
            timer()
        elif "what's all" in command:
            if weather_checker == False:
                weather_checker = True
                weathers.start()
            if clocker_created == False:
                create_clock()
            get_time()
            timer()
        elif "who is" in command:
            wikisearch = command.replace("who is", '')
            wiki(wikisearch)
        elif "volume" in command:
            volume(command)
        elif "full screen" in command:
            full_screen(command)
            return search, get_time
        elif 'stop':
            Music_stopper(command)
            weather_checker = False
            MusyicOn = False
            YoutubeOn = False
            voice_dead = True
            clockers = True
            show_yt(command)
            get_time()
            reminders(command)
            exit()

voicer = threading.Thread(target=reseta)
voicer.start()
master.mainloop()



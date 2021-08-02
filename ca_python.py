#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Andre Goncalves
"""

from tkinter import *
from tkinter import messagebox
import requests
import json
from datetime import date
import time as tm

root = Tk()


#Get date
today = date.today()


#Formate the date
f_today = today.strftime("%A, %B %d, %Y")
today_label = Label(root, text=f_today, fg="black", bg="snow2", font=("Time News Roman", 20, "bold"))
today_label.pack()


#Get time
time = tm.strftime('%H:%M:%S')
time_label = Label(root, text=time, fg="black", bg="snow2", font=("Time News Roman", 20, "bold"))
time_label.pack()


type = 'sports'
apiKey = 'Y3137dbdbcc7c4440bd909e23d6f7caef'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=ie&category={type}&apiKey=3137dbdbcc7c4440bd909e23d6f7caef'
 
 
class NewsApp:
    global apiKey, type
 
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("News")

 
        #====variables========#
        self.newsCatButton = []
        self.newsCat = ["business", "entertainment", "general", "health",
                         "science", "sports", "technology"]
 
        #========title frame===========#
        bg_color = "snow2"
        text_area_bg = "#606060"
        basic_font_color = "black"
        
        

         #=======Category frame=======#
        Frame1 = LabelFrame(self.root, text="Category", font=(
            "times new roman", 20, "bold"), bg=bg_color, fg=basic_font_color, bd=10, relief=GROOVE)
        Frame1.place(x=0, y=70, width=300, relheight=0.88)
        
         #=======Longitude and Latitude frame=======#
        Frame3 = LabelFrame(self.root, text="Latitude + Longitude", font=(
            "times new roman", 20, "bold"), bg=bg_color, fg=basic_font_color, bd=10, relief=GROOVE)
        Frame3.place(x=0, y=450, width=300, relheight=0.88)
        
        #=======Input box Latitude=======#
        screen = Entry(Frame3, width=40)
        screen.pack( padx=10, pady =10)
        screen.insert(0,"Please enter your Latitude")
        
        #=======Input box Longitude=======#
        screen1 = Entry(Frame3, width=40)
        screen1.pack( padx=10, pady =10)
        screen1.insert(0,"Please enter your Longitude")
        

        
         #=======search button=======#       
        b1 = Button (Frame3, text="search", padx =10, pady = 10)
        b1.pack()
        
        location = ("     ",screen, "+-", "     ", screen1)
        
        #=======location api for latitude and longitude=======#
        def openCage(Frame3, screen, screen1):
            # api-endpoint 
            URL = "https://api.opencagedata.com/geocode/v1/json"

            # defining a params dict for the parameters to be sent to the API 
            PARAMS = {'q':str(screen) + "+" + str(screen1),
                      'key':'0003b51dcf5d4f45aae3536bd7c63694'} 
  
            # sending get request and saving the response as response object 
            r = requests.get(url = URL, params=PARAMS) 

            # extracting data in json format 
            data = r.json() 
    
            city = data['results'][0]['components']['city']
            country = data['results'][0]['components']['country']
            

            openCage(screen,screen1)        
     
        #=======for loop for category buttons=======#
        for i in range(len(self.newsCat)):
            b = Button(Frame1, text=self.newsCat[i].upper(
            ), width=20, bd=7, font="arial 15 bold")
            b.grid(row=i, column=0, padx=10, pady=5)
            b.bind('<Button-1>', self.Newsarea)
            self.newsCatButton.append(b)
            
        
            
 
        #=======news frame=======#
        Frame2 = Frame(self.root, bd=7, relief=GROOVE)
        Frame2.place(x=320, y=80, relwidth=0.7, relheight=0.8)
        news_title = Label(Frame2, text="News", font=("arial", 20, "bold"), bd=15, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Frame2, orient=VERTICAL)
        self.txtarea = Text(Frame2, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), bg="seashell2", fg="black")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.insert(
            END, "PLEASE SELECT ANY CATEGORY TO SHOW THE NEWS. ")
        self.txtarea.pack(fill=BOTH, expand=1)
        
        
       
        
     #=======News function=======#   
    def Newsarea(self, event):
        

        
        type = event.widget.cget('text').lower()
        #=======API URL=======#
        BASE_URL = f'http://newsapi.org/v2/top-headlines?country=ie&category={type}&apiKey=3137dbdbcc7c4440bd909e23d6f7caef'
        #=======Top of page text=======#
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, f"\n Welcome to Today's News\n")
        self.txtarea.insert(
            END, "--------------------------------------------------------------------\n")
        try:
            #=======json=======#
            articles = (requests.get(BASE_URL).json())['articles']
            
            #=======if statement to check if there's smth to show=======#
            if(articles != 0):
                #=======for loop to print all the news - by title and information=======#
                for i in range(len(articles)):
                    self.txtarea.insert(END, f"{articles[i]['title']}\n")
                    self.txtarea.insert(
                        END, f"{articles[i]['description']}\n\n")
                    self.txtarea.insert(END, f"{articles[i]['content']}\n\n")
                    self.txtarea.insert(
                        END, f"read more...{articles[i]['url']}\n")
                    self.txtarea.insert(
                        END, "--------------------------------------------------------------------\n")
                    self.txtarea.insert(
                        END, "--------------------------------------------------------------------\n")
                    
             #=======in case there's nothing to show, this message will appear on the screen=======#       
            else:
                self.txtarea.insert(END, "Sorry, there's no news available")
                #=======if smth went wrong, error message=======#
        except Exception as e:
            messagebox.showerror(
                'ERROR', "Sorry can't connect to internet or some issues with newsapp :'(")
 
 

obj = NewsApp(root)
root.mainloop()
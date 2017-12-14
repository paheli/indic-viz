# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 08:32:51 2016

@author: ravsh
"""
#!/usr/bin/python
print('Content-type: text/html\r\n\r')
# -*- coding: iso-8859-1 -*-

from scipy import spatial
import cgitb
import cgi
cgitb.enable()
import numpy as np
import io
#import math
import heapq
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
#from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plot
#matplotlib.use("TkAgg")
#import itertools
import random 
from mpldatacursor import datacursor
import matplotlib.patches as mpatches
from collections import defaultdict
import Tkinter as Tkinter
import matplotlib
from PIL import ImageTk, Image
import os
import pandas as pd
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
LARGE_FONT= ("Verdana", 10)
LARGE_FONT1= ("Verdana", 10, "bold")
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        #Tkinter.Tk.iconbitmap(self, default="iit_logo.ico")
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.label= Tkinter.Label(self,text="Select the Mode",font=LARGE_FONT1)
        self.label.grid(row=0, columnspan=2, sticky='W')
        self.opt=Tkinter.StringVar(self)
        self.opt.set("Enter the Number of words")
        choices = ["Enter the Number of words","Show top similar words"]
        options = Tkinter.OptionMenu( self, self.opt, *choices,command=self.func)
        options.configure(font=LARGE_FONT1, justify="center")
        options.grid(row=0, column=2, sticky='EW')
        self.label= Tkinter.Label(self,text="Enter the Word",font=LARGE_FONT1)
        self.label.grid(row=1,column=0, columnspan=2, sticky='W')
        
        
        
        self.entryVariable_word = Tkinter.StringVar()
        self.entry_word = Tkinter.Entry(self,textvariable=self.entryVariable_word,font=LARGE_FONT)
        self.entry_word.grid(row=2,columnspan=2,sticky='EW')
        self.entry_word.bind("<Return>", self.OnPressEnter)
        
        self.label= Tkinter.Label(self,text="Nos of English Words",font=LARGE_FONT1)
        self.label.grid(row=1,column=2,sticky='W')
        
        self.entryVariable_nos_word_en = Tkinter.IntVar()
        self.entry_nos_word_en = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_en,font=LARGE_FONT)
        self.entry_nos_word_en.grid(column=2,row=2,columnspan=1,sticky='EW')
        self.entry_nos_word_en.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_en.set(2)
        
        self.label= Tkinter.Label(self,text="Nos of Hindi Words",font=LARGE_FONT1)
        self.label.grid(row=1, column=3,columnspan=1, sticky='W')
        
        self.entryVariable_nos_word_hin = Tkinter.IntVar()
        self.entry_nos_word_hin = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_hin,font=LARGE_FONT)
        self.entry_nos_word_hin.grid(column=3,row=2,columnspan=1,sticky='EW')
        self.entry_nos_word_hin.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_hin.set(2)
        
        self.label= Tkinter.Label(self,text="Nos of Bengali Words",font=LARGE_FONT1)
        self.label.grid(row=1, column=4,columnspan=1, sticky='W')
        
        self.entryVariable_nos_word_bong = Tkinter.IntVar()
        self.entry_nos_word_bong = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_bong,font=LARGE_FONT)
        self.entry_nos_word_bong.grid(column=4,row=2,columnspan=1,sticky='EW')
        self.entry_nos_word_bong.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_bong.set(2)
        
        self.label= Tkinter.Label(self,text="Nos of Tamil words",font=LARGE_FONT1)
        self.label.grid(row=1, column=5,columnspan=1, sticky='W')
        
        self.entryVariable_nos_word_tam = Tkinter.IntVar()
        self.entry_nos_word_tam = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_tam,font=LARGE_FONT)
        self.entry_nos_word_tam.grid(column=5,row=2,columnspan=1,sticky='EW')
        self.entry_nos_word_tam.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_tam.set(2)
        
        self.label= Tkinter.Label(self,text="Nos of Gujarati words",font=LARGE_FONT1)
        self.label.grid(row=1, column=6,columnspan=1, sticky='W')
        
        self.entryVariable_nos_word_guj = Tkinter.IntVar()
        self.entry_nos_word_guj = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_guj,font=LARGE_FONT)
        self.entry_nos_word_guj.grid(column=6,row=2,columnspan=1,sticky='EW')
        self.entry_nos_word_guj.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_guj.set(2)
        
        self.label= Tkinter.Label(self,text="Nos of Marathi words",font=LARGE_FONT1)
        self.label.grid(row=1, column=7,columnspan=1, sticky='W')
        
        self.entryVariable_nos_word_mrt = Tkinter.IntVar()
        self.entry_nos_word_mrt = Tkinter.Entry(self,textvariable=self.entryVariable_nos_word_mrt,font=LARGE_FONT)
        self.entry_nos_word_mrt.grid(column=7,row=2,columnspan=1,sticky='E')
        self.entry_nos_word_mrt.bind("<Return>", self.OnPressEnter)
        self.entryVariable_nos_word_mrt.set(2)
        
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        self.label= Tkinter.Label(self,text="Or Try these words",font=LARGE_FONT1)
        self.label.grid(row=3, column=0,columnspan=8, sticky='W')
        
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        
        
        button = Tkinter.Button(self,text=u"Find !",
                                command=self.OnButtonClick, bg="white",foreground="Blue",font=LARGE_FONT1)
        button.grid(column=0,row=5,columnspan=8,sticky='EW')
        
        
        
        self.label_en= Tkinter.Label(self,text="English Words",font=LARGE_FONT1)
        self.label_en.grid(row=6, column=0,columnspan=4, sticky='W')
        self.labelVariable_en = Tkinter.StringVar()
        label_en = Tkinter.Label(self,textvariable=self.labelVariable_en,
                              anchor="w",fg="red",bg="white",font=LARGE_FONT,wraplength=600,justify='left')
        label_en.grid(column=0,row=7,columnspan=4,sticky='EW',pady=(0,15))
        
        self.label_hin= Tkinter.Label(self,text="Hindi Words",font=LARGE_FONT1)
        self.label_hin.grid(row=6, column=4,columnspan=4, sticky='W')
        self.labelVariable_hin = Tkinter.StringVar()
        label_hin = Tkinter.Label(self,textvariable=self.labelVariable_hin,
                              anchor="w",fg="dark green",bg="white",font=LARGE_FONT,wraplength=700,justify='left')
        label_hin.grid(column=4,row=7,columnspan=4,sticky='EW',pady=(0,15))
        
        self.label_bong= Tkinter.Label(self,text="Bengali Words",font=LARGE_FONT1)
        self.label_bong.grid(row=8, column=0,columnspan=4, sticky='W')
        self.labelVariable_bong = Tkinter.StringVar()
        label_bong = Tkinter.Label(self,textvariable=self.labelVariable_bong,
                              anchor="w",fg="blue",bg="white",font=LARGE_FONT,wraplength=600,justify='left')
        label_bong.grid(column=0,row=9,columnspan=4,sticky='EW',pady=(0,15))
        
        self.label_tam= Tkinter.Label(self,text="Tamil Words",font=LARGE_FONT1)
        self.label_tam.grid(row=8, column=4,columnspan=4, sticky='W')
        self.labelVariable_tam = Tkinter.StringVar()
        label_tam = Tkinter.Label(self,textvariable=self.labelVariable_tam,
                              anchor="w",fg="purple",bg="white",font=LARGE_FONT,wraplength=700,justify='left')
        label_tam.grid(column=4,row=9,columnspan=4,sticky='EW',pady=(0,15))
        
        self.label_guj= Tkinter.Label(self,text="Gujarati Words",font=LARGE_FONT1)
        self.label_guj.grid(row=10, column=0,columnspan=4, sticky='W')
        self.labelVariable_guj = Tkinter.StringVar()
        label_guj = Tkinter.Label(self,textvariable=self.labelVariable_guj,
                              anchor="w",fg="orange",bg="white",font=LARGE_FONT,wraplength=600,justify='left')
        label_guj.grid(column=0,row=11,columnspan=4,sticky='EW',pady=(0,15))

        self.label_mrt= Tkinter.Label(self,text="Marathi Words",font=LARGE_FONT1)
        self.label_mrt.grid(row=10, column=4,columnspan=4, sticky='W')
        self.labelVariable_mrt = Tkinter.StringVar()
        label_mrt = Tkinter.Label(self,textvariable=self.labelVariable_mrt,
                              anchor="w",fg="brown",bg="white",font=LARGE_FONT,wraplength=700,justify='left')
        label_mrt.grid(column=4,row=11,columnspan=4,sticky='EW',pady=(0,15))
#==============================================================================
#         self.label_graph = Tkinter.Label(self, text="Graph",font=LARGE_FONT1)
#         self.label_graph.grid(column=0,row=17,columnspan=8,sticky='W')
#==============================================================================
        
#        self.graph=Tkinter.Canvas(self,width=2000, height=1000)
#        self.graph.grid(column=0,row=18,columnspan=8,sticky='W')

     
#        f = Figure(figsize=(5,5), dpi=100)
#        a = f.add_subplot(111)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#    
#    
#        self.canvas = FigureCanvasTkAgg(f, self)
#        self.canvas.show()
#        self.canvas.get_tk_widget().pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH, expand=True)

#        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
#        self.toolbar.update()
#        self.canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=True)

        #self.canvas = FigureCanvasTkAgg(self,self.container)
        #self.container.get_tk_widget().pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH, expand=True)
#
#        self.toolbar = NavigationToolbar2TkAgg(self,self.container)
#        self.toolbar.update()
#        self.canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=True)
        
        self.grid_columnconfigure(0,weight=1)
        self.update()     
        self.entry_word.focus_set()
        self.entry_word.selection_range(0, Tkinter.END)
        self.entry_nos_word_en.selection_range(0,Tkinter.END)
        self.entry_nos_word_hin.selection_range(0,Tkinter.END)
        self.entry_nos_word_bong.selection_range(0,Tkinter.END)
        self.entry_nos_word_tam.selection_range(0,Tkinter.END)
        self.entry_nos_word_guj.selection_range(0,Tkinter.END)
        self.entry_nos_word_mrt.selection_range(0,Tkinter.END)
        #self.canvas.stop_event_loop()
    
    def func(self,arg):
        if self.opt.get()==str("Enter the Number of words"):
            self.option=1 
            print("enter value")
        else:
            self.option=0
            print("all words")
            
        return self.option    
    
    def OnButtonClick(self):
        
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.entryVariable_word.get(),self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.entryVariable_word.get())
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
        
        
    def OnPressEnter(self,event):
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.entryVariable_word.get(),self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.entryVariable_word.get())
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='EW')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
    
    def OnButtonClick_link1(self):
        self.entryVariable_word.set(self.freq_words[0])

        if self.func(self)==1:

            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[0],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[0])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='EW')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
            
        
    def OnButtonClick_link2(self):
        self.entryVariable_word.set(self.freq_words[1])
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[1],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            print(eng_word,hin_word)
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[1])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
        
        
    def OnButtonClick_link3(self):
        self.entryVariable_word.set(self.freq_words[2])            
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[2],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[2])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
        
        
    def OnButtonClick_link4(self):
        self.entryVariable_word.set(self.freq_words[3])
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[3],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[3])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
            
    def OnButtonClick_link5(self):
        self.entryVariable_word.set(self.freq_words[4])
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[4],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[4])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
        
    def OnButtonClick_link6(self):
        self.entryVariable_word.set(self.freq_words[5])
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[5],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[5])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
        
    def OnButtonClick_link7(self):
        self.entryVariable_word.set(self.freq_words[6])
        if self.func(self)==1:
        
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word,nos_en,nos_hin,nos_bong,nos_tam,nos_guj,nos_mrt=self.GetSimWord(self.freq_words[6],self.entryVariable_nos_word_en.get(),self.entryVariable_nos_word_hin.get(),self.entryVariable_nos_word_bong.get(),self.entryVariable_nos_word_tam.get(),self.entryVariable_nos_word_guj.get(),self.entryVariable_nos_word_mrt.get())
            if nos_en==self.entryVariable_nos_word_en.get():
               self.labelVariable_en.set(eng_word)
            else: 
               self.labelVariable_en.set(eng_word+" (Found Only %r English Words)" %nos_en) 
               
            if nos_hin==self.entryVariable_nos_word_hin.get():
               self.labelVariable_hin.set(hin_word)
            else: 
               self.labelVariable_hin.set(hin_word+" (Found Only %r Hindi Words)" %nos_hin)
            if nos_bong==self.entryVariable_nos_word_bong.get():
               self.labelVariable_bong.set(bong_word)
            else: 
               self.labelVariable_bong.set(bong_word+" (Found Only %r Bengali Words)" %nos_bong)
            if nos_tam==self.entryVariable_nos_word_tam.get():
               self.labelVariable_tam.set(tam_word)
            else: 
               self.labelVariable_tam.set(tam_word+" (Found Only %r Tamil Words)" %nos_tam)
            if nos_guj==self.entryVariable_nos_word_guj.get():
               self.labelVariable_guj.set(guj_word)
            else: 
               self.labelVariable_guj.set(guj_word+" (Found Only %r Gujarati Words)" %nos_guj)
            if nos_mrt==self.entryVariable_nos_word_mrt.get():
               self.labelVariable_mrt.set(mrt_word)
            else: 
               self.labelVariable_mrt.set(mrt_word+" (Found Only %r Marathi Words)" %nos_mrt)   
    #==============================================================================
    #         self.photo = ImageTk.PhotoImage(Image.open(self.entryVariable_word.get()+'.png'))
    #         self.graph.create_image(1500/2, 400/2, anchor=Tkinter.CENTER, image=self.photo)
    #==============================================================================
            self.entry_word.focus_set()
            self.entry_word.selection_range(0, Tkinter.END)
            #os.remove(self.entryVariable_word.get()+'.png')
            self.entryVariable_nos_word_en.set(2)
            self.entryVariable_nos_word_hin.set(2)
            self.entryVariable_nos_word_bong.set(2)
            self.entryVariable_nos_word_tam.set(2)
            self.entryVariable_nos_word_guj.set(2)
            self.entryVariable_nos_word_mrt.set(2)
            
            
        elif self.func(self)==0: 
            eng_word,hin_word,bong_word,tam_word,guj_word,mrt_word=self.GetSimWordAll(self.freq_words[6])
            
            self.labelVariable_en.set(eng_word)
            self.labelVariable_hin.set(hin_word)
            self.labelVariable_bong.set(bong_word)
            self.labelVariable_tam.set(tam_word)
            self.labelVariable_guj.set(guj_word)
            self.labelVariable_mrt.set(mrt_word)
            
            
        
        self.freq_words=['happy','বৃহস্পতিবার','அதை','તૈયાર','வருகிறார்','जाहीर','खिलाफ','জুলাই','person','આવેલી','ছেলে','பால்','सुरक्षा','experience','सूत्रों','પહોંચી','அருகில்','কমিটি','वीज','treatment','ચામાં','ঘোষণা','প্রশাসন','brother','दर्ज','जाणार','সরকারের','અલગારી','अधिकारियों','பேசியதாவது','બન્ને','knowledge','இல்லாமல்','ছোট','काळात']
        self.freq_words = set(self.freq_words)
        self.freq_words = random.sample(self.freq_words, 7)
        button1 = Tkinter.Button(self,text=self.freq_words[0],
                                command=self.OnButtonClick_link1,font=LARGE_FONT)
        button1.grid(column=0,row=4,columnspan=1,sticky='EW')
        button2= Tkinter.Button(self,text=self.freq_words[1],
                                command=self.OnButtonClick_link2,font=LARGE_FONT)
        button2.grid(column=2,row=4,columnspan=1,sticky='EW')
        button3 = Tkinter.Button(self,text=self.freq_words[2],
                                command=self.OnButtonClick_link3,font=LARGE_FONT)
        button3.grid(column=3,row=4,columnspan=1,sticky='EW')
        
        button4 = Tkinter.Button(self,text=self.freq_words[3],
                                command=self.OnButtonClick_link4,font=LARGE_FONT)
        button4.grid(column=4,row=4,columnspan=1,sticky='Ew')
        button5 = Tkinter.Button(self,text=self.freq_words[4], 
                                command=self.OnButtonClick_link5,font=LARGE_FONT)
        button5.grid(column=5,row=4,columnspan=1,sticky='EW')
        button6= Tkinter.Button(self,text=self.freq_words[5],
                                command=self.OnButtonClick_link6,font=LARGE_FONT)
        button6.grid(column=6,row=4,columnspan=1,sticky='EW')
        button7 = Tkinter.Button(self,text=self.freq_words[6],
                                command=self.OnButtonClick_link7,font=LARGE_FONT)
        button7.grid(column=7,row=4,columnspan=1,sticky='EW')
        
        return
     
     
    def GetSimWord(self,a,b,c,d,e,f,g):
        query_word =a
        nos_word_en =b
        nos_word_hin =c
        nos_word_bong =d
        nos_word_tam=e
        nos_word_guj=f
        nos_word_mrt=g
       # nos_word=nos_word_en+nos_word_hin+nos_word_bong+nos_word_tam+nos_word_guj+nos_word_mrt
        top_sim_list_en=[]
        top_sim_list_hin=[]
        top_sim_list_bong=[]
        top_sim_list_tam=[]
        top_sim_list_guj=[]
        top_sim_list_mrt=[]
        sim_list_en=[]
        sim_list_tam=[]
        sim_list_guj=[]
        sim_list_mrt=[]
        sim_list_hin=[]
        sim_list_bong=[]
        sim_word_list=[]
        sim_word_list_1=[]
        sim_word_list_2=[]
        sim_word_list_3=[]
       # words_list_en=[]
       #words_list_hin=[]
       # words_list_bong=[]
        words_list_tam=[]
        #words_list_guj=[]
        #words_list_mrt=[]
        #component_matrix1_en=[]
        #component_matrix2_en=[]
        #component_matrix1_hin=[]
        #component_matrix2_hin=[]
        #component_matrix1_bong=[]
        #component_matrix2_bong=[]
        
        cos_sim_rest_tam=[]
        cos_sim_list=[]
        cos_sim_list_en=[]
        cos_sim_list_hin=[]
        cos_sim_list_bong=[]
        cos_sim_list_tam=[]
        cos_sim_list_guj=[]
        cos_sim_list_mrt=[]
        word_cat=[]
        word_cat_en=[]
        word_cat_hin=[]
        word_cat_bong=[]
        word_cat_tam=[]
        word_cat_guj=[]
        word_cat_mrt=[]
        top_word_cat=[]
        top_word_cat_en=[]
        top_word_cat_hin=[]
        top_word_cat_bong=[]
        top_word_cat_tam=[]
        top_word_cat_guj=[]
        top_word_cat_mrt=[]
        vec_list=[]
        word_vec_rest_tam=[]
        top1component_matrix=[]
        top2component_matrix=[]
        i=0  
        j=0
        del_dup=[]
        top_word=[]
        efont = {'fontname':'Arial'}
        hfont = {'fontname':'Lohit Devanagari'}
        bfont={'fontname':'Lohit Bengali'}
        gfont={'fontname':'Lohit Gujarati'}
        tfont={'fontname':'Samyak Tamil'}
        def pca2(data, pc_count = None):
               return PCA(n_components = pc_count).fit(data).transform(data)
        
        print(query_word)
        a=query_word.decode("utf-8")

        print(a,ord(a[0]))
        if (ord(a[0])>=65) and (ord(a[0])<=122):
            print('english')
            with io.open("en-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
        if (ord(a[0])>=2304) and (ord(a[0])<=2431):
            a=a+'H'
            print('hindi')
            with io.open("en-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               wordlist=re.split(',|-',line)
               if a==(wordlist[0]):
                   i=i+1
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):

                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
            if i==0:           
                a=a[:-1]+'M' 
                print(a)
                print('marathi')            
                with io.open("mrt-sim.txt", encoding="utf-8") as infile:
                 for line in infile:
                     
                   wordlist=re.split(',|-',line)
                   if a==(wordlist[0]):
                       wordlist=wordlist[2:-1]
                       print(wordlist)
                       for words in wordlist:
                           #words=str(words)
                           if (ord(words[0])>=65) and (ord(words[0])<=122):
                                top_sim_list_en.append(words) 
                           elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                                if words[-1]=='H':
                                    top_sim_list_hin.append(words)
                                else:
                                    top_sim_list_mrt.append(words)
                           elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                                top_sim_list_bong.append(words)
                           elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                                top_sim_list_tam.append(words)
                           elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                                top_sim_list_guj.append(words)            
                        
                        
        if (ord(a[0])>=2432) and (ord(a[0])<=2559):
            print('ben')
            with io.open("bong-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
                        
                        
                        
                        
        if (ord(a[0])>=2944) and (ord(a[0])<=3071):
            print('tamil')
            with io.open("tam-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)                
                        
        if (ord(a[0])>=2688) and (ord(a[0])<=2815):
            print('guj')
            with io.open("guj-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)                 
                            
                        
                   
                        
           
        top_sim_list_en=top_sim_list_en[:nos_word_en]
        top_sim_list_hin=top_sim_list_hin[:nos_word_hin]
        top_sim_list_bong=top_sim_list_bong[:nos_word_bong]
        top_sim_list_mrt=top_sim_list_mrt[:nos_word_mrt]
        top_sim_list_guj=top_sim_list_guj[:nos_word_guj]
        top_sim_list_tam=top_sim_list_tam[:nos_word_tam]
        
       
       

#        print(top_word_cat_en,top_word_cat_hin,top_word_cat_bong,top_word_cat_tam,top_word_cat_guj,top_word_cat_mrt)
        top_sim_word_list= top_sim_list_en+top_sim_list_hin+top_sim_list_bong+ top_sim_list_tam+top_sim_list_guj+ top_sim_list_mrt
        
#        print(top_sim_word_list)
#        print("--------------------------------------")
        
        print(top_sim_list_en)
        print(top_sim_list_hin)
        print(top_sim_list_bong)
        print(top_sim_list_mrt)
        print(top_sim_list_guj)
        print(top_sim_list_tam)
        
        if len(top_sim_list_en):    
            count=0
            with io.open("en-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_en):
                        break
                    wordlist_1=line_1.split(' ')
                
                    for word in top_sim_list_en:                    
                        if wordlist_1[0]==word:
                                print(word)
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_hin):    
            count=0
            with io.open("hin-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_hin):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_hin:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:]  
                                vec_list.append(vec)
                                #word=str(word)
                                word=word[:-1]
                                top_word.append(word)
        if len(top_sim_list_bong):    
            count=0
            with io.open("bong-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_bong):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_bong:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_mrt):    
            count=0
            with io.open("mrt-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_mrt):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_mrt:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                #word=str(word)
                                word=word[:-1]
                                top_word.append(word)
        if len(top_sim_list_guj):    
            count=0
            with io.open("guj-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_guj):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_guj:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_tam):    
            count=0
            with io.open("tam-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_tam):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_tam:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)                        
                                
        
      
        for i in range(len(top_sim_list_hin)):
            top_sim_list_hin[i]=(top_sim_list_hin[i])[:-1]
        
        for i in range(len(top_sim_list_mrt)):
            top_sim_list_mrt[i]=(top_sim_list_mrt[i])[:-1]
        
        
        if len(top_word)==0:
            
            fig = plot.figure(figsize=(18,8)) 
            #ax = fig.add_subplot(111)
            plot.grid() 
            plot.xlabel('1st Principal compenent')
            plot.ylabel('2nd Principal component')
            plot.title('t-NSE Representation')
            #plot.savefig(query_word+'.png')
            #print(nos_word_en,nos_word_hin,nos_word_bong,nos_word_tam,nos_word_guj,nos_word_mrt)
            return ((', ').join(top_sim_list_en)), ((', ').join(top_sim_list_hin)), ((', ').join(top_sim_list_bong)),((', ').join(top_sim_list_tam)),((', ').join(top_sim_list_guj)),((', ').join(top_sim_list_mrt)),len(top_sim_list_en), len(top_sim_list_hin), len(top_sim_list_bong),len(top_sim_list_tam),len(top_sim_list_guj),len(top_sim_list_mrt)
        
        
        else:
                        
            print (vec_list)
#                print(len(vec_list))
            print(top_word)
#                for x in vec_list:
        
##                    print(len(x))
##                    print("#####################")
            vec_array=np.array(vec_list, dtype=float) 
            print(vec_array)
            model=TSNE(n_components=2, random_state=0)
            top_vec_component=model.fit_transform(vec_array)
            print(top_vec_component)
            top_vec_component=top_vec_component.tolist()
            for i in range(len(top_vec_component)):
                   top_vec_component[i].insert(0, top_word[i])
            tnse_en=top_vec_component[:len(top_sim_list_en)]
            tnse_hin=top_vec_component[len(top_sim_list_en):len(top_sim_list_hin)+len(top_sim_list_en)]
    
            tnse_bong=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)]
            tnse_mrt=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)]
            tnse_guj=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj)]
            tnse_tam=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj):+len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj)+len(top_sim_list_tam)]
            
            print(top_vec_component)
            print(tnse_en,tnse_hin, tnse_bong, tnse_mrt,tnse_guj, tnse_tam)
            
            
            #plot.close()
            data_en=pd.DataFrame(tnse_en,columns=['A', 'B', 'C'])
            data_hin=pd.DataFrame(tnse_hin,columns=['A', 'B', 'C'])
            data_bong=pd.DataFrame(tnse_bong,columns=['A', 'B', 'C'])
            data_mrt=pd.DataFrame(tnse_mrt,columns=['A', 'B', 'C'])
            data_guj=pd.DataFrame(tnse_guj,columns=['A', 'B', 'C'])
            data_tam=pd.DataFrame(tnse_tam,columns=['A', 'B', 'C'])
            Graph = plot.figure(figsize=(18,8)) 
            ax = Graph.add_subplot(111)
            Graph.canvas.set_window_title('Graphical Representation')
            #colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(top_word)))
            #font_hin={'family':'Mangal'}
            #font_bong={'family':'SolaimanLipi'}
            data_en['A'] = data_en['A'].astype('str')
            data_en['B'] = data_en['B'].astype('float64') 
            data_en['C'] = data_en['C'].astype('float64')
            data_hin['A'] = data_hin['A'].astype('str')
            data_hin['B'] = data_hin['B'].astype('float64') 
            data_hin['C'] = data_hin['C'].astype('float64')
            data_bong['A'] = data_bong['A'].astype('str')
            data_bong['B'] = data_bong['B'].astype('float64') 
            data_bong['C'] = data_bong['C'].astype('float64')
            data_mrt['A'] = data_mrt['A'].astype('str')
            data_mrt['B'] = data_mrt['B'].astype('float64') 
            data_mrt['C'] = data_mrt['C'].astype('float64')
            data_guj['A'] = data_guj['A'].astype('str')
            data_guj['B'] = data_guj['B'].astype('float64') 
            data_guj['C'] = data_guj['C'].astype('float64')
            data_tam['A'] = data_tam['A'].astype('str')
            data_tam['B'] = data_tam['B'].astype('float64') 
            data_tam['C'] = data_tam['C'].astype('float64')
            print(data_en)            
            print(data_en['A'], data_en['B'])
            plot.scatter(data_en['B'],data_en['C'], marker='o', color="red")
            a=plot.plot(data_en['B'],data_en['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_en['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**efont)
            
            plot.scatter(data_hin['B'],data_hin['C'], marker='o', color="green")
            a=plot.plot(data_hin['B'],data_hin['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_hin['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**hfont)
            
            plot.scatter(data_mrt['B'],data_mrt['C'], marker='o', color="brown")
            a=plot.plot(data_mrt['B'],data_mrt['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_mrt['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**hfont)
            
            plot.scatter(data_guj['B'],data_guj['C'], marker='o', color="orange")
            a=plot.plot(data_guj['B'],data_guj['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_guj['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**gfont)
            
            
            plot.scatter(data_tam['B'],data_tam['C'], marker='o', color="purple")
            a=plot.plot(data_tam['B'],data_tam['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_tam['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**tfont)
            
            plot.scatter(data_bong['B'],data_bong['C'], marker='o', color="blue")
            a=plot.plot(data_bong['B'],data_bong['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_bong['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**bfont)
            
            classes = ['English Words','Hindi Words','Bengali Words','Marathi Words', 'Gujarati Words', 'Tamil Words']
            class_colours = ['red','green','blue','brown','orange','purple']
            recs = []
            for i in range(0,len(class_colours)):
                   recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))

            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            plot.legend(recs,classes,loc='center left', bbox_to_anchor=(1, 0.5))
            
            plot.title('t-SNE Representation')
            #axes = plot.gca()
            #axes.set_xlim([-0.05,0.05])
            #axes.set_ylim([-0.05,0.0005])
            plot.grid()  
            plot.show(block=False)
            #print(nos_word_en,nos_word_hin,nos_word_bong,nos_word_tam,nos_word_guj,nos_word_mrt)
            return (((', ').join(top_sim_list_en)), ((', ').join(top_sim_list_hin)), ((', ').join(top_sim_list_bong)),((', ').join(top_sim_list_tam)),((', ').join(top_sim_list_guj)),((', ').join(top_sim_list_mrt)),len(top_sim_list_en), len(top_sim_list_hin), len(top_sim_list_bong),len(top_sim_list_tam),len(top_sim_list_guj),len(top_sim_list_mrt))
        
            
    def GetSimWordAll(self,a):
        query_word =a
        
       # nos_word=nos_word_en+nos_word_hin+nos_word_bong+nos_word_tam+nos_word_guj+nos_word_mrt
        top_sim_list_en=[]
        top_sim_list_hin=[]
        top_sim_list_bong=[]
        top_sim_list_tam=[]
        top_sim_list_guj=[]
        top_sim_list_mrt=[]
        i=0
        vec_list=[]
      
        top_word=[]
        efont = {'fontname':'Arial'}
        hfont = {'fontname':'Lohit Devanagari'}
        bfont={'fontname':'Lohit Bengali'}
        gfont={'fontname':'Lohit Gujarati'}
        tfont={'fontname':'Samyak Tamil'}
        def pca2(data, pc_count = None):
               return PCA(n_components = pc_count).fit(data).transform(data)
        
        print(query_word)
        a=query_word.decode("utf-8")
        if (ord(a[0])>=65) and (ord(a[0])<=122):
            print('english')
            with io.open("en-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
        if (ord(a[0])>=2304) and (ord(a[0])<=2431):
            a=a+'H'
            print('hindi')
            with io.open("en-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               wordlist=re.split(',|-',line)
               if a==(wordlist[0]):
                   i=i+1
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
            if i==0:           
                a=a[:-1]+'M' 
                print(a)
                print('marathi')            
                with io.open("mrt-sim.txt", encoding="utf-8") as infile:
                 for line in infile:
                     
                   wordlist=re.split(',|-',line)
                   if a==(wordlist[0]):
                       wordlist=wordlist[2:-1]
                       print(wordlist)
                       for words in wordlist:
                           #words=str(words)
                           if (ord(words[0])>=65) and (ord(words[0])<=122):
                                top_sim_list_en.append(words) 
                           elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                                if words[-1]=='H':
                                    top_sim_list_hin.append(words)
                                else:
                                    top_sim_list_mrt.append(words)
                           elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                                top_sim_list_bong.append(words)
                           elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                                top_sim_list_tam.append(words)
                           elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                                top_sim_list_guj.append(words)            
                        
                        
        if (ord(a[0])>=2432) and (ord(a[0])<=2559):
            print('ben')
            with io.open("bong-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)
                        
                        
                        
                        
        if (ord(a[0])>=2944) and (ord(a[0])<=3071):
            print('tamil')
            with io.open("tam-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)                
                        
        if (ord(a[0])>=2688) and (ord(a[0])<=2815):
            print('guj')
            with io.open("guj-sim.txt", encoding="utf-8") as infile:
             for line in infile:
               i=i+1 
               wordlist=re.split(',|-',line)
               if wordlist[0]==query_word:
                   wordlist=wordlist[2:-1]
                   print(wordlist)
                   for words in wordlist:
                       #words=str(words)
                       if (ord(words[0])>=65) and (ord(words[0])<=122):
                            top_sim_list_en.append(words) 
                       elif (ord(words[0])>=2304) and (ord(words[0])<=2431):
                            if words[-1]=='H':
                                top_sim_list_hin.append(words)
                            else:
                                top_sim_list_mrt.append(words)
                       elif ((ord(words[0])>=2432) and (ord(words[0])<=2559)):
                            top_sim_list_bong.append(words)
                       elif ((ord(words[0])>=2944) and (ord(words[0])<=3071)):
                            top_sim_list_tam.append(words)
                       elif ((ord(words[0])>=2688) and (ord(words[0])<=2815)):
                            top_sim_list_guj.append(words)                 
                            
                        
                   
                        
           

       
       

#        print(top_word_cat_en,top_word_cat_hin,top_word_cat_bong,top_word_cat_tam,top_word_cat_guj,top_word_cat_mrt)
        top_sim_word_list= top_sim_list_en+top_sim_list_hin+top_sim_list_bong+ top_sim_list_tam+top_sim_list_guj+ top_sim_list_mrt
        
#        print(top_sim_word_list)
#        print("--------------------------------------")
        
        print(top_sim_list_en)
        print(top_sim_list_hin)
        print(top_sim_list_bong)
        print(top_sim_list_mrt)
        print(top_sim_list_guj)
        print(top_sim_list_tam)
        
        if len(top_sim_list_en):    
            count=0
            with io.open("en-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_en):
                        break
                    wordlist_1=line_1.split(' ')
                
                    for word in top_sim_list_en:                    
                        if wordlist_1[0]==word:
                                print(word)
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_hin):    
            count=0
            with io.open("hin-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_hin):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_hin:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:]  
                                vec_list.append(vec)
                                #word=str(word)
                                word=word[:-1]
                                top_word.append(word)
        if len(top_sim_list_bong):    
            count=0
            with io.open("bong-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_bong):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_bong:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_mrt):    
            count=0
            with io.open("mrt-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_mrt):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_mrt:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                #word=str(word)
                                word=word[:-1]
                                top_word.append(word)
        if len(top_sim_list_guj):    
            count=0
            with io.open("guj-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_guj):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_guj:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)
                                
        if len(top_sim_list_tam):    
            count=0
            with io.open("tam-vec.txt", encoding="utf-8") as infile:
                for line_1 in infile:
                    if count==len(top_sim_list_tam):
                        break
                    wordlist_1=line_1.split(' ')
                    for word in top_sim_list_tam:                    
                        if wordlist_1[0]==word:
                                count += 1
                                vec = wordlist_1[1:-1]  
                                vec_list.append(vec)
                                top_word.append(word)                        
                                
        
      
        for i in range(len(top_sim_list_hin)):
            top_sim_list_hin[i]=(top_sim_list_hin[i])[:-1]
        
        for i in range(len(top_sim_list_mrt)):
            top_sim_list_mrt[i]=(top_sim_list_mrt[i])[:-1]
        
        
        if len(top_word)==0:
            
            fig = plot.figure(figsize=(12,6)) 
            #ax = fig.add_subplot(111)
            plot.grid() 
            plot.xlabel('1st Principal compenent')
            plot.ylabel('2nd Principal component')
            plot.title('t-SNE Representation')
            #plot.savefig(query_word+'.png')
            #print(nos_word_en,nos_word_hin,nos_word_bong,nos_word_tam,nos_word_guj,nos_word_mrt)
            return ((', ').join(top_sim_list_en)), ((', ').join(top_sim_list_hin)), ((', ').join(top_sim_list_bong)),((', ').join(top_sim_list_tam)),((', ').join(top_sim_list_guj)),((', ').join(top_sim_list_mrt))
        
        
        else:
                        
            print (vec_list)
#                print(len(vec_list))
            print(top_word)
#                for x in vec_list:
        
##                    print(len(x))
##                    print("#####################")
            vec_array=np.array(vec_list, dtype=float) 
            print(vec_array)
            model=TSNE(n_components=2, random_state=0)
            top_vec_component=model.fit_transform(vec_array)
            print(top_vec_component)
            top_vec_component=top_vec_component.tolist()
            for i in range(len(top_vec_component)):
                   top_vec_component[i].insert(0, top_word[i])
            tnse_en=top_vec_component[:len(top_sim_list_en)]
            tnse_hin=top_vec_component[len(top_sim_list_en):len(top_sim_list_hin)+len(top_sim_list_en)]
    
            tnse_bong=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)]
            tnse_mrt=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)]
            tnse_guj=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt):len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj)]
            tnse_tam=top_vec_component[len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj):+len(top_sim_list_hin)+len(top_sim_list_en)+len(top_sim_list_bong)+len(top_sim_list_mrt)+len(top_sim_list_guj)+len(top_sim_list_tam)]
            
            print(top_vec_component)
            print(tnse_en,tnse_hin, tnse_bong, tnse_mrt,tnse_guj, tnse_tam)
            
            
            #plot.close()
            data_en=pd.DataFrame(tnse_en,columns=['A', 'B', 'C'])
            data_hin=pd.DataFrame(tnse_hin,columns=['A', 'B', 'C'])
            data_bong=pd.DataFrame(tnse_bong,columns=['A', 'B', 'C'])
            data_mrt=pd.DataFrame(tnse_mrt,columns=['A', 'B', 'C'])
            data_guj=pd.DataFrame(tnse_guj,columns=['A', 'B', 'C'])
            data_tam=pd.DataFrame(tnse_tam,columns=['A', 'B', 'C'])
            Graph = plot.figure(figsize=(18,8)) 
            ax = Graph.add_subplot(111)
            Graph.canvas.set_window_title('Graphical Representation')
            #colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(top_word)))
            #font_hin={'family':'Mangal'}
            #font_bong={'family':'SolaimanLipi'}
            data_en['A'] = data_en['A'].astype('str')
            data_en['B'] = data_en['B'].astype('float64') 
            data_en['C'] = data_en['C'].astype('float64')
            data_hin['A'] = data_hin['A'].astype('str')
            data_hin['B'] = data_hin['B'].astype('float64') 
            data_hin['C'] = data_hin['C'].astype('float64')
            data_bong['A'] = data_bong['A'].astype('str')
            data_bong['B'] = data_bong['B'].astype('float64') 
            data_bong['C'] = data_bong['C'].astype('float64')
            data_mrt['A'] = data_mrt['A'].astype('str')
            data_mrt['B'] = data_mrt['B'].astype('float64') 
            data_mrt['C'] = data_mrt['C'].astype('float64')
            data_guj['A'] = data_guj['A'].astype('str')
            data_guj['B'] = data_guj['B'].astype('float64') 
            data_guj['C'] = data_guj['C'].astype('float64')
            data_tam['A'] = data_tam['A'].astype('str')
            data_tam['B'] = data_tam['B'].astype('float64') 
            data_tam['C'] = data_tam['C'].astype('float64')
            print(data_en)            
            print(data_en['A'], data_en['B'])
            plot.scatter(data_en['B'],data_en['C'], marker='o', color="red")
            a=plot.plot(data_en['B'],data_en['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_en['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**efont)
            
            plot.scatter(data_hin['B'],data_hin['C'], marker='o', color="green")
            a=plot.plot(data_hin['B'],data_hin['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_hin['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**hfont)
            
            plot.scatter(data_mrt['B'],data_mrt['C'], marker='o', color="brown")
            a=plot.plot(data_mrt['B'],data_mrt['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_mrt['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**hfont)
            
            plot.scatter(data_guj['B'],data_guj['C'], marker='o', color="orange")
            a=plot.plot(data_guj['B'],data_guj['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_guj['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**gfont)
            
            
            plot.scatter(data_tam['B'],data_tam['C'], marker='o', color="purple")
            a=plot.plot(data_tam['B'],data_tam['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_tam['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**tfont)
            
            plot.scatter(data_bong['B'],data_bong['C'], marker='o', color="blue")
            a=plot.plot(data_bong['B'],data_bong['C'], marker='o', linestyle='', visible=False)
            datacursor(a, hover=True, point_labels=data_bong['A'], bbox=dict(fc='yellow'),
            formatter=lambda **kwargs: kwargs['point_label'][0], xytext=(0, 25),**bfont)
            
            classes = ['English Words','Hindi Words','Bengali Words','Marathi Words', 'Gujarati Words', 'Tamil Words']
            class_colours = ['red','green','blue','brown','orange','purple']
            recs = []
            for i in range(0,len(class_colours)):
                   recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))

            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            plot.legend(recs,classes,loc='center left', bbox_to_anchor=(1, 0.5))
            
            plot.title('t-SNE Representation')
#            axes = plot.gca()
#            axes.set_xlim([-0.01,0.01])
#            axes.set_ylim([-0.01,0.01])
            plot.grid()  
            plot.show(block = False)
            #print(nos_word_en,nos_word_hin,nos_word_bong,nos_word_tam,nos_word_guj,nos_word_mrt)
            return (((', ').join(top_sim_list_en)), ((', ').join(top_sim_list_hin)), ((', ').join(top_sim_list_bong)),((', ').join(top_sim_list_tam)),((', ').join(top_sim_list_guj)),((', ').join(top_sim_list_mrt)))
        
    
        
    
    
    

        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Word2Vec Application')
    #app.iconbitmap(default="iit_logo.ico")
    app.mainloop()
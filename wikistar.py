"""Importing Module"""

from tkinter import *
import wikipedia
import tkinter.messagebox as thh
import pygame

"""Starting Code"""

root = Tk()
root.geometry("865x675")
root.maxsize(865, 655)
root.minsize(865, 655)
root.title("WikiStar--By Aryan Tiwari")
root.config(bg="#FF1493")
root.iconbitmap("resource/wikistaricon.ico")



"""Functions"""

def wifi():
    import socket
    IPaddress=socket. gethostbyname(socket. gethostname())
    if IPaddress=="127.0.0.1":
        thh.showerror("Failed", "Check Internet Connection")
    else:
        find()


def find():
    p = wikipedia.summary(query.get(), sentences = 2)
    answer.delete("1.0", END)
    pygame.mixer.init()
    pygame.mixer.music.load("resource/wikiStarf.wav")
    pygame.mixer.music.play()
    answer.insert(1.0, p)
 

"""Main Program"""

title = Label(root, text="WikiStar", font="lucida 40 bold", fg="#FFD700", bg="#FF1493" )
title.pack(pady=20)

query = StringVar()

query = Entry(root, font="hevetica 18 bold", width=50)
query.pack()

get_answer = Button(root,text="Get Answer", bg="yellow", font="lucida 20 bold", fg="blue", command=wifi)
get_answer.pack(pady=10)

answer = Text(root, font="lucida 20 bold", height=13)
answer.pack()


    

root.mainloop()


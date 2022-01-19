#!/usr/bin/env python
# coding: utf-8


import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
import sqlite3 as sqltor
import blockchain

conn=sqltor.connect('main.db') #main database
cursor=conn.cursor() #main cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS poll
                    (name)""")

def voting_screen():
    global screen2
    global image1
    global image2
    global image3
    global image4
    
    screen2 = Toplevel(screen)
    screen2.title("Voting Screen")
    screen2.geometry("1100x500")
    
    image1 = ImageTk.PhotoImage(Image.open("obama1.png"))
    label1 = Label(screen2,image=image1)
    label1.grid(row=2, column=0)
    

    image2 = ImageTk.PhotoImage(Image.open("brando.jpg"))
    label2 = Label(screen2,image=image2)
    label2.grid(row=2, column=1)

    image3 = ImageTk.PhotoImage(Image.open("leonardo.jpg"))
    label3 = Label(screen2,image=image3)
    label3.grid(row=2, column=2)

    image4 = ImageTk.PhotoImage(Image.open("brad.jpg"))
    label4 = Label(screen2,image=image4)
    label4.grid(row=2, column=3)
    
    Button(screen2,text='VOTE',command=obama_click).grid(row=4,column=0,padx=30)
    Button(screen2,text='VOTE',command=brando_click).grid(row=4,column=1,padx=30)
    Button(screen2,text='VOTE',command=leo_click).grid(row=4,column=2,padx=30)
    Button(screen2,text='VOTE',command=brad_click).grid(row=4,column=3,padx=30)
    Button(screen2,text="Close the Window", command=screen2.destroy).grid(row=6,column=2,padx=40)
    
def obama_click():
    vote = "obama"     
    blockchain_data=username_bc+","+password_bc+","+vote    
    flag2 = 0
    fileRead=open("vote_history.txt", "r")
    for line in fileRead: 
            line_list = line.strip().split(",")    
            if (username_bc == line_list[0] and password_bc == line_list[1]):
                flag2 = 1        
                break
            
    if flag2 == 1:
        messagebox.showinfo('Error!',"Your have already voted! You can't vote again!")
    else:
        messagebox.showinfo('Success!',"Your vote added to the blockchain successfuly!")   
        file=open("vote_history.txt", "a")
        file.write(blockchain_data+"\n")     
        file.close()
        blockchain.add_block(blockchain_data)        
    fileRead.close()


def brando_click():
    vote = "brando"
    blockchain_data=username_bc+","+password_bc+","+vote    
    flag2 = 0
    fileRead=open("vote_history.txt", "r")
    for line in fileRead: 
            line_list = line.strip().split(",")    
            if (username_bc == line_list[0] and password_bc == line_list[1]):
                flag2 = 1        
                break
            
    if flag2 == 1:
        messagebox.showinfo('Error!',"Your have already voted! You can't vote again!")
    else:
        messagebox.showinfo('Success!',"Your vote added to the blockchain successfuly!")   
        file=open("vote_history.txt", "a")
        file.write(blockchain_data+"\n")     
        file.close()
        blockchain.add_block(blockchain_data)    
    fileRead.close()

def leo_click():
    vote = "leonardo"
    blockchain_data=username_bc+","+password_bc+","+vote    
    flag2 = 0
    fileRead=open("vote_history.txt", "r")
    for line in fileRead: 
            line_list = line.strip().split(",")    
            if (username_bc == line_list[0] and password_bc == line_list[1]):
                flag2 = 1        
                break
            
    if flag2 == 1:
        messagebox.showinfo('Error!',"Your have already voted! You can't vote again!")
    else:
        messagebox.showinfo('Success!',"Your vote added to the blockchain successfuly!")   
        file=open("vote_history.txt", "a")
        file.write(blockchain_data+"\n")     
        file.close()
        blockchain.add_block(blockchain_data)        
    fileRead.close()


def brad_click():
    vote = "brad"
    blockchain_data=username_bc+","+password_bc+","+vote    
    flag2 = 0
    fileRead=open("vote_history.txt", "r")
    for line in fileRead: 
            line_list = line.strip().split(",")    
            if (username_bc == line_list[0] and password_bc == line_list[1]):
                flag2 = 1        
                break
            
    if flag2 == 1:
        messagebox.showinfo('Error!',"Your have already voted! You can't vote again!")
    else:
        messagebox.showinfo('Success!',"Your vote added to the blockchain successfuly!")   
        file=open("vote_history.txt", "a")
        file.write(blockchain_data+"\n")     
        file.close()
        blockchain.add_block(blockchain_data)               
    fileRead.close()

def login():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Login")
    screen3.geometry("750x300")
    
    #any variable outside the function needs to be globalized, else it will cause error
    global login_username
    global login_password
    global username_login
    global password_login
    
    login_username = StringVar()
    login_password = StringVar()
    
    Label(screen3, text = "Please enter details below")
    
    Label(screen3, text = "Username *").grid(row=0,column=1,padx=30)
    username_login=Entry(screen3, textvariable = login_username)
    username_login.grid(row=1,column=1,padx=30)
    Label(screen3, text = "Password *").grid(row=2,column=1,padx=30)
    password_login=Entry(screen3, textvariable = login_password)
    password_login.grid(row=3,column=1,padx=30)
    Label(screen3, text = "").grid(row=4,column=1,padx=30)
    Button(screen3, text = "Login", width = 10, height = 1, command = login_control).grid(row=5,column=1,padx=50)
    Button(screen3,text="Close the Window", command=screen3.destroy).grid(row=7,column=1,padx=40)
    
def login_control():
    global username_bc
    global password_bc
    
    username_bc = login_username.get()
    password_bc = login_password.get()
    
    if username_bc == "" or password_bc == "":
        Label(screen3, text = "Login not successful..Please go back to previous screen and provide valid information!").grid(row=6,column=0,padx=30)
    else:         
        flag=0
        file1 = open('voters.txt','r')
        for line in file1: 
            line_list = line.strip().split(",")    
            if (username_bc == line_list[0] and password_bc == line_list[1]):
                flag = 1
                break
        file1.close()        
 
        # clear the fields once the register is completed
        username_login.delete(0, 'end')
        password_login.delete(0, 'end')
    
        if flag == 1:
            Label(screen3, text = "Login successful. You can vote now!").grid(row=3,column=2,padx=30)
            Button(screen3,text = "Vote", command = voting_screen).grid(row=4,column=2,padx=30,pady=20)
        else:
            Label(screen3, text = "Login not successful..You are not able to vote!").grid(row=3,column=0,padx=30)

def exit():
    screen.destroy()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Blockchain Voting")
    Label(text = "Welcome to the Blockchain E-Voting Application", font = "Calibri 14 bold").grid(row=1,column=2)    
    Button(text = "Login",command=login).grid(row=3,column=2,padx=30,pady=20)
    Button(text = "Exit",command=exit).grid(row=4,column=2,padx=30,pady=20)
 
    screen.mainloop()
    
#main_screen()
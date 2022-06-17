from tkinter import *
import os
import hashlib
import datetime
import time
import mysql.connector
import tkinter.messagebox as tkMessageBox
from datetime import datetime
from pyfingerprint.pyfingerprint import PyFingerprint
from mysql.connector import Error

def Database2():
    
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                         database='smartdoor',
                                         user='salwana',
                                         password='awe123')
    cursor = conn.cursor()

##database
def Database():

    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                         database='smartdoor',
                                         user='salwana',
                                         password='awe123')
    cursor = conn.cursor()

def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        screen.destroy()
        exit()


def run():
    os.system('python3 backupenroll.py')
    
def run2():
    os.system('python3 authenticate.py')


def register_user():

    run()
    Database()

    userid_info = userid.get()
    username_info = username.get()
    phonenumber_info = userid.get()
    email_info = username.get()
  

 #applying empty validation
    if userid=='' or username==''or phonenumber=='' or email=='':
        message.set("fill the empty field!!!")
    else:
        cursor.execute("INSERT INTO `user` (userid, username, phonenumber, email) VALUES(%s, %s, %s, %s)", (str(userid.get()), str(username.get()), str(phonenumber.get()), str(email.get())))
        conn.commit()
        userid.set("")
        username.set("")
        phonenumber.set("")
        email.set("")
        cursor.close()
        conn.close()
    Label(screen1, text = "Registration sucess" , fg = "green" , font = ("calibri",11)).pack()
   
def login_verify():
    run2()
    Database2()
   
    fingerid_info = fingerid.get()
    sname_info = sname.get()
    
     

 #applying empty validation

    if fingerid=='' or sname=='':
        message.set("fill the empty field!!!")
    else:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
# Assuming you have a cursor named cursor you want to execute this query on:
        #cursor.execute('insert into log(fingerid,sname, eventdt) values(%s, %s , %s)', (fingerid,sname, formatted_date))
        cursor.execute("INSERT INTO `log` (fingerid,userid, sname,eventdt) VALUES(%s,%s,%s, %s)", (str(fingerid.get()),str(fingerid.get()), str(sname.get()), formatted_date))
        #val = (fingerid,userid,sname,timestamp)

       
        conn.commit()

        fingerid.set("")
        sname.set("")
     
        cursor.close()
        conn.close()
        
        Label(screen2, text = "Login sucess" , fg = "green" , font = ("calibri",11)).pack()

    
    
    
    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global userid
    global username
    global phonenumber
    global email
    
    global userid_entry
    global username_entry
    global phonenumber_entry
    global email_entry
    
    userid = StringVar()
    username = StringVar()
    phonenumber = StringVar()
    email = StringVar()
    
    Label(screen1, text = "Please Enter Details Below").pack()
    Label(screen1, text = "").pack()
    
    Label(screen1, text = "User ID").pack()
    userid_entry = Entry(screen1, textvariable = userid)
    userid_entry.pack()
    
    Label(screen1, text = "Username").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    
    Label(screen1, text = "Phone number").pack()
    phonenumber_entry = Entry(screen1, textvariable = phonenumber)
    phonenumber_entry.pack()
    
    
    Label(screen1, text = "Email").pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
   
   

    Label(screen1, text = "").pack()
    #Button(screen1,text = "Register" , width = 10 , height = 2 , command = register_user).pack()

    Button(screen1,text = "Scan Fingerprint & Register", height = "2", width= "30" , command = register_user).pack()
    Label(screen1, text = "").pack()
    Button(screen1,text = "Exit", height = "2", width= "30" , command = Exit).pack()

def login():
    global screen2
    screen2 = Toplevel (screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please Enter Details Below to Login").pack()
    Label(screen2, text = "").pack()
    
    global fingerid
    global sname
   
    
    global fingerid_entry
    global sname_entry
   
    
    fingerid = StringVar()
    sname = StringVar()
   
    
    
    Label(screen2, text = "Finger ID").pack()
    fingerid_entry = Entry(screen2, textvariable = fingerid)
    fingerid_entry.pack()
    
    Label(screen2, text = "Username").pack()
    sname_entry = Entry(screen2, textvariable = sname)
    sname_entry.pack()
    
    Label (screen2,text = "").pack()
    Button(screen2,text = "Scan Fingerprint Login", height = "2", width= "30" , command = login_verify).pack()
    Button(screen2,text = "Exit", height = "2", width= "30" , command = Exit).pack()

    
    
   
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome Home ")
    Label(text = "Smart Door Lock" , bg = "grey", width ="300",font=("Calibri" , 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width= "30" , command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width= "30" , command = register).pack()
    Label(text = "").pack()
    Button(text = "Exit", height = "2", width= "30" , command = Exit).pack()
    Label(text = "").pack()
    

    
    screen.mainloop()
    
main_screen()
    
    



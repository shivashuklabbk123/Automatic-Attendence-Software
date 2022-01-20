from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import face_recognition
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x800+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        #===First Image===========>

        img_top =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\helpbg.jpeg")
        img_top=img_top.resize((1520,745),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1520,height=745)

        bg_img=Label(f_lbl,text="Email:shivashukla847@gmail.com",font=("times new roman",30,"bold"),fg="blue")
        bg_img.place(x=440,y=260)


        img1_top =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\shiva1.jpeg")
        img1_top=img1_top.resize((100,130),Image.ANTIALIAS)
        self.photoimg1_top=ImageTk.PhotoImage(img1_top)

        f_lbl=Label(f_lbl,image=self.photoimg1_top)
        f_lbl.place(x=275,y=375,width=100,height=130)











if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()        

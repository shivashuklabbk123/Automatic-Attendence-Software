from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("740x630+380+30")
        self.root.wm_iconbitmap("face.ico")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open('chat.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=740,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=740)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>>",command=self.send,font=('arial',16,'bold'),width=7,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',16,'bold'),width=8,bg='red',fg='blue')
        self.clare.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

    #====================Function Declaration===================
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')






    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send) 
        self.text.yview(END)  

        if (self.entry.get()==''):
            self.msg='Please enter some input' 
            self.label_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')  

        if(self.entry.get()=='hello chatbot'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif(self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: fine and you!!')


        elif(self.entry.get()=='i am also fine'):
            self.text.insert(END,'\n\n'+'Bot: Good')

        elif(self.entry.get()=='who created you'):
            self.text.insert(END,'\n\n'+'Bot: Mr. Shiva shiva created me')

        elif(self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr. Bot')

        elif(self.entry.get()=='what is my group no.'):
            self.text.insert(END,'\n\n'+'Bot: Your group number is G4')

        elif(self.entry.get()=='Who is team leader of my project'):
            self.text.insert(END,'\n\n'+'Bot: Your team leader is Mr. Shiva shukla')

        elif(self.entry.get()=='How many team member of my project is'):
            self.text.insert(END,'\n\n'+'Bot: There are only 2 member')

        elif(self.entry.get()=='Tell me name of member'):
            self.text.insert(END,'\n\n'+'Bot: Shiva and Suryansh')

        elif(self.entry.get()=='what the status of my project'):
            self.text.insert(END,'\n\n'+'Bot: Your project is ready!!')

        elif(self.entry.get()=='what is my college name'):
            self.text.insert(END,'\n\n'+'Bot: You college name is Raj Kumar Goel Institute of Technology') 

        elif(self.entry.get()=='what is face recognition attendence software'):
            self.text.insert(END,'\n\n'+'Bot: A facial recognition attendance system uses facial recognition technology to identify and verify a person using the person facial features and automatically mark attendance. The software can be used for different groups of people such as employees, students, etc. The system records and stores the data in real-time.')
                                                                                                                         

        elif(self.entry.get()=='what is opencv'):
            self.text.insert(END,'\n\n'+'Bot: OpenCV is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human')
        
        elif(self.entry.get()=='full form of LBPH'):
            self.text.insert(END,'\n\n'+'Bot: Local binary pattern histogram')

        elif(self.entry.get()=='what is LBPH'):
            self.text.insert(END,'\n\n'+'Bot: LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person. It is known for its performance and how it is able to recognize the face of a person from both front face and side face.')
    
        elif(self.entry.get()=='how many algorithm are used in my project'):
            self.text.insert(END,'\n\n'+'Bot: There are 2 algorithm are used 1.opencv, 2.Local binary pattern histogram')

        elif(self.entry.get()=='which algorithm my project work'):
            self.text.insert(END,'\n\n'+'Bot: Local binary pattern histogram and opencv') 

        elif(self.entry.get()=='how my project work'):
            self.text.insert(END,'\n\n'+'Bot: Your project work by recognizing the face and mark the attendence in excel sheet')       

        elif(self.entry.get()=='what is features of my project'):
            self.text.insert(END,'\n\n'+'Bot: Feature of your project is:- 1.Firstly you can register, 2.You can login if you forget password then you can reset your password,3.After login you will reach the home page of software,3.you can add the all detail of student,4.You can take photosample and then,5.You can train the data,6.You can see your images by clicking on photo tab,7.You can detect your face by clicking on face detector tab and it mark the attendence automatically by recognizing the face, 8.You can see your attendence on attendence tab, 9.You can also import and export the csv file of attendence, 10.You can take help by clicking on help desk tab if you have any issue, 11.You can also chat with chatBot ask any question, 12.At the last you can exit from the software by clicking on exit tab!!!',)  

        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thanks for chatting me')  
        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry I didn`t get it')                                       







if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()


    
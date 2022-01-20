from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x800+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")

        #=======================Variables======================
        self.var_dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_scholar=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_mentor=StringVar()



        # FIRST image

        img =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\face-recognition.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        # second image

        img1 =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # third image

        img2 =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\student_detail.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3 =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\wp2551980.jpg")
        img3=img3.resize((1520,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1520,height=700)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=650)

        #Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left=Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\university.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
          

        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #Current Course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=130,width=720,height=140)

        #Department
        dep_label=Label(current_course_frame,text="Department", font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=7,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","EEE","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course", font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=7,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","B.Tech","M.Tech","BBA","MBA","B.Pharam","M.Pharma")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year", font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=7,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=7,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester", font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=7,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=7,sticky=W)


        #Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #studentId

        studentId_label=Label(class_student_frame,text="StudentId:", font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student Name

        studentName_label=Label(class_student_frame,text="Name:", font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student Roll Number

        roll_label=Label(class_student_frame,text="Roll Number:", font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #student Gender

        gender_label=Label(class_student_frame,text="Gender:", font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=17)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        #student DOB

        dob_label=Label(class_student_frame,text="DOB:", font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #student Email Id

        email_label=Label(class_student_frame,text="Email_id:", font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #student Phone Number

        phone_label=Label(class_student_frame,text="Phone No:", font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #student Address

        address_label=Label(class_student_frame,text="Address:", font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #student Mentor Name

        menter_label=Label(class_student_frame,text="Mentor Name:", font=("times new roman",13,"bold"),bg="white")
        menter_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        menter_entry=Entry(class_student_frame,textvariable=self.var_mentor,width=20,font=("times new roman",13,"bold"))
        menter_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #student scholar/DaysScholar

        scholar_label=Label(class_student_frame,text="Scholar/DaysScholar:", font=("times new roman",13,"bold"),bg="white")
        scholar_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        scholar_entry=Entry(class_student_frame,textvariable=self.var_scholar,width=20,font=("times new roman",13,"bold"))
        scholar_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=710,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=710,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=680,height=580)

        img_right =Image.open(r"C:\Users\HP\Documents\Face Recognition System\college_images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #=================Searching System==================================================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=665,height=70)

        Search_label=Label(Search_frame,text="Search By:", font=("times new roman",13,"bold"),bg="red")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll_NO.","Phone_No.","3rd","4th","5th","6th","7th","8th")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        Search_entry=Entry(Search_frame,width=17,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        #=================Table Frame=======================================================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=665,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","Year","Sem","id","name","roll","scholar","gender","dob","email","phone","address","mentor"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("scholar",text="Scholar/DaysScholar")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email_id")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mentor",text="Mentor Name")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("scholar",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("mentor",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_curser)
        self.fetch_data()

    #==========================Function Declaration=====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password="Shiva@123",database="myproject")
                my_curser=conn.cursor()
                my_curser.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_Sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_scholar.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_mentor.get(),
                                                                                            self.var_radio1.get()


                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added Successfully",parent="self.root") 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
    #===================================Fetch Data================================================
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password="Shiva@123",database="myproject")
        my_curser=conn.cursor()
        my_curser.execute("select * from student")
        data =my_curser.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    #======================================get curser=================================================
    def get_curser(self,event=""):
        curser_focus=self.student_table.focus()
        content=self.student_table.item(curser_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_scholar.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_mentor.set(data[13]),
        self.var_radio1.set(data[14])
    #=======================update function=============== 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password="Shiva@123",database="myproject")
                    my_curser=conn.cursor()   
                    my_curser.execute("update student set dep=%s,Course=%s,Year=%s,Sem=%s,name=%s,roll=%s,scholar=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,mentor=%s,PhotoSample=%s where id = %s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_Course.get(),
                                                                                                                                                                                self.var_Year.get(),
                                                                                                                                                                                
                                                                                                                                                                                self.var_Sem.get(),
                                                                                                                                                                                
                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_scholar.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_id.get()


                                                                                                                                                                            ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student detail successfully completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()


            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
#====================Delete Function ==============================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password="Shiva@123",database="myproject")
                    my_curser=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_curser.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
    #=====================Reset========================================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_scholar.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_mentor.set("")
        self.var_radio1.set("")
    #=========================Generate data or take photo sample=====================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password="Shiva@123",database="myproject")
                my_curser=conn.cursor()
                my_curser.execute("select * from student")
                myresult=my_curser.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_curser.execute("update student set dep=%s,Course=%s,Year=%s,Sem=%s,name=%s,roll=%s,scholar=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,mentor=%s,PhotoSample=%s where id = %s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_Course.get(),
                                                                                                                                                                                self.var_Year.get(),
                                                                                                                                                                                
                                                                                                                                                                                self.var_Sem.get(),
                                                                                                                                                                                
                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_scholar.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_id.get()==id+1


                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #================Load predefine data on face frontals from opencv========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3                                                                                                                                                                
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)      



        








        

        


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
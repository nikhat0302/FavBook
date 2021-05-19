#--------------------Modules-------------------
from tkinter import*
# from PIL import ImageTk
from tkinter import messagebox
from tkinter.filedialog import*
import os
import random
import datetime
import pyttsx3
import mysql.connector
import webbrowser
import wikipedia

conn=mysql.connector.connect(host="localhost",user="root",password="password123",database="mydb")
mycursor=conn.cursor()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate', 125)

class FavBook:
    def __init__(self,root):
        self.root=root
        self.root.title("My FavBook")
        self.root.geometry("1540x1000+0+0")

        #--------------------Images-------------------
        
        self.logo_icon=PhotoImage(file="images/logo.png")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/password.png")
        #self.cal_icon=PhotoImage(file="timetable.png")
        self.chitchat_icon=PhotoImage(file="gallery/chitchat.png")
        self.car_icon=PhotoImage(file="gallery/car_game.png")
        self.space_icon=PhotoImage(file="gallery/space_game.png")

        #--------------------background-------------------
        #bg_label=Label(self.root,bg="dodgerblue3").place(x=40,y=20,width=800,height=900)
        def intro():
            engine.say("Welcome to my favbook ,   ,      , Pleaselogin to enter in the world of favbook which offers you a lot of options for example you can write your own sticky notes, read books and store a book collection and also can listen it alongwith games , reminder , calculator and a chitchat window , , cum text assistant, , which can serve anything according to you ")
            engine.runAndWait()

        #--------------------Title-------------------
        title=Button(self.root,text="My FavBook",font=("mistral", 30, "bold"),fg="old lace",bg="dodgerblue3",bd=4,relief=RIDGE,command=intro)
        title.place(x=0,y=0,relwidth=1)

        #---------------------frame2-----------------
        frame2=Frame(self.root,bg="white")
        frame2.place(x=550,y=100,width=500,height=650)

        #--------------------label-------------------
        logo_label=Label(frame2,image=self.logo_icon,bg="white")
        logo_label.grid(row=0,column=0,columnspan=2,ipady=10)
        user_label=Label(frame2,text="Username",image=self.user_icon,font=("times new roman", 18, "bold"),compound=LEFT)
        user_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        user_dob=Label(frame2,text="Dob",image=self.user_icon,font=("times new roman", 18, "bold"),compound=LEFT)
        user_dob.grid(row=2,column=0,padx=10,pady=10,sticky="w")   
        secure_label=Label(frame2,text="Click Here to Answer a Security Question!",font=("times new roman",16, "bold"))
        secure_label.grid(row=4,column=0,columnspan=2) 
        pass_label=Label(frame2,text="Password",font=("times new roman", 18, "bold"),image=self.pass_icon,compound=LEFT)
        pass_label.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        

         #--------------------dropdown-------------------
        def test_opt():
            getopt=selopt.get()
            if getopt==1:
                if scr.get()=="automation of boring stuff":
                    return True
            elif getopt==2:
                if scr.get()=="21":
                    return True
            elif getopt==3:
                if scr.get()=="3":
                    return True
            else:
                return False

        menubtn=Menubutton(frame2,text="Security Questions",font=("times new roman",15))
        menus=Menu(menubtn)
        menubtn.config(menu=menus)
        selopt=IntVar() 
        menus.add_radiobutton(label="What's your favourite book?",variable=selopt,command=test_opt,value=1)
        menus.add_radiobutton(label="What's your age?",variable=selopt,command=test_opt,value=2)
        menus.add_radiobutton(label="What's your favourite number?",variable=selopt,command=test_opt,value=3)
        menubtn.grid(row=5,column=0,columnspan=2)

        #-------------------security question-------------------
        scr=StringVar()
        scrques_entry=Entry(frame2,textvariable=scr,font=("times new roman",20)).grid(row=7,column=0,columnspan=2)

        #--------------------entry-------------------
        user_val=StringVar()
        pass_val=StringVar()
        dob_val=StringVar()
        showpass=StringVar()
        user_entry=Entry(frame2,font=("times new roman",20),bd=4,relief=RIDGE,textvariable=user_val).grid(row=1,column=1)
        dob_entry=Entry(frame2,font=("times new roman",20),bd=4,relief=RIDGE,textvariable=dob_val).grid(row=2,column=1)
        showpas=Label(frame2,font=("times new roman",20),textvariable=showpass,bd=4,relief=RIDGE).grid(row=3,column=1,ipadx=100)

         #--------------------show password-------------------
        def showpassword():
            option=test_opt()
            if (user_val.get()=="nikhat" and dob_val.get()=="03-02-1999" and option==True): 
                 showpass.set("pass123")
            else:
                messagebox.showerror("Error", "Unauthorized Approach!")

        def swap(frame):
            frame.tkraise()

        #--------------------button-------------------
        resetbtn=Button(frame2,text="Show Password",command=showpassword,font=("times new roman",18,"bold"),bd=5,bg="dodgerblue3",fg="old lace")
        resetbtn.grid(row=8,column=0,padx=10,pady=10)
        loginbtn=Button(frame2,text="Login",command=lambda: swap(frame1),font=("times new roman",18,"bold"),bd=5,bg="dodgerblue3",fg="old lace")
        loginbtn.grid(row=8,column=1,ipadx=40,pady=10)

        #--------------------frame1-------------------
        #bg_label=Label(self.root,bg="dodgerblue3").pack(fill=BOTH)
        frame1=Frame(self.root,bg="white")
        frame1.place(x=550,y=100,width=500,height=650)

        #--------------------label-------------------
        logo_label=Label(frame1,image=self.logo_icon,bg="white")
        logo_label.grid(row=0,column=0,columnspan=2,ipady=10)
        user_label=Label(frame1,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman", 20, "bold"))
        user_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        pass_label=Label(frame1,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman", 20, "bold"))
        pass_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")    

        #--------------------entry-------------------
        userlog_val=StringVar()
        passlog_val=StringVar()
        user_entry=Entry(frame1,font=("times new roman",20),bd=4,relief=RIDGE,textvariable=userlog_val).grid(row=1,column=1,padx=0)
        pass_entry=Entry(frame1,font=("times new roman",20),bd=4,relief=RIDGE,show="*",textvariable=passlog_val).grid(row=2,column=1)

         #--------------------user_login command-------------------
        def user_login():
            name=userlog_val.get()
            wrd=passlog_val.get()
            if name=="a" and wrd=="a":
                messagebox.showinfo("Info", "Login Successfully!")

                #-----------------frame3---------------
                frame3=Frame(self.root)
                frame3.place(x=0,y=0,width=1700,height=1000)

                #----------------------notes command-----------------
                def notes():
                    mycolor=["floral white", "linen", "alice blue", "pale green", "light yellow", "snow2", "honeydew2", "ivory2", "thistle1"]
                    color=random.choice(mycolor)
                    font_family=["arial", "blackadder itc", "chiller", "mistral"]
                    myfont=random.choice(font_family)
                    frame4=Frame(self.root,bg=color)
                    frame4.place(x=0,y=0,width=1000,height=1000)
                    

                    #----------------date & time--------------
                    datetime_var=datetime.datetime.now()
                    dtm=datetime_var.strftime("%Y-%m-%d %H:%M:%S")

                    #--------------------notes menu functions------------------
                    def save_note():
                        global file
                        file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documensts", "*.txt")])
                        if file=="":
                            file=None
                        else:
                            f=open(file,"w")
                            f.write(txtar.get(1.0,END))
                            f.close()

                    def open_note():
                        global file
                        file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documensts", "*.txt")])
                        if file=="":
                            file=None
                        else:
                            txtar.delete(1.0,END)
                            f=open(file,"r")
                            txtar.insert(1.0,f.read())
                            f.close()

                    def pyspeak():
                        speak_var=txtar.get(1.0,END)
                        rate=engine.getProperty('rate')
                        engine.setProperty('rate', 125)
                        engine.say(speak_var)
                        engine.runAndWait()
                        
                    def exit_notes():
                        frame3.tkraise()

                    #--------------------notes menu------------------
                    time_menubtn=Menubutton(frame4,text=dtm,font=20,bg=color,fg="black")
                    menu1=Menu(time_menubtn)
                    time_menubtn.config(menu=menu1)
                    menu1.add_command(label="Save",command=save_note,font=("times new roman", 10))
                    menu1.add_command(label="Open",command=open_note,font=("times new roman", 10))
                    menu1.add_command(label="Speak",command=pyspeak,font=("times new roman", 10))
                    menu1.add_separator()
                    menu1.add_command(label="Exit",command=exit_notes,font=("times new roman", 10))
                    time_menubtn.grid(row=0,column=0,pady=10)

                   #-----------------notes textarea-------------
                    txtar=Text(frame4,bg=color,font=40,fg="black")
                    file=None
                    txtar.grid(row=1,column=0,ipady=700)
                    
                    #----------------------books---------------------
                def books():
                    frame6=Frame(self.root,bg="white")
                    frame6.place(x=0,y=0,width=1000,height=1000)

                    #----------------date & time--------------
                    datetime_var1=datetime.datetime.now()
                    dtm1=datetime_var1.strftime("%Y-%m-%d %H:%M:%S")

                    #----------------functions-----------------
                    def open_book():
                        top1=Toplevel()
                        
                        mycursor.execute("select book_no,name,topic,author,edition from book_store")
                        myresult=mycursor.fetchall()
                        lb=Listbox(top1)
                        for x in myresult:
                            for y in range(1):
                                lb.insert(y, x)
                        lb.grid(row=0,column=0,ipadx=100)

                        #---------------------increment important-----------------
                        def check():
                            test=testing.get()
                            if test==1:
                                mycursor.execute("select book from book_store where book_no=1")
                                myresult=mycursor.fetchall()
                                fill.set(myresult)
                                top1.destroy()

                            if test==2:
                                mycursor.execute("select book from book_store where book_no=2")
                                myresult=mycursor.fetchall()
                                fill.set(myresult)
                                top1.destroy()

                            if test==3:
                                mycursor.execute("select book from book_store where book_no=3")
                                myresult=mycursor.fetchall()
                                fill.set(myresult)
                                top1.destroy()

                            if test==4:
                                mycursor.execute("select book from book_store where book_no=4")
                                myresult=mycursor.fetchall()
                                fill.set(myresult)
                                top1.destroy()

                            if test==5:
                                mycursor.execute("select book from book_store where book_no=5")
                                myresult=mycursor.fetchall()
                                fill.set(myresult)
                                top1.destroy()

                        Label(top1,text="Book Number",font="arial 10 bold").grid(row=1,column=0)
                        testing=IntVar()
                        Entry(top1,textvariable=testing,font="arial 10 bold").grid(row=2,column=0)
                        Button(top1,text="Open",font="mistral 15 bold",command=check).grid(row=3,column=0)

                    #------------------------add book----------------
                    def add_book():
                        top2=Frame()
                        top2.place(x=80,y=50)
                        Label(top2,text="Add New Book",font="mistral 20 bold").grid(row=0,column=0,columnspan=2)
                        Label(top2,text="Name",font="arial 10 bold").grid(row=1,column=0)
                        Label(top2,text="Topic",font="arial 10 bold").grid(row=2,column=0)
                        Label(top2,text="Author",font="arial 10 bold").grid(row=3,column=0)
                        Label(top2,text="Edition",font="arial 10 bold").grid(row=4,column=0)

                        def upload():
                            global file1
                            file1=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documensts", "*.txt")])
                            if file1=="":
                                file1=None
                            else:
                                txtar1.delete(1.0,END)
                                f=open(file1,"r")
                                txtar1.insert(1.0,f.read())
                                f.close()

                        Button(top2,text="Upload",font="arial 10 bold",command=upload).grid(row=5,column=0)

                        name1=StringVar()
                        topic1=StringVar()
                        author1=StringVar()
                        edition1=StringVar()

                        Entry(top2,font="arial 10 bold",textvariable=name1).grid(row=1,column=1)
                        Entry(top2,font="arial 10 bold",textvariable=topic1).grid(row=2,column=1)
                        Entry(top2,font="arial 10 bold",textvariable=author1).grid(row=3,column=1)
                        Entry(top2,font="arial 10 bold",textvariable=edition1).grid(row=4,column=1)
                        txtar1=Text(top2,height=2,width=5)
                        file1=None
                        txtar1.grid(row=5,column=1)

                        def add_new():
                            name2=name1.get()
                            topic2=topic1.get()
                            author2=author1.get()
                            edition2=edition1.get()
                            upload1=txtar1.get(1.0,END)
                            top2.destroy()

                            if len(name2)==0 and len(topic2)==0 and len(author2)==0 and len(edition2)==0 and len(upload1)==0:
                                messagebox.showerror("Error","All fiels are required \n Operation Unsuccessful")
                            else:
                                sql="insert into book_store (name,topic,author,edition,book) values (%s,%s,%s,%s,%s)"
                                val=name2, topic2, author2, edition2, upload1
                                mycursor.execute(sql,val)
                                conn.commit()

                        Button(top2,text="Add New Book",font="arial 10 bold",command=add_new).grid(row=6,column=1,columnspan=2)

                    def delete_book():
                        top3=Toplevel()
                        
                        mycursor.execute("select book_no,name,topic,author,edition from book_store")
                        myresult=mycursor.fetchall()
                        lb2=Listbox(top3)
                        for x in myresult:
                            for y in range(1):
                                lb2.insert(y, x)
                        lb2.grid(row=0,column=0,ipadx=100)

                        def delete():
                            del_book=testing1.get()
                            if del_book==1:
                                mycursor.execute("delete from book_store where book_no=1")
                                conn.commit()

                            if del_book==2:
                                mycursor.execute("delete from book_store where book_no=2")
                                conn.commit()

                            if del_book==3:
                                mycursor.execute("delete from book_store where book_no=3")
                                conn.commit()

                            if del_book==4:
                                mycursor.execute("delete from book_store where book_no=4")
                                conn.commit()

                            if del_book==5:
                                mycursor.execute("delete from book_store where book_no=5")
                                conn.commit()

                        Label(top3,text="Book Number",font="arial 10 bold").grid(row=1,column=0)
                        testing1=IntVar()
                        Entry(top3,textvariable=testing1,font="arial 10 bold").grid(row=2,column=0)
                        Button(top3,text="Delete",font="mistral 15 bold",command=delete).grid(row=3,column=0)

                    #----------------------------speak book------------------
                    def read_book():
                        speak_var=testing.get()
                        rate=engine.getProperty('rate')
                        engine.setProperty('rate', 125)
                        engine.say(speak_var)
                        engine.runAndWait()

                    def exit_book():
                        frame3.tkraise()

                    time_menubtn1=Menubutton(frame6,text=dtm1,font=20,bg="white",fg="black")
                    menu4=Menu(time_menubtn1)
                    time_menubtn1.config(menu=menu4)
                    menu4.add_command(label="Open",command=open_book,font=("times new roman", 10))
                    menu4.add_command(label="Add New",command=add_book,font=("times new roman", 10))
                    menu4.add_command(label="Delete",command=delete_book,font=("times new roman", 10))
                    menu4.add_command(label="Speak",command=read_book,font=("times new roman", 10))

                    menu4.add_separator()
                    menu4.add_command(label="Exit",command=exit_book,font=("times new roman", 10))
                    time_menubtn1.grid(row=0,column=0,pady=10)

                    fill=StringVar()
                    Label(frame6,textvariable=fill,font="arial 15").grid(row=1,column=0)

                #---------------------reminder call-------------------
                def reminder_call():
                    os.system('python reminder.py')


                #------------------calculator-----------------------
                def calculator_call():
                    os.system('python calculator.py')

                #------------------game-----------------------
                def gamer_call():
                    frame8=Frame(self.root)
                    frame8.place(x=0,y=0,width=1600,height=1000)

                    #----------------------space invader--------------------
                    def space_invader():
                        os.system('python space_invader.py')

                    def car_racing():
                        os.system('python car_racing.py')

                    #-------------------------game option---------------------
                    Button(frame8,image=self.space_icon,command=space_invader).grid(row=0,column=0,pady=5)  
                    Button(frame8,image=self.car_icon,command=car_racing).grid(row=0,column=1,pady=5) 
                #----------------------chitchat---------------------
                """
                CHITCHAT WINDOW
                """
                def chitchat():
                    chitchat_frame=Frame(self.root,bg="deepskyblue3")
                    chitchat_frame.place(x=1300,y=0,width=500,height=1000)

                    def mainframe():
                        query=chitchat_var.get().lower()
                        txtarea.delete(1.0,END)

                        if "wikipedia" in query:
                            result=wikipedia.summary(query, sentences=2)
                            txtarea.insert(1.0,result)
                            return result 
                        
                        elif "google" in query:
                            webbrowser.open("www.google.com")

                        elif "youtube" in query:
                            webbrowser.open("www.youtube.com")

                        elif "open code" in query:
                            result=r"C:\Users\Nikhat Parween\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                            os.startfile(result)

                        elif "open c++ library" in query:
                            result=r"C:\Users\Nikhat Parween\Desktop\library"
                            os.startfile(result)

                        #snake game creates problem

                        #-------------------music list-----------------
                        elif "play song online" in query:
                            webbrowser.open("www.gaana.com")
                        elif "play music online" in query:
                            webbrowser.open("www.gaana.com")
                        
                        elif "play song" in query:
                            result=f"C:\\Users\\Nikhat Parween\\Music\\tune1.mp3"
                            os.startfile(result)
                        elif "play music" in query:
                            result=f"C:\\Users\\Nikhat Parween\\Music\\tune1.mp3"
                            os.startfile(result)

                        #-----------------pictures------------------
                        elif "open pic"in query:
                            result=r"C:\Users\Nikhat Parween\Pictures"
                            os.startfile(result)
                        elif "open photo"in query:
                            result=r"C:\Users\Nikhat Parween\Pictures"
                            os.startfile(result)

                        #---------------------whatsapp-------------------
                        elif "open whatsapp" in query:
                            result=r"C:\ProgramData\Nikhat Parween\WhatsApp\WhatsApp.exe"
                            os.startfile(result)
                        elif "send whatsapp msg to me" in query:
                            result=r"C:\ProgramData\Nikhat Parween\WhatsApp\WhatsApp.exe"
                            os.startfile(result)
                            os.system('python automate.py')

                        #------------------------------eva-------------------
                        elif "your intro" in query:
                            result="Hi, I am Eva. How are you?"
                            txtarea.insert(1.0,result)
                            return result 
                        elif "who are you" in query:
                            result="Hi, I am Eva. How are you?"
                            txtarea.insert(1.0,result)
                            return result 

                        elif "how are you" in query:
                            result="I am fine. Thankyou \nHow may I help you?"
                            txtarea.insert(1.0,result)
                            return result 

                        else:
                            result="Sorry!, I can't understand your command. \nPlease try again!"
                            txtarea.delete(1.0,END) 
                            txtarea.insert(1.0,result)
                            return result 

                    def speak():
                        audio=mainframe()
                        engine.say(audio)
                        engine.runAndWait()                   

                    chitchat_var=StringVar()
                    Label(chitchat_frame,image=self.chitchat_icon,bg="deepskyblue3").grid(row=0,column=0,pady=20)
                    lbl1=Label(chitchat_frame,text="Ask Me Anything!",font="mistral 20 bold",bg="deepskyblue3")
                    lbl1.grid(row=1,column=0,padx=5)
                    Entry(chitchat_frame,textvariable=chitchat_var,font="mistral 20 bold",bg="deepskyblue3").grid(row=2,column=0,pady=5)
                    Button(chitchat_frame,text="Let's Go!",font="mistral 20 bold",bg="deepskyblue3",command=mainframe).grid(row=3,column=0,pady=5)
                    Button(chitchat_frame,text="speak",command=speak,font="mistral 20 bold",bg="deepskyblue3").grid(row=4,column=0,pady=5)
                    txtarea=Text(chitchat_frame,font="mistral 20 bold",width=13,height=10,bg="deepskyblue3")
                    txtarea.grid(row=5,column=0,pady=5)

                    #----------------------chitchat---------------------
                    """
                    CHITCHAT WINDOW
                    """
                   
                    
                #----------------------buttons---------------------
                notesbtn=Button(frame3,text="Sticky Notes",font=("mistral",40,"bold"),bg="deepskyblue2",fg="white",command=notes)
                notesbtn.grid(row=0,column=0,ipady=430)
                booksbtn=Button(frame3,text="Book Store",font=("mistral",40,"bold"),bg="deepskyblue3",fg="white",command=books)
                booksbtn.grid(row=0,column=1,ipadx=15,ipady=430)
                gamebtn=Button(frame3,text="Game World",font=("mistral",40,"bold"),bg="deepskyblue2",fg="white",command=gamer_call)
                gamebtn.grid(row=0,column=2,ipadx=15,ipady=430)
                reminderbtn=Button(frame3,text="Remind Me",font=("mistral",40,"bold"),bg="deepskyblue3",fg="white",command=reminder_call)
                reminderbtn.grid(row=0,column=3,ipadx=15,ipady=430)
                calbtn=Button(frame3,text="Calculator",font=("mistral",40,"bold"),bg="deepskyblue2",fg="white",command=calculator_call)
                calbtn.grid(row=0,column=4,ipadx=15,ipady=430)
                chatbtn=Button(frame3,text="ChitChat \n  Window",font=("mistral",40,"bold"),bg="deepskyblue3",fg="white",command=chitchat)
                chatbtn.grid(row=0,column=5,ipadx=10,ipady=400)
            else:
                messagebox.showwarning("Warning", "Password is Wrong!")

        
        #--------------------button-------------------
        log_btn=Button(frame1,text="Login",command=user_login,font=("times new roman",18,"bold"),bd=5,bg="dodgerblue3",fg="old lace")
        log_btn.grid(row=3,column=1,columnspan=2,ipadx=40)
        res_btn=Button(frame1,text="Show Password",command=lambda: swap(frame2),font=("times new roman",18,"bold"),bd=5,bg="dodgerblue3",fg="old lace")
        res_btn.grid(row=6,column=0,columnspan=2,ipadx=50)
        

         #--------------------ask for reset-------------------
        reg_label1=Label(frame1,text="Forget Password?",font=("times new roman", 15,"bold"),fg="red")
        reg_label1.grid(row=4,column=0,columnspan=2)
        reg_label2=Label(frame1,text="See Password Here!",font=("times new roman", 15, "bold"),fg="red")
        reg_label2.grid(row=5,column=0,columnspan=2)

        
root=Tk()
obj=FavBook(root)
root.mainloop()

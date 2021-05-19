from tkinter import*
from PIL import ImageTk
import datetime,time,math
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import mysql.connector
import pygame
from pygame import mixer

pygame.init()

conn=mysql.connector.connect(host="localhost",user="root",password="password123",database="mydb")
mycursor=conn.cursor()

class remindme:
    def __init__(self, rem):
        self.rem=rem
        self.rem.geometry("400x400+450+100")
        self.rem.resizable(0,0)
        self.rem.title("RemindMe")

       #-----------------image----------------
        self.bg_icon=ImageTk.PhotoImage(file="images/grass.jpeg")
        grasslb=Label(rem,image=self.bg_icon)
        grasslb.place(x=0,y=0,height=400,width=400)

        #------------------button's functionality------------------
        def alarm():
            pass
        
            

        def reminder():
            #-----------------frame1--------------
            frame1=Frame(rem)
            frame1.place(x=0,y=0,width=400,height=400)

####################################################################################################################################
            def birthday():
                frame2=Frame(rem,bg="light pink")
                frame2.place(x=0,y=0,width=400,height=400)

                birthlb=Label(frame2,text="Birthday Reminder",font="mistral 30 bold",bg="light pink")
                birthlb.grid(row=0,column=0,columnspan=2,padx=10)

                bname=Label(frame2,text="Birthday    Name",font="arial 12 bold",bg="light pink")
                bname.grid(row=1,column=0,pady=10)
                name=StringVar()
                bename=Entry(frame2,font="arial 12 bold",width=10,bg="light pink",textvariable=name)
                bename.grid(row=1,column=1,pady=10)

                des=Label(frame2,text="Birthday's Description",font="arial 12 bold",bg="light pink")
                des.grid(row=2,column=0,pady=10)
                descrip=Text(frame2,font="arial 12 bold",height=4,width=10,bg="light pink")
                descrip.grid(row=2,column=1,pady=10)

                datelb=Label(frame2,text="Select your Date",font="arial 12 bold",bg="light pink")
                datelb.grid(row=3,column=0,pady=10)
                getdate=StringVar()
                date1=DateEntry(frame2,textvariable=getdate,bg="light pink").grid(row=3,column=1)

                tune=Label(frame2,text="Select your Tune",font="arial 12 bold",bg="light pink")
                tune.grid(row=4,column=0,pady=10)

                #--------------------tune-----------------------
                menubtn=Menubutton(frame2,text="Select",font="arial 12 bold")
                menu1=Menu(menubtn,tearoff=0)
                menubtn.config(menu=menu1)

                def tuning():
                    get_tune=var.get()
                    if get_tune==1:
                       mixer.music.load("gallery/tune1.mp3")
                       mixer.music.play() 
                    if get_tune==2:
                       mixer.music.load("gallery/tune2.mp3")
                       mixer.music.play() 

                var=IntVar()
                menu1.add_radiobutton(label="Tune1",font=("times new roman", 10),variable=var,value=1,command=tuning)
                menu1.add_radiobutton(label="Tune2",font=("times new roman", 10),variable=var,value=2,command=tuning)
                menubtn.grid(row=4,column=1)
                select_tune=StringVar()

                #-------------------set reminder-----------------
                def set_reminder():
                    #---------------------------
                    desc=descrip.get(1.0,END)
                    nameget=name.get()
                    getdate1=getdate.get()
                    get_tune=select_tune.get()
                    if len(desc)==0 and len(nameget)==0 and len(getdate1)==0:
                        messagebox.showerror("Error", "All fiels are required!")
                    else:
                        for x in range(1):
                            sql="insert into reminder (title, name, description, date) values (%s, %s, %s, %s)"
                            val=("birthday", nameget, desc, getdate1, get_tune)
                            mycursor.execute(sql,val)
                            conn.commit()

                    datetime_var1=datetime.datetime.now()
                    dtm1=datetime_var1.strftime("%d / %m / %y")
                    dtm2=datetime_var1.strftime("%H:%M")
                    
                    if dtm1==getdate1:#---------------------clock code & no blank----------------
                        messagebox.showinfo("Birthday","Today is " + nameget + "'s Birthday")
                        if get_tune==1:
                            mixer.music.load("gallery/tune1.mp3")
                            mixer.music.play(2)
                        if get_tune==2:
                            mixer.music.load("gallery/tune2.mp3")
                            mixer.music.play(2)

                def exit():
                    frame1.tkraise()

                setbtn1=Button(frame2,text="Set",font="mistral 20 bold",command=set_reminder,bg="light pink").grid(row=6,column=0)
                exitbtn=Button(frame2,text="Exit",font="mistral 20 bold",command=exit,bg="light pink").grid(row=6,column=1)

####################################################################################################################################

####################################################################################################################################
            def anniversary():
                frame3=Frame(rem,bg="light blue")
                frame3.place(x=0,y=0,width=400,height=400)

                birthlb=Label(frame3,text="Anniversary Reminder",font="mistral 30 bold",bg="light blue")
                birthlb.grid(row=0,column=0,columnspan=2,padx=10)

                bname=Label(frame3,text="Anniversary Couple",font="arial 12 bold",bg="light blue")
                bname.grid(row=1,column=0,pady=10)
                name=StringVar()
                bename=Entry(frame3,font="arial 12 bold",width=10,bg="light blue",textvariable=name)
                bename.grid(row=1,column=1,pady=10)

                des=Label(frame3,text="Anniversary's Description",font="arial 12 bold",bg="light blue")
                des.grid(row=2,column=0,pady=10)
                descrip=Text(frame3,font="arial 12 bold",height=4,width=10,bg="light blue")
                descrip.grid(row=2,column=1,pady=10)

                datelb=Label(frame3,text="Select your Date",font="arial 12 bold",bg="light blue")
                datelb.grid(row=3,column=0,pady=10)
                getdate=StringVar()
                date1=DateEntry(frame3,textvariable=getdate,bg="light blue").grid(row=3,column=1)

                tune=Label(frame3,text="Select your Tune",font="arial 12 bold",bg="light blue")
                tune.grid(row=4,column=0,pady=10)

                menubtn=Menubutton(frame3,text="Select",font="arial 12 bold")
                menu1=Menu(menubtn,tearoff=0)
                menubtn.config(menu=menu1)
                #--------------------tune------------------------
                def tuning():
                    get_tune=var.get()
                    if get_tune==1:
                       mixer.music.load("gallery/alarm_beep.wav")
                       mixer.music.play() 
                    if get_tune==2:
                       mixer.music.load("gallery/sunny_day.wav")
                       mixer.music.play() 

                var=IntVar()
                menu1.add_radiobutton(label="Tune1",font=("times new roman", 10),variable=var,value=1,command=tuning)
                menu1.add_radiobutton(label="Tune2",font=("times new roman", 10),variable=var,value=2,command=tuning)
                menubtn.grid(row=4,column=1)
                select_tune=StringVar()

                #-------------------set reminder-----------------
                def set_reminder1():
                    #---------------------------
                    desc=descrip.get(1.0,END)
                    nameget=name.get()
                    getdate1=getdate.get()
                    get_tune=select_tune.get()
                    if len(desc)==0 and len(nameget)==0 and len(getdate1)==0:
                        messagebox.showerror("Error", "All fiels are required!")
                    else:
                        for x in range(1):
                            sql="insert into reminder (title, name, description, date) values (%s, %s, %s, %s)"
                            val=("anniversary", nameget, desc, getdate1, get_tune)
                            mycursor.execute(sql,val)
                            conn.commit()

                    datetime_var1=datetime.datetime.now()
                    dtm1=datetime_var1.strftime("%d / %m / %y")
                    dtm2=datetime_var1.strftime("%H:%M")
                    
                    if dtm1==getdate1:#---------------------clock code & no blank----------------
                        messagebox.showinfo("Anniversary","Today is " + nameget + "'s Anniversary")
                        if get_tune==1:
                            mixer.music.load("gallery/alarm_beep.wav")
                            mixer.music.play(2)
                        if get_tune==2:
                            mixer.music.load("gallery/sunny_day.wav")
                            mixer.music.play(2)
                       

                def exit():
                    frame1.tkraise()

                setbtn1=Button(frame3,text="Set",font="mistral 20 bold",command=set_reminder1,bg="light blue").grid(row=5,column=0)
                exitbtn=Button(frame3,text="Exit",font="mistral 20 bold",command=exit,bg="light blue").grid(row=5,column=1)

####################################################################################################################################

####################################################################################################################################
            def mourning():
                frame4=Frame(rem,bg="light green")
                frame4.place(x=0,y=0,width=400,height=400)

                birthlb=Label(frame4,text="Mourning Reminder",font="mistral 30 bold",bg="light green")
                birthlb.grid(row=0,column=0,columnspan=2,padx=10)

                bname=Label(frame4,text="Mourning    ",font="arial 12 bold",bg="light green")
                bname.grid(row=1,column=0,pady=10)
                name=StringVar()
                bename=Entry(frame4,font="arial 12 bold",width=10,bg="light green",textvariable=name)
                bename.grid(row=1,column=1,pady=10)

                des=Label(frame4,text="Mourning's Description",font="arial 12 bold",bg="light green")
                des.grid(row=2,column=0,pady=10)
                descrip=Text(frame4,font="arial 12 bold",height=4,width=10,bg="light green")
                descrip.grid(row=2,column=1,pady=10)

                datelb=Label(frame4,text="Select your Date",font="arial 12 bold",bg="light green")
                datelb.grid(row=3,column=0,pady=10)
                getdate=StringVar()
                date1=DateEntry(frame4,textvariable=getdate,bg="light blue").grid(row=3,column=1)

                #-------------------set reminder-----------------
                def set_reminder2():
                    #---------------------------
                    desc=descrip.get(1.0,END)
                    nameget=name.get()
                    getdate1=getdate.get()
                    if len(desc)==0 and len(nameget)==0 and len(getdate1)==0:
                        messagebox.showerror("Error", "All fiels are required!")
                    else:
                        sql="insert into reminder (title, name, description, date, tune) values (%s, %s, %s, %s, %s)"
                        val=("mourning", nameget, desc, getdate1, "tune1")
                        mycursor.execute(sql,val)
                        conn.commit()

                    datetime_var1=datetime.datetime.now()
                    dtm1=datetime_var1.strftime("%d / %m / %y")
                    dtm2=datetime_var1.strftime("%H:%M")
                    print(dtm2)
                    var=getdate.get()
                    
                    if dtm1==getdate1:#---------------------clock code & no blank----------------
                        #---------------play tune------------
                        messagebox.showinfo("RIP","Mourn Day")

                def exit():
                    frame1.tkraise()

                setbtn1=Button(frame4,text="Set",font="mistral 20 bold",command=set_reminder2,bg="light green").grid(row=5,column=0)
                exitbtn=Button(frame4,text="Exit",font="mistral 20 bold",command=exit,bg="light green").grid(row=5,column=1)

####################################################################################################################################


####################################################################################################################################
            def other():
                frame5=Frame(rem,bg="light pink")
                frame5.place(x=0,y=0,width=400,height=400)

                birthlb=Label(frame5,text="Reminder",font="mistral 30 bold",bg="light pink")
                birthlb.grid(row=0,column=0,columnspan=2,padx=10)

                bname=Label(frame5,text="Title",font="arial 12 bold",bg="light pink")
                bname.grid(row=1,column=0,pady=10)
                name=StringVar()
                bename=Entry(frame5,font="arial 12 bold",width=10,bg="light pink",textvariable=name)
                bename.grid(row=1,column=1,pady=10)

                des=Label(frame5,text="Description",font="arial 12 bold",bg="light pink")
                des.grid(row=2,column=0,pady=10)
                descrip=Text(frame5,font="arial 12 bold",height=4,width=10,bg="light pink")
                descrip.grid(row=2,column=1,pady=10)

                datelb=Label(frame5,text="Select your Date",font="arial 12 bold",bg="light pink")
                datelb.grid(row=3,column=0,pady=10)
                getdate=StringVar()
                date1=DateEntry(frame5,textvariable=getdate,bg="light pink").grid(row=3,column=1)

                tune=Label(frame5,text="Select your Tune",font="arial 12 bold",bg="light pink")
                tune.grid(row=4,column=0,pady=10)
                 #-------------------set reminder-----------------
                menubtn=Menubutton(frame5,text="Select",font="arial 12 bold")
                menu1=Menu(menubtn,tearoff=0)
                menubtn.config(menu=menu1)
                #--------------------tune------------------------
                def tuning():
                    get_tune=var.get()
                    if get_tune==1:
                       mixer.music.load("gallery/alarm_beep.wav")
                       mixer.music.play() 
                    if get_tune==2:
                       mixer.music.load("gallery/sunny_day.wav")
                       mixer.music.play() 

                var=IntVar()
                menu1.add_radiobutton(label="Tune1",font=("times new roman", 10),variable=var,value=1,command=tuning)
                menu1.add_radiobutton(label="Tune2",font=("times new roman", 10),variable=var,value=2,command=tuning)
                menubtn.grid(row=4,column=1)
                select_tune=StringVar()

                #-------------------set reminder-----------------
                def set_reminder3():
                    #---------------------------
                    desc=descrip.get(1.0,END)
                    nameget=name.get()
                    getdate1=getdate.get()
                    get_tune=select_tune.get()
                    if len(desc)==0 and len(nameget)==0 and len(getdate1)==0:
                        messagebox.showerror("Error", "All fiels are required!")
                    else:
                        for x in range(1):
                            sql="insert into reminder (title, name, description, date) values (%s, %s, %s, %s)"
                            val=("anniversary", nameget, desc, getdate1, get_tune)
                            mycursor.execute(sql,val)
                            conn.commit()

                    datetime_var1=datetime.datetime.now()
                    dtm1=datetime_var1.strftime("%d / %m / %y")
                    dtm2=datetime_var1.strftime("%H:%M")
                    
                    if dtm1==getdate1:#---------------------clock code & no blank----------------
                        messagebox.showinfo("Other","It's a Special Day for " + nameget)
                        if get_tune==1:
                            mixer.music.load("gallery/alarm_beep.wav")
                            mixer.music.play(2)
                        if get_tune==2:
                            mixer.music.load("gallery/sunny_day.wav")
                            mixer.music.play(2)
                        

                def exit():
                    frame1.tkraise()

                setbtn1=Button(frame5,text="Set",font="mistral 20 bold",command=set_reminder3,bg="light pink").grid(row=5,column=0)
                exitbtn=Button(frame5,text="Exit",font="mistral 20 bold",command=exit,bg="light pink").grid(row=5,column=1)

####################################################################################################################################

            def rem_list():
                frame6=Frame(rem,bg="light green")
                frame6.place(x=0,y=0,width=400,height=400)
                lb=Listbox(frame6,bg="light green",width=50,height=9,font=8)
                mycursor.execute("select* from reminder")
                myresult=mycursor.fetchall()
                for x in myresult:
                    for y in range(1):
                        lb.insert(y, x)
                lb.grid(row=0,column=0,ipadx=10)

                def delete_reminder():
                    list_selection=listentry1.get()
                    if list_selection=="1":
                        mycursor.execute("delete from reminder where id=1")
                        conn.commit()
                    if list_selection=="2":
                        mycursor.execute("delete from reminder where id=2")
                        conn.commit()
                    if list_selection=="3":
                        mycursor.execute("delete from reminder where id=3")
                        conn.commit()
                    if list_selection=="4":
                        mycursor.execute("delete from reminder where id=4")
                        conn.commit()
                    if list_selection=="5":
                        mycursor.execute("delete from reminder where id=5")
                        conn.commit()

                def exit():
                    frame1.tkraise()
   
                listentry1=StringVar()
                listentry=Entry(frame6,textvariable=listentry1,font="arial 20 bold",bg="light green")
                listentry.grid(row=1,column=0)
                listbtn1=Button(frame6,text="Delete",font="mistral 20 bold",command=delete_reminder,bg="light green")
                listbtn1.grid(row=2,column=0)
                listbtn2=Button(frame6,text="Exit",font="mistral 20 bold",command=exit,bg="light green")
                listbtn2.grid(row=3,column=0)

            def back():
                frame1.destroy()
                self.rem.tkraise()

            btn1=Button(frame1,text="Birthday",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light pink",command=birthday).grid(row=0,column=1,ipadx=136)
            btn2=Button(frame1,text="Anniversary",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light blue",command=anniversary).grid(row=1,column=1,padx=6,ipadx=122)
            btn3=Button(frame1,text="Mourning",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light green",command=mourning).grid(row=2,column=1,padx=6,ipadx=136)
            btn4=Button(frame1,text="Other",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light pink",command=other).grid(row=3,column=1,ipadx=160)
            btn5=Button(frame1,text="Reminder List",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light blue",command=rem_list).grid(row=4,column=1,ipadx=116)
            btn6=Button(frame1,text="Exit",font="mistral 20 bold",bd=5,relief=GROOVE,bg="light green",command=back).grid(row=5,column=1,ipadx=166)

        #----------------alarm & reminder buttons-----------------
        btn1=Button(rem,text="Alarm",font=("mistral", 20, "bold"),command=alarm)
        btn1.place(x=150,y=240)
        btn2=Button(rem,text="Remind Me",font=("mistral", 20, "bold"),command=reminder)
        btn2.place(x=120,y=320)



if __name__ == "__main__":
    rem=Tk()
    obj=remindme(rem)
    rem.mainloop()

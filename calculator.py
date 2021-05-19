from tkinter import*
import tkinter
import math


#global declaration
exp=""


root=Tk()

#window design
root.geometry("400x330+650+100")
root.title("My Calculator")
root.resizable(0,0)
root.config(bg="cyan")

#clear function
def clear():
    global exp
    exp=""
    equation.set("")

#buttons function
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)



#equal function
def equal():
    try:
        global exp
        result=str(eval(exp))
        equation.set(result)
        exp=""

    except:
        equation.set("error")


# Driver code
if __name__ == "__main__":

    #inputbar design
    equation=StringVar()
    input=Entry(root,borderwidth=10,bg="powder blue",relief=RIDGE,width=10,textvariable=equation,font="arial 10 bold").grid(row=0,column=0,columnspan=4,ipady=5,ipadx=100,pady=3)

    #buttons-1
    clear=Button(root,text="C",bg="white",font="arial 15 bold",command=clear).grid(row=1,column=0,columnspan=4,ipadx=132,pady=2)

    #buttons-2
    seven=Button(root,text=7,bg="white",font="arial 15 bold",width=5,command=lambda: press(7)).grid(row=2,column=0,pady=2)
    eight=Button(root,text=8,bg="white",font="arial 15 bold",width=5,command=lambda: press(8)).grid(row=2,column=1,sticky="w",pady=2)
    nine=Button(root,text=9,bg="white",font="arial 15 bold",width=5,command=lambda: press(9)).grid(row=2,column=2,sticky="w",pady=2)
    div=Button(root,text="/",bg="white",font="arial 15 bold",width=5,command=lambda: press("/")).grid(row=2,column=3,sticky="w",pady=2)

    #buttons-3
    four=Button(root,text=4,bg="white",font="arial 15 bold",width=5,command=lambda: press(4)).grid(row=3,column=0,pady=2)
    five=Button(root,text=5,bg="white",font="arial 15 bold",width=5,command=lambda: press(5)).grid(row=3,column=1,sticky="w",pady=2)
    six=Button(root,text=6,bg="white",font="arial 15 bold",width=5,command=lambda: press(6)).grid(row=3,column=2,sticky="w",pady=2)
    multi=Button(root,text="X",bg="white",font="arial 15 bold",width=5,command=lambda: press("*")).grid(row=3,column=3,sticky="w",pady=2)

    #buttons-4
    one=Button(root,text=1,bg="white",font="arial 15 bold",width=5,command=lambda: press(1)).grid(row=4,column=0,pady=2)
    two=Button(root,text=2,bg="white",font="arial 15 bold",width=5,command=lambda: press(2)).grid(row=4,column=1,sticky="w",pady=2)
    three=Button(root,text=3,bg="white",font="arial 15 bold",width=5,command=lambda: press(3)).grid(row=4,column=2,sticky="w",pady=2)
    sub=Button(root,text="-",bg="white",font="arial 15 bold",width=5,command=lambda: press("-")).grid(row=4,column=3,sticky="w",pady=2)

    #buttons-5
    zero=Button(root,text=0,bg="white",font="arial 15 bold",width=5,command=lambda: press(0)).grid(row=5,column=0,pady=2)
    deci=Button(root,text=".",bg="white",font="arial 15 bold",width=5,command=lambda: press(".")).grid(row=5,column=1,sticky="w",pady=2)
    add=Button(root,text="+",bg="white",font="arial 15 bold",width=5,command=lambda: press("+")).grid(row=5,column=2,sticky="w",pady=2)

    #buttons-equal
    equal=Button(root,text="=",bg="white",font="arial 15 bold",command=equal).grid(row=6,column=0,columnspan=4,ipadx=134,pady=2)
    


    root.mainloop()

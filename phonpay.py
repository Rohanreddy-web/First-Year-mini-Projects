from tkinter import *
from tkinter import messagebox
rohan=Tk()
def n():
    if(ep.get()==250106):
       messagebox.showinfo(title="PHON-PAY",message="WELLCOME # ROHAN REDDY #")
    else:
        messagebox.showerror(title="PHON-PAY",message="SORRY WRONG  UPI PIN PLEASE CHICK THE PIN")
def m():
    if(rp.get()<=10000):
       Label(rohan,text="AMOUNT IS TRANSFERRED TO "+" \n"+str(entry106.get())+
             " TRANSFERED AMMOUNT: is\n" +str(rp.get()),font=("Bookerly",12,'bold'),bg="#A32CC4",fg="#52eb34").pack()
    else:
        messagebox.showwarning(title="PHON-PAY",message="INSUFFICIENT BALANCE")
def b():
      messagebox.showinfo(title="PHON-PAY",message="REMAINING BALANCE\n"+str(10000-rp.get()))
def p():
       if(len(entry106.get())==10):
           messagebox.showinfo(title="PHON-PAY",message="CLICK ok FOR FURTHER PROCEEDING\t!!!!")
       else:
           messagebox.showerror(title="PHON-PAY",message="YOUR PHONE NUMBER IS LESS THEN OR GREATHER 10 DIGITS\n!!!!")
rohan.geometry('500x500')
rohan.title("PHON-PAY")
Label0=Label(rohan,text="WELLCOME TO PHON-PAY",font=("Bookerly",16,'bold') ,bg="#A32CC4",fg="white")
Label0.pack()
Label3=Label(rohan,text="enter your method of Teansfer ",font=("Bookerly",12),bg="#A32CC4",fg="white")
Label3.pack(padx=1)
options=StringVar(rohan)
kumar1=OptionMenu(rohan,options,"to mobile", "to bank UPI\ID","to self account")
kumar1.pack(padx=1)
LP1=Label(rohan,text="phon number to (FURTHER TRANSFER )",font=("Bookerly",12),bg="#A32CC4",fg="white")
LP1.pack(padx=1)
entry106=Entry(rohan)
entry106.pack(padx=1)
button5=Button(rohan,text="CLICK",command=p,fg="black",relief=RAISED)
button5.pack(padx=1)

Label4=Label(rohan,text="enter you Amount ",font=("Bookerly",12),bg="#A32CC4",fg="white")
Label4.pack(padx=1)
rp=IntVar()
entry2=Entry(rohan,textvariable=rp)
entry2.pack(padx=1)
Label2=Label(rohan,text="enter your UPI pin",font=("Bookerly",12),bg="#A32CC4",fg="white")
Label2.pack(padx=1)
ep=IntVar()
entry0=Entry(rohan,textvariable=ep,show="*")
entry0.pack(padx=1)
button1=Button(rohan,text="SUBMIT UPI",command=n,fg="black",relief=RAISED)
button1.pack(padx=1)
button2=Button(rohan,text="SUBMIT AMOUNT",command=m,fg="black",relief=RAISED)
button2.pack(padx=1)
Label5=Label(rohan,text="remaining balance",font=("Bookerly",12),bg="#A32CC4",fg="white")
Label5.pack(padx=1)
button2=Button(rohan,text="CLICK FOR BALANCE INQUIRE",command=b,fg="black",relief=RAISED)
button2.pack(padx=1)
rohan.config(background="#A32CC4")
rohan.mainloop()

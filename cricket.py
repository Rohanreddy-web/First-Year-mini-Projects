from tkinter import * 
from tkinter import messagebox
#creating  main window#
rohan=Tk()
rohan.title("Python Project")
rohan.geometry('600x800')
#creating function call back#
def id():
    if (ro.get()== 7671856106 and rp.get()=="rohan106"):
        messagebox.showinfo(title="CRICBUZZ.COM",message="T.SAI ROHAN REDDY PRESS OK FOR CONFORMATION ")

    else:
        messagebox.showerror(title="CRICBUZZ.COM",message="SORRY THERE IS NO ACCOUNT FOR THIS MOBILE NUMBER\n try with an another mobile number \t:(<<<\n or\n your mobile number or pasword is wrong please check it")
#function call back#        
def total():
    Label(rohan,text="TOTAL SCORE\n",fg="red",bg="#32a899",font=("Bookerly",12,'bold')).pack()
    Label(rohan,text=int(r.get())+int(o.get())+int(h.get())+int(a.get())+int(n.get())+int(d.get()),fg="red",bg="#32a899",font=("Bookerly",12,'bold')).pack()
    messagebox.showinfo(title="CRICBUZZ.COM",message="TOTAL SCORE OF THIS OVER IS\n"+str(int(r.get())+int(o.get())+int(h.get())+int(a.get())+int(n.get())+int(d.get())))
    #creating label#
Label0=Label(rohan,text="CRICBUZZ.COM",font=("Bookerly",16,'bold'),fg="#FFD700",bg="#32a899",relief=RAISED)
Label0.pack()
   #creating label#
Label3=Label(rohan,text="enter your mobile number  to Log.in",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
#creating an integer input entry #
ro=IntVar()
Label3.pack(padx=1)
#entry#
entry=Entry(rohan,textvariable=ro)
entry.pack(padx=1)
   #creating label#
Label4=Label(rohan,text=" enter your password",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label4.pack(padx=1)
#creating an string entry#
rp=StringVar()
#entry#
entry=Entry(rohan,textvariable=rp,show="*")
entry.pack(padx=1)
#creating a button#
button=Button(rohan,text="SUBMIT",font=("Bookerly",11),command=id,relief=RAISED,fg="black")
button.pack(padx=1)
   #creating label#
Labelz=Label(rohan,text="select country",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Labelz.pack(padx=1)
#creating an option menu#
options=StringVar(rohan)
l=OptionMenu(rohan,options,"INDIA","PAKISTAN","NEW ZEALAND")
l.pack(padx=1)
   #creating label#
Labelx=Label(rohan,text="select the batsman",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Labelx.pack(padx=1)
#creating a option menu#
options=StringVar(rohan)
k=OptionMenu(rohan,options,"MS Dhoni", "Virat Kohli","Rohit Shaarma","Ravindra Jadeja","Krdar Jadhav","Ravichandran Ashwin")
k.pack(padx=1)
   #creating label#
Label5=Label(rohan,text="PLEASE ENTER THE SCORE",font=("Bookerly",14),fg="#FFD700",bg="#32a899")
Label5.pack(padx=1)
   #creating label#
Label12=Label(rohan,text="TOTAL WICKETS",font=("Bookerly",16),fg="#FFD700",bg="#32a899")
Label12.pack(side=RIGHT)
#creating a option menu#
options=IntVar(rohan)
P=OptionMenu(rohan,options,"0","1","2","3","4","5","6")
P.pack(side=RIGHT)

#creating an integer type entrys#(total are "6")
r=IntVar()
o=IntVar()
h=IntVar()
a=IntVar()
n=IntVar()
d=IntVar()
   #creating label#
Label6=Label(rohan,text="First ball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label6.pack(padx=1)
#entry#
entryr=Entry(rohan,textvariable=r)
entryr.pack(padx=1)
   #creating label#
Label7=Label(rohan,text="Second ball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label7.pack(padx=1)
#entry
entryo=Entry(rohan,textvariable=o)
entryo.pack(padx=1)
   #creating label#
Label8=Label(rohan,text="Thard ball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label8.pack(padx=1)
#entry#
entryh=Entry(rohan,textvariable=h)
entryh.pack(padx=1)
   #creating label#
Label9=Label(rohan,text="Fourthball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label9.pack(padx=1)
#entry#
entrya=Entry(rohan,textvariable=a)
entrya.pack(padx=1)
   #creating label#
Label10=Label(rohan,text="Fifth ball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label10.pack(padx=1)
#entry#
entryn=Entry(rohan,textvariable=n)
entryn.pack(padx=1)
   #creating label#
Label11=Label(rohan,text="Sixth ball:",font=("Bookerly",12),fg="#FFD700",bg="#32a899")
Label11.pack(padx=1)
#entry#
entryd=Entry(rohan,textvariable=d)
entryd.pack(padx=1)
#creating a button#
button2=Button(rohan,text="CLICk",command=total,relief=RAISED,fg="black")
button2.pack(padx=1)
#baground colour#
rohan.config(background="#32a899")
#ending the program
rohan.mainloop()
#THE END#

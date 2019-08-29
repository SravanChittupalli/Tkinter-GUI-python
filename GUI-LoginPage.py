#This is a login page with sign up,login and forgot password options

import tkinter as tk
import tkinter.ttk as ttk
import getpass
from tkinter import E,W
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
import random
import os

window=tk.Tk()

window.title('HOME PROJECT')
window.geometry('500x350')

lbl3=tk.Label(window,text="Welcome to PlasmaTech's Login Page",font=('Comic San MS',10))
lbl3.grid(column=0,row=0,padx=5,pady=5)
lbl1=tk.Label(window,text='UserName: ',font=('Comic San MS',10))
lbl1.grid(column=0,row=1,sticky=E,padx=5,pady=5)
lbl2=tk.Label(window,text='Password: ',font=('Comic San MS',10))
lbl2.grid(column=0,row=2,sticky=E,padx=5,pady=5)

txt1=tk.Entry(window,width=20)
txt1.grid(column=1,row=1)
txt2=tk.Entry(window,width=20,show='*')
txt2.grid(column=1,row=2)

def new():
    signup=tk.Tk()
    signup.title('CREATE AN ACCOUNT')
    signup.geometry('400x250')

    lbl1=tk.Label(signup,text='Name: ',font=('Comic San MS',10))
    lbl1.grid(column=0,row=0,sticky=E,padx=5,pady=5)
    lbl2=tk.Label(signup,text='Phone Number: ',font=('Comic San MS',10))
    lbl2.grid(column=0,row=1,sticky=E,padx=5,pady=5) 
    lbl3=tk.Label(signup,text='New Password: ',font=('Comic San MS',10))
    lbl3.grid(column=0,row=2,sticky=E,padx=5,pady=5)
    lbl4=tk.Label(signup,text='Re-enter Password: ',font=('Comic San MS',10))
    lbl4.grid(column=0,row=3,sticky=E,padx=5,pady=5) 
    lbl5=tk.Label(signup,text='Date Of Birth: ',font=('Comic San MS',10))
    lbl5.grid(column=0,row=4,sticky=E,padx=5,pady=5)

    def keyPress(event):
        if ( event.char >= 'a' and event.char <= 'z' ):
            messagebox.showerror('ERROR','Only Numerical Values Are Allowed')
    
    
    txt5=tk.Entry(signup,width=20)
    txt5.grid(column=1,row=0)
    txt6=tk.Entry(signup,width=20)
    txt6.grid(column=1,row=1)
    txt3=tk.Entry(signup,width=20,show='*')
    txt3.grid(column=1,row=2)
    txt4=tk.Entry(signup,width=20,show='*')
    txt4.grid(column=1,row=3)
    
    DOB=DateEntry(signup)
    DOB.grid(column=1,row=4)
    txt6.bind('<KeyPress>', keyPress) #keypress event detection

    def save():
        if(txt3.get() != txt4.get()):
            messagebox.showerror('ERROR','New and Re-Entered Password must be the same')
        fwrite=open('CustomerRecords.log','a')
        name=txt5.get()
        phno=txt6.get()
        passw=txt3.get()
        dob=DOB.get()
        fwrite.write(name+';'+phno+';'+passw+';')
        fwrite.write(dob)
        fwrite.write('\n')
        fwrite.close()
        
    btn4=tk.Button(signup,text='Sign up',command=save)
    btn4.grid(column=1,row=5,sticky=E,padx=10,pady=10)

def login():
    flag=0
    fread=open('CustomerRecords.log','r')
    readwhole=fread.read()
    count_records=readwhole.count('\n')
    fread.seek(0,0)
    for count1 in range (0,count_records,1):
        read_line=fread.readline()
        seperated_line=read_line.split(';')
        if(seperated_line[0]==txt1.get() and seperated_line[2]==txt2.get()):
            flag=1
            login=tk.Tk()
    if(flag==0):
        messagebox.showerror('ERROR','Incorrect Password')
def forgot():
    forgot=tk.Tk()
    forgot.title('FORGOT PASSWORD')
    forgot.geometry('300x200')

    lbl6=tk.Label(forgot,text='OTP: ',font=('Comic San MS',10))
    lbl6.grid(column=0,row=0,sticky=E)

    txt7=tk.Entry(forgot,width=15)
    txt7.grid(column=1,row=0,sticky=W)

    def genotp():
        otp=tk.Tk()
        otp.title('OTP')
        otp.geometry('300x50')

        OTP=random.randint(1000,9999)
        charOTP=str(OTP)
        fop=open('OTP.log','w')
        fop.write(charOTP)
        fop.close()
        lbl7=tk.Label(otp,text="Your OTP is:{} ".format(OTP),font=('Ariel Bold',25) )
        lbl7.grid(column=0,row=0)

    def passw():
        fread=open('OTP.log','r')
        OTPnew=fread.read()
        if(txt7.get()==OTPnew):
            fread.close()
            forgotpass=tk.Tk()
            forgotpass.title('RESET PASSWORD WINDOW')
            forgotpass.geometry('650x300')

            lbl9=tk.Label(forgotpass,text='ENTER YOUR CREDENTIALS HERE',font=('Ariel Bold',20))
            lbl9.grid(column=0,row=0)
            lbl10=tk.Label(forgotpass,text='UserName:',font=('Comic San MS',10))
            lbl10.grid(column=0,row=1,sticky=E,padx=5,pady=5)
            lbl7=tk.Label(forgotpass,text='New Password:',font=('Comic San MS',10))
            lbl7.grid(column=0,row=2,sticky=E,padx=5,pady=5)
            lbl8=tk.Label(forgotpass,text='Confirm Password:',font=('Comic San MS',10))
            lbl8.grid(column=0,row=3,sticky=E,padx=5,pady=5)

            txt8=tk.Entry(forgotpass,width=15,show='*')
            txt8.grid(column=1,row=2,sticky=W)
            txt9=tk.Entry(forgotpass,width=15,show='*')
            txt9.grid(column=1,row=3,sticky=W)
            txt10=tk.Entry(forgotpass,width=15)
            txt10.grid(column=1,row=1)

            def click():
                if(txt8.get() != txt9.get()):
                    messagebox.showerror('ERROR','New and Re-Entered Password must be the same')
                else:
                    fread=open('CustomerRecords.log','r')
                    fwrite=open('Temp.log','a')
                    wholerecord=fread.read()
                    CountLines=wholerecord.count('\n')
                    DividedLine=wholerecord.split('\n')
                    for count in range ( 0 , CountLines , 1 ):
                        CheckName=DividedLine[count].split(';')
                        if ( CheckName[0]==txt10.get() ):
                            CheckName[2]=txt8.get()
                            fwrite.write(CheckName[0]+';'+CheckName[1]+';'+CheckName[2]+';'+CheckName[3]+'\n')

                        else:
                            fwrite.write(DividedLine[count])
                            fwrite.write('\n')
                    fwrite.close()
                    fread.close()
                    os.remove('CustomerRecords.log')
                    os.replace('Temp.log','CustomerRecords.log')

                                
            btn7=tk.Button(forgotpass,text='Reset Password',command=click)
            btn7.grid(column=1,row=4,sticky=W)

        else:
            messagebox.showerror('ERROR','OTP DID NOT MATCH....PLEASE TRY AGAIN')

    btn5=tk.Button(forgot,text='Enter',command=passw)
    btn5.grid(column=0,row=1,sticky=W,padx=5,pady=5)
    btn6=tk.Button(forgot,text='Generate OTP',command=genotp)
    btn6.grid(column=1,row=1,sticky=W,padx=5,pady=5)

    
btn1=tk.Button(window,text='Create A New Account',command=new)
btn1.grid(column=1,row=4,columnspan=10,sticky=W)
btn2=tk.Button(window,text='Log In',command=login)
btn2.grid(column=1,row=3,sticky=W,pady=5)
btn3=tk.Button(window,text='Forgot Password',command=forgot)
btn3.grid(column=2,row=3,sticky=W,pady=5)

window.mainloop()



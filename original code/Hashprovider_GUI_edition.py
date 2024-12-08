# -*- coding: utf-8 -*-

import hashlib
from io import open
import tkinter.ttk

from tkinter import filedialog
from tkinter import Text,messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Label,Button
#importing

def allerror():
    errorbar = messagebox.showerror(title="Error",message="Imput the text and times first")

def notexterror():
    errorbar = messagebox.showerror(title="Error",message="Empty text")

def notimeserror():
    errorbar = messagebox.showerror(title="Error",message="Invaild times")

def fileerror():
    errorbar = messagebox.showerror(title="Error",message="Invaild times")

def tips():
    tipsbar = messagebox.showwarning(title="Caution",message='''The valve you input is too large,software may take a long time to finish it.
The software may be not responsed.However,after a few times,the result will be worked out.
The time you have to wait depends on your performance of your computer''')

def toosmall():
    warningbar = messagebox.showwarning(title="Too small",message="The window size is too small!")
    body.geometry("800x600+%d+%d"%(centerwid,centerhei))

def sha1core(timestohash,readytohash):
    timestohash = int(timestohash)

    if timestohash > 2500000:
        tips()
    #Too large!

    for timestohash in range (timestohash):
        output = hashlib.sha1(readytohash.encode()).hexdigest()
        readytohash = output
    #Let's cycle

    body2 = tkinter.Toplevel(takefocus=1,bg="#f0f8ff")
    body2.withdraw()
    body2.update()

    body2.title("Result")

    body2.iconbitmap("./icons.ico")
    body2.wm_iconbitmap("./icons.ico")
    body2.resizable(False,False)
    body2.deiconify()

    def cpy():
        body2.clipboard_clear()
        body2.clipboard_append(result.cget("text"))
    #Copy me!

    result = Label(body2,justify="center",text=(output),background="Aliceblue")
    result.grid(row=0,column=0)

    copyme = Button(body2,text="Copy",command=cpy)
    copyme.grid(row=1,column=0)

    body2.mainloop()
    #Resultbar

def sha224core(timestohash,readytohash):
    timestohash = int(timestohash)

    if timestohash > 2500000:
        tips()
    #Too large!

    for timestohash in range (timestohash):
        output = hashlib.sha224(readytohash.encode()).hexdigest()
        readytohash = output
    #Let's cycle

    body2 = tkinter.Toplevel(takefocus=1,bg="#f0f8ff")
    body2.withdraw()
    body2.update()

    body2.title("Result")

    body2.iconbitmap("./icons.ico")
    body2.wm_iconbitmap("./icons.ico")
    body2.resizable(False,False)
    body2.deiconify()

    def cpy():
        body2.clipboard_clear()
        body2.clipboard_append(result.cget("text"))
    #Copy me!

    result = Label(body2,justify="center",text=(output),background="Aliceblue")
    result.grid(row=0,column=0)

    copyme = Button(body2,text="Copy",command=cpy)
    copyme.grid(row=1,column=0)

    body2.mainloop()
    #Resultbar

def sha256core(timestohash,readytohash):
    timestohash = int(timestohash)

    if timestohash > 2500000:
        tips()
    #Too large!

    for timestohash in range (timestohash):
        output = hashlib.sha256(readytohash.encode()).hexdigest()
        readytohash = output
    #Let's cycle

    body2 = tkinter.Toplevel(takefocus=1,bg="#f0f8ff")
    body2.withdraw()
    body2.update()

    body2.title("Result")

    body2.iconbitmap("./icons.ico")
    body2.wm_iconbitmap("./icons.ico")
    body2.resizable(False,False)
    body2.deiconify()

    def cpy():
        body2.clipboard_clear()
        body2.clipboard_append(result.cget("text"))
    #Copy me!

    result = Label(body2,justify="center",text=(output),background="Aliceblue")
    result.grid(row=0,column=0)

    copyme = Button(body2,text="Copy",command=cpy)
    copyme.grid(row=1,column=0)

    body2.mainloop()
    #Resultbar

def sha384core(timestohash,readytohash):
    timestohash = int(timestohash)

    if timestohash > 2500000:
        tips()
    #Too large!

    for timestohash in range (timestohash):
        output = hashlib.sha384(readytohash.encode()).hexdigest()
        readytohash = output
    #Let's cycle

    body2 = tkinter.Toplevel(takefocus=1,bg="#f0f8ff")
    body2.withdraw()
    body2.update()

    body2.title("Result")

    body2.iconbitmap("./icons.ico")
    body2.wm_iconbitmap("./icons.ico")
    body2.resizable(False,False)
    body2.deiconify()

    def cpy():
        body2.clipboard_clear()
        body2.clipboard_append(result.cget("text"))
    #Copy me!

    result = Label(body2,justify="center",text=(output),background="Aliceblue")
    result.grid(row=0,column=0)

    copyme = Button(body2,text="Copy",command=cpy)
    copyme.grid(row=1,column=0)

    body2.mainloop()
    #Resultbar

def sha1():
    readytohash =textreq.get(1.0,tkinter.END)[:-1]
    timestohash = times.get(1.0,tkinter.END)[:-1]
    check = timestohash.isdigit()
    ifitisnone = str(times.get(1.0,tkinter.END))
    #Get variable

    if check == False and readytohash == "":
        allerror()
        return None

    if readytohash == "":
        notexterror()
        return None

    if check == False:
        notimeserror()
        return None


    sha1core(timestohash=timestohash,readytohash=readytohash)
    if ifitisnone == r"\n":
        return None
    #Something lost
#sha1

def sha224():
    readytohash =textreq.get(1.0,tkinter.END)[:-1]
    timestohash = times.get(1.0,tkinter.END)[:-1]
    check = timestohash.isdigit()
    ifitisnone = str(times.get(1.0,tkinter.END))
    #Get variable

    if check == False and readytohash == "":
        allerror()
        return None

    if readytohash == "":
        notexterror()
        return None

    if check == False:
        notimeserror()
        return None

    sha224core(timestohash=timestohash,readytohash=readytohash)
#sha224

def sha256():
    readytohash =textreq.get(1.0,tkinter.END)[:-1]
    timestohash = times.get(1.0,tkinter.END)[:-1]
    check = timestohash.isdigit()
    ifitisnone = str(times.get(1.0,tkinter.END))
    #Get variable

    if check == False and readytohash == "":
        allerror()
        return None

    if readytohash == "":
        notexterror()
        return None

    if check == False:
        notimeserror()
        return None

    sha256core(timestohash=timestohash,readytohash=readytohash)
#sha256

def sha384():
    readytohash =textreq.get(1.0,tkinter.END)[:-1]
    timestohash = times.get(1.0,tkinter.END)[:-1]
    check = timestohash.isdigit()
    ifitisnone = str(times.get(1.0,tkinter.END))
    #Get variable

    if check == False and readytohash == "":
        allerror()
        return None

    if readytohash == "":
        notexterror()
        return None

    if check == False:
        notimeserror()
        return None

    sha384core(timestohash=timestohash,readytohash=readytohash)
#sha384

#Those are the calculator core

def filewithsha1():
    global filename,whatinthefile
    filename = filedialog.askopenfilename()

    if filename == None:
        return None

    whatinthefile = str(open(filename,mode="r"))

    requesttimes = times.get(1.0,tkinter.END)[:-1]
    if requesttimes == "":
        fileerror()
        return None

    requesttimes = int(requesttimes)

    sha1core(timestohash=requesttimes,readytohash=whatinthefile)

def filewithsha224():
    filename = filedialog.askopenfilename()

    if filename == None:
        return None

    whatinthefile = str(open(filename,mode="r"))

    requesttimes = times.get(1.0,tkinter.END)[:-1]
    if requesttimes == "":
        fileerror()
        return None

    requesttimes = int(requesttimes)

    sha224core(timestohash=requesttimes,readytohash=whatinthefile)

def filewithsha256():
    filename = filedialog.askopenfilename()

    if filename == None:
        return None

    whatinthefile = str(open(filename,mode="r"))

    requesttimes = times.get(1.0,tkinter.END)[:-1]
    if requesttimes == "":
        fileerror()
        return None

    requesttimes = int(requesttimes)

    sha256core(timestohash=requesttimes,readytohash=whatinthefile)

def filewithsha384():
    filename = filedialog.askopenfilename()

    if filename == None:
        return None

    whatinthefile = str(open(filename,mode="r"))

    requesttimes = times.get(1.0,tkinter.END)[:-1]
    if requesttimes == "":
        fileerror()
        return None

    requesttimes = int(requesttimes)

    sha384core(timestohash=requesttimes,readytohash=whatinthefile)

def modern(args):
    height = body.winfo_height()
    width = body.winfo_width()
    if height < 500 or width < 780:
        toosmall()
        body.update()

    textheight = int(height/18)
    textwidth = int(width/12)

    textreq.config(height=textheight,width=textwidth,font=("Microsoft YaHei UI",8),background="Aliceblue")
    textreq.grid(row=2,column=0,rowspan=20)

    timesheight = int(height/600)
    timeswidth = int(width/60)

    times.config(height=timesheight,width=timeswidth,font=("Microsoft YaHei UI",8),background="Aliceblue")
    times.grid(row=1,column=1)

    config = open("config"+"."+"txt",mode="w+")

    config.write(str(height)+"\n")
    config.write(str(width))
    config.close()


with open("./config.txt","r") as conf:
    lines = conf.readlines()
    line1 = lines[0]
    line2 = lines[1]

bodyhei = int(line1)
bodywid = int(line2)

body = tkinter.Tk()

sizewid = body.winfo_screenwidth()
sizehei = body.winfo_screenheight()

centerwid = int(sizewid-bodywid)/2
centerhei = int(sizehei-bodyhei-100)/2

body.bind("<Configure>",modern)
body.title("Hash Calculator,version1.3")
body.withdraw()
body.update()

body.iconbitmap("./icons.ico")
body.wm_iconbitmap("./icons.ico")

body.config(bg="#f0f8ff")
body.geometry("%dx%d+%d+%d"%(bodywid,bodyhei,centerwid,centerhei))
body.deiconify()
#Set the window

text = Label(body,text="Hash Calculator,version1.3",justify="center")
text.config(font=("Microsoft YaHei UI",24),background="Aliceblue")
text.grid(row=0,column=0)
#Copyright

req = Label(body,text="enter the text here")
req.config(background="Aliceblue")
req.grid(row=1,column=0)

textreq = ScrolledText(body,exportselection=0,height=40,width=130,highlightthickness=0)
#readytohash

timesreq = Label(body,text='''Enter the times
if you want to get a file's hash,imput it first.''')
timesreq.config(background="Aliceblue")
timesreq.grid(row=0,column=1)

times = Text(body,height=1,width=20)
#timestohash

formreq = Label(body,text='Select the type')
formreq.config(background="Aliceblue")
formreq.grid(row=3,column=1)

select = Button(body,text="sha1",command=sha1)
select.grid(row=4,column=1)

select2 = Button(body,text="sha224",command=sha224)
select2.grid(row=5,column=1)

select3 = Button(body,text="sha256",command=sha256)
select3.grid(row=6,column=1)

select4 = Button(body,text="sha384",command=sha384)
select4.grid(row=7,column=1)
#formattohash

sha1filereq = Button(text="  Hash a file with sha1  ",command=filewithsha1)
sha1filereq.grid(row=0,column=3)

sha224filereq = Button(text="Hash a file with sha224",command=filewithsha224)
sha224filereq.grid(row=1,column=3)

sha256filereq = Button(text="Hash a file with sha256",command=filewithsha256)
sha256filereq.grid(row=2,column=3)

sha384filereq = Button(text="Hash a file with sha384",command=filewithsha384)
sha384filereq.grid(row=3,column=3)

#Hash file buttons

body.mainloop()


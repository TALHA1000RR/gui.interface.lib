import guis
import tkinter as tk
import time


def mainloop(selfs,root:tk.Tk):
    count=0
    while 1:
        print(count)
        try:
           selfs.text.delete("0","end")
           selfs.text.insert("0",str(count))
        except:
            break
        time.sleep(1)
        count=count+1



def startmain(selfs,root:tk.Tk):
    selfs.text=tk.Entry(background="black",foreground="white")
    selfs.text.pack(padx=10,pady=10)
   



apps=guis.inits(startsubs=startmain,mainsubs=mainloop,title="my apps",backgrounds="black", foregrounds="white")

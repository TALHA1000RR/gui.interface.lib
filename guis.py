import tkinter as tk
import threading



class myapps:
    def __init__(self,root:tk.Tk,startsubs,mainsubs,titles:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(titles)
        self.root.configure(background=backgrounds)
        self.fogrounds=foregrounds
        self.startsubs=startsubs
        self.mainsubs=mainsubs
        self.time=threading.Thread(target=self.mains)
        
        self.startsubs(self,self.root)
        
        self.time.start()
    def mains(self):
        self.mainsubs(self,self.root)

        





def inits(startsubs,mainsubs,title:str,backgrounds:str,foregrounds:str):
    root=tk.Tk()
    apps=myapps(root,startsubs,mainsubs,title,backgrounds,foregrounds)
    root.mainloop()
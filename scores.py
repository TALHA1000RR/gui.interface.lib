class scores:
    def __init__(self,inits):
        self.value=inits
    
    def scr(self,values):
        self.value=self.value+values
    
    def report(self):
        print(str(self.value) + " ps")

ps=10
total=0
scor=scores(0)
for a in range (10):
    scor.report()
    scor.scr(ps)
dim x as integer=710
dim y as integer=1170
'eu a4
dim colors as integer=14
dim colors2 as integer=0
dim grid as integer=30
dim mx as double=x\256
dim my as double=y\256
dim xx as double=mx*grid
dim yy as double=my*grid
dim n as double=0.00
dim nn as integer=0
color 0,6
cls
ScreenRes 320, 200, 32
color 0,colors
cls 
print "creat..."
dim graphic as any ptr= imagecreate(x, y, rgb(255,255,0),32)
line graphic,(0,0)-(x,y), rgb(255,255,0),bf
line graphic,(0,0)-(x-1,y-1),colors2,b
for n=0 to 255
    nn=(255-n)\2
    yy=my*(255-n)
    xx=mx*(255-n)
    line graphic,(n,n)-(n+xx,n+yy),rgb(255,255,n),bf
next


bsave "my.bmp",graphic
ImageDestroy graphic
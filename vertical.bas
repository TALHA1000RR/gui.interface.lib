dim x as double=710
dim y as double=1170
'eu a4
dim colors as integer=14
dim colors2 as integer=0
dim colors3 as integer=6
dim grid as double=47.2
dim grid2 as double=grid/10
dim grid3 as double=grid/2
dim n as double=0
dim nn as double=0
dim counter as integer=0
dim counter2 as integer=0
dim counter3 as integer=0
color 0,colors3
cls 
print "creat..."
screen 12
color 0,colors
cls 

dim graphic as any ptr= imagecreate(x, y, colors,4)
line graphic,(0,0)-(x,y),colors,bf
line graphic,(0,0)-(x-1,y-1),colors2,b
color 0
for nn=0 to y step 100
    counter=0
    counter2=0
    counter3=0
    for n=0 to 25
        
        line graphic,(nn+0,n*grid)-(nn+30,n*grid),colors2
        counter2=counter\10
        Draw String graphic,(nn+50,counter*grid),rtrim(ltrim(str(counter2))),colors2
    
    
    
   
    
        Draw String graphic,(nn+65,counter*grid),rtrim(ltrim(str(counter3))),colors2
        counter3=counter3+1
        counter=counter+1
        if counter3>9 then counter3=0
    next
    for n=0 to 250
        line graphic,(0+nn,n*grid2)-(nn+15,n*grid2),colors2
    next
    for n=0 to 50
        line graphic,(0+nn,n*grid3)-(nn+25,n*grid3),colors2
    next
next
bsave "my.bmp",graphic
ImageDestroy graphic
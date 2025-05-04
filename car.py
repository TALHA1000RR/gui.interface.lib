
import time
import random
print ("\033c\033[43;30m\nenter simulator\n")
def floats():
    f=float(random.randrange(1,9)-5)
    return f
def collapseEvent():
    rets=random.randrange(1,1000)
    retss=rets>995
    return retss
def sims(n):
    totals=0
    money=float(0.0)
    rets=[]
    nn=0
    t=True
    truck=float(0.0)
    car=float(0.0)
    while t:
        print(str(totals)+" units")
        totals=totals+n
        if collapseEvent():
           print("collapse event all car as destroy")
           totals=0
        if totals>10:
            totals=0
            car=float(9.00+floats())
            truck=float(9.00+floats())
            
            print("truck=2 X "+str(float(truck))+" ="+str(float(truck*2.00)))
            print("car=8 X "+str(float(car))+" ="+str(float(car*8.00)))
            money=money+float(truck*8.00)+float(car*8.00)-float(110.00)
            print("expenses="+str(float(110.00)))
            print("money="+str(float(money)))
            print("8 units as car")
            print("2 units truck")
        time.sleep(1)
    
sims(1)
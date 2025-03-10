num=1000
divsn=9
n=100
nn=200
v=0
def mults(value):
    global num
    return value*num
def divs(value):
    global num
    return value//num
def maths(min,max,value):
    return(max-min)//value
t=True
n=mults(n)
nn=mults(nn)
v=maths(n,nn,divsn)
print("\033c\033[43;30m\n")
print(str(n)+"="+str(divs(n)))
while t:
    n=n+v
    if n<nn:
        print(str(n)+"="+str(divs(n)))
    else:
        t=0
        

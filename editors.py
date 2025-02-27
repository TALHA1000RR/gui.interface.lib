print("\033c\033[43;30m\n")
LLoops=True
a=input("give a name to new file ? ")
aa=""
aaa=""
print("to exit input empty line")
while LLoops:
    aaa=input("")
    aa=aa+"\n"+aaa
    if aaa.strip()=="":
        LLoops=False

f1=open(a,"w")
f1.write(aa)
f1.close
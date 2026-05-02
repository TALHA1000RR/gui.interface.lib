#change next 2 lines
winas="c:\\MinGW\\bin\\as.exe"
winobj="c:\\MinGW\\bin\\objdump.exe"
import os
txt=".intel_syntax noprefix\n"
for a in range(1,10):
    txt=txt+"a"+str(a)+":\n.word " +str(a)+"\n"
f1=open("out.s","w")
f1.write(txt)
f1.close()
os.system(winas+" --32 -o out.o out.s")
os.system("type out.o")
os.system(winobj+" -x out.o")

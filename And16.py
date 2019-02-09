## Script to write two 16-bit And inputs 


f=open("And16.txt","w+")

for i in range(16):
    f.write("And(a=a[%d], b=b[%d], out=out[%d]);\n" %(i,i,i))

f.close()

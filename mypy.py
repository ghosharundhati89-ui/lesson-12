f1=open("codingal.txt","w")
f1.write("codingal is in a mission to teach coding")
f1.close()
f1=open("codingal.txt","r")
print(f1.read())
f1.close()
f1=open("codingal.txt","a")
f1.write("codingal is in a mission to teach coding")
f1.close()
f1=open("codingal.txt","r")
print(f1.read())
c=0
content=f1.read()
olist=content.split("\n")
for lines in olist:
    if lines:
      c+=1
print(c)
f1.close()

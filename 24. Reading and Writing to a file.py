
f=open('mytext.txt','w')
f.write("I ")
f.write("am ")
f.write("student ")
f.write("of ")
f.write("NiT")
f.close()

x=open('mytext.txt','r')
s=x.read()
print(s)
print(type(s))
x.close()

# if we just write this it overwrites the file instead of add newline
# f=open('mytext.txt','w')
# f.write("NiT = Narula Institue of Technology")

f=open('mytext.txt','a')
f.write("\n")
f.write("NiT = Narula Institue of Technology")
f.close()

x=open('mytext.txt','r')
s=x.read()
print(s)
x.close()

a_1=1
n=5
d=3
f = open('mytext.txt','w')
f.write(str(a_1))
for i in range(1,n):
    f.write('\n')
    x=str(a_1+i*d)
    f.write(x)
f.close()


x=open('mytext.txt','r')
s=x.read()
print(s)
x.close()
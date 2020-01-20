
n=input("enter string\n")
k=input("enter key\n")
k=int(k)
a=""
b=" "
for i in range(len(n)):
	b=ord(n[i])-97
	b=(b*k)%26
	b=chr(b+97)
	a=a+b
print("Encrypted")
print(a)

r1=26
r2=k
t1=0
t2=1
t=0

while(r2>0):
	q=r1//r2
	r=r1-q*r2
	r1=r2
	r2=r
	t=t1-q*t2
	t1=t2
	t2=t

if r1==1:
	k=(t1)%26
print(k)

c=""
b=" "
for i in range(len(a)):
	b=ord(a[i])-97
	b=(b*k)%26
	b=chr(b+97)
	c=c+b
print("Decrypted")
print(c)

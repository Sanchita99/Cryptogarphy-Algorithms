
n=input("enter string\n")
k=input("enter key\n")
k=int(k)
a=""
b=" "
for i in range(len(n)):
	b=ord(n[i])-97
	b=(b+k)%26
	b=chr(b+97)
	a=a+b
print("Encrypted")
print(a)

c=""
b=" "
for i in range(len(a)):
	b=ord(a[i])-97
	b=(b-k)%26
	b=chr(b+97)
	c=c+b
print("Decrypted")
print(c)

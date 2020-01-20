
import random
import math
import sympy

p=sympy.randprime(100,1000)
while(1):
	q=sympy.randprime(100,1000)
	if p!=q:
		break

n=p*q

phi=(p-1)*(q-1)

e=random.randint(1,phi+1)
#print(e)
while(math.gcd(e,phi)!=1):
	e=random.randint(1,phi+1)

r1=phi
r2=e
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
	d=(t1)%phi
print('This is d {}'.format(d))

m=int(input('Enter Message: '))
# p=''
# for i in m:
# 	p+="{0:08b}".format(ord(m))
# 	print(p)
c=(m**e)%n

mm=(c**d)%n

print('Decrypted message: {}'.format(mm))
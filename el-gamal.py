
import sympy
import random
import math

def group(p):
	g=[]
	for i in range(1,p):
		if math.gcd(i,p)==1:
			g.append(i)

	r=[]
	v=[0]*len(g)

	for i in g:
		z=100
		for j in range(len(g)+1):

			if j==0:
				m=1
			else:
				m=(i**j)%p
			q=g.index(m)
			v[q]=1
		for j in range(len(g)):
			if v[j]==0:
				v=[0]*len(g)
				z=1
				break
		if z==100:
			v=[0]*len(g)
			r.append(i)
	e1=random.choice(r)
	return e1

def moduloinverse(b,n):
	r1=n
	r2=b
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
		k=(t1)%n
	#print(k)
	return k


def ElGamal():

	# Key Generation
	p=sympy.randprime(10,50)
	d=random.randint(1,p-2)
	e1=group(p)
	e2=(e1**d)%p

	#Encyption
	r=random.randint(1,p)
	c1=(e1**r)%p
	M=int(input('Enter msg: '))
	c2=(M*(e2**r))%p
	# print(c1)
	# print(c2)

	#Decryption
	inv=moduloinverse((c1**d),p)
	MM=((c2%p)*(inv))%p
	print('Decrypted Text: %d'%M)

ElGamal()
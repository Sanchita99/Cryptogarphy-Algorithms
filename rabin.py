
import random
import math
import sympy

def crt(a1,a2,p,q):
	m=p*q
	m1=m/p
	m2=m/q

	r1=p
	r2=m1
	t1=0
	t2=1
	t=0

	while(r2>0):
		u=r1//r2
		r=r1-u*r2
		r1=r2
		r2=r
		t=t1-u*t2
		t1=t2
		t2=t
		#print(r1,r2)

	if r1==1:
		mm1=(t1)%p

	r1=q
	r2=m2
	t1=0
	t2=1
	t=0

	while(r2>0):
		u=r1//r2
		r=r1-u*r2
		r1=r2
		r2=r
		t=t1-u*t2
		t1=t2
		t2=t

	if r1==1:
		k=(t1)%q
		mm2=k

	p=(a1*m1*mm1+a2*m2*mm2)%m
	#print(m1,mm1,m2,mm2)
	print(p)

def rabin():
	#Key Generation
	# p=sympy.randprime(10,100)
	# while(1):
	# 	q=sympy.randprime(10,100)
	# 	if p!=q:
	# 		break

	p=23
	q=7
	n=p*q

	#Encryption
	m=int(input('Enter Text: '))
	c=(m**2)%n

	#Decryption
	a1=(c**((p+1)/4))%p
	a2=(-c**((p+1)/4))%p
	b1=(c**((q+1)/4))%q
	b2=(-c**((q+1)/4))%q

	crt(a1,b1,p,q)
	crt(a1,b2,p,q)
	crt(a2,b1,p,q)
	crt(a2,b2,p,q)

rabin()

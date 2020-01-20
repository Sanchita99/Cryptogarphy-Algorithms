
import numpy as np

s=str(input("enter string\n"))
name = s
n=len(s)

st=list(s)
for i in range(n):
	if st[i]=='j':
		st[i]='i'

s=''.join(st)

m=(['l','g','d','b','a'],
	['q','m','h','e','c'],
	['u','r','n','i','f'],
	['x','v','s','o','k'],
	['z','y','w','t','p'])

#Process before encrpytion
for i in range(n-1):
	if s[i]==s[i+1]:
		s=s[:i+1]+'x'+s[i+1:]
		i=i+1
		n=len(s)
		# print(s)
		# print(n)
if n%2!=0:
	s=s[:n]+'x'
	n=len(s)
print('final:')
print(s)


#Encryption
u_m=np.array(list(s))
m=np.array(m)
# print(m.shape)
# print('here')
#print(u_m)
matrix = u_m.reshape(-1, 2) 
r=matrix.shape[0]
e=[]
for i in range(r):
	[ar]=np.where(m==matrix[i][0])[0]
	[ac]=np.where(m==matrix[i][0])[1]
	[br]=np.where(m==matrix[i][1])[0]
	[bc]=np.where(m==matrix[i][1])[1]

	if ar==br:
		ac=(ac+1)%5
		bc=(bc+1)%5
		#print(ac, bc)

	elif ac==bc:
		ar=(ar+1)%5
		br=(br+1)%5

	else:
		k=ac
		ac=bc
		bc=k
	e.append([m[ar][ac],m[br][bc]])
	# e[i][0]=m[ar][ac]
	# e[i][1]=m[br][bc]


print('Encrypted')
print(e)

#Decryption
e=np.array(e)
e_matrix = e.reshape(-1, 2) 
r=e_matrix.shape[0]
d=[]
d_s=""
d_n_s=""
for i in range(r):
	[ar]=np.where(m==e_matrix[i][0])[0]
	[ac]=np.where(m==e_matrix[i][0])[1]
	[br]=np.where(m==e_matrix[i][1])[0]
	[bc]=np.where(m==e_matrix[i][1])[1]

	if ar==br:
		ac=(ac-1)%5
		bc=(bc-1)%5

	elif ac==bc:
		ar=(ar-1)%5
		br=(br-1)%5

	else:
		k=ac
		ac=bc
		bc=k

	d.append([m[ar][ac],m[br][bc]])
	d_s=d_s+m[ar][ac]+m[br][bc]

print('Decryption')
print(d)

z=100
n=len(d_s)
for i in range(n-2):
	if d_s[i]==d_s[i+2]:
		if d_s[i+1]=='x':
			d_n_s=d_s[:i+1]+d_s[i+2:]
			z=1
if z==100:
	d_n_s=d_s
print('original:')
print(d_n_s)

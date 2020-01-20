import numpy as np

s=str(''.join(input("enter string\n").split(" ")))
n=len(s)
while(n%5!=0):
	s=s[:n]+'z'
	n=n+1
s=np.array(list(s))
s_m=s.copy()
j=0
for i in range(0,n,5):
	s_m[j]=s[i+2]
	s_m[j+1]=s[i]
	s_m[j+2]=s[i+3]
	s_m[j+3]=s[i+4]
	s_m[j+4]=s[i+1]
	j=j+5

s_m=''.join(s_m)
print(s_m)
# n=len(s_m)
# for i in range(4,n,5):
# 	s_m=s_m[:i+1]+' '+s_m[i+1:]
# 	print(s_m)

s_m=np.array(list(s_m))
s_m_d=s_m.copy()
j=0
for i in range(0,n,5):
	s_m_d[i+2]=s_m[j]
	s_m_d[i]=s_m[j+1]
	s_m_d[i+3]=s_m[j+2]
	s_m_d[i+4]=s_m[j+3]
	s_m_d[i+1]=s_m[j+4]
	j=j+5

m=''.join(s_m_d)
print(m)


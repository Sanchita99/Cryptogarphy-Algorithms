import numpy as np
import random
n=random.randint(100,100000)
g=random.randint(100,100000)
x=random.randint(100,100000)
y=random.randint(100,100000)

a=(g**x)%n
b=(g**y)%n

k1=(b**x)%n
k2=(a**y)%n

print(k1,k2)

if k1==k2:
	print("Key exchange successfull")
else:
	print("Unsucessfull")

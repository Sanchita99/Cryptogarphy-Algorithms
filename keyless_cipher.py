import numpy as np

num_columns = 4

def encrypt(plain_text):
	L = len(plain_text)
	num_rows = int(np.ceil(len(plain_text)/num_columns))
	res = [['~']*num_columns for i in range(num_rows)]
	k = 0
	for i in range(L):
		ind_i = i//num_columns
		ind_j = k%num_columns
		k+=1
		res[ind_i][ind_j] = plain_text[i]
	res = np.array(res)
	print(res)
	cipher = ''
	for i in range(num_columns):
		sts = ''.join(res[:,i])
		if sts[num_rows-1] == '~':
			cipher+=sts[:-1]
		else: 
			cipher+=sts
	return cipher,res

def decrypt(plain_text,ress):
	L = len(plain_text)
	num_col = int(np.ceil(len(plain_text)/num_columns))
	num_row = num_columns
	res = [['~']*num_col for i in range(num_row)]
	k = 0
	for i in range(L):
		ind_i = i//num_col
		ind_j = k%num_col
		k+=1
		res[ind_i][ind_j] = plain_text[i]
	res = np.array(res)
	print(res)
	cipher = ''
	for i in range(ress.shape[0]):
		sts = ''.join(ress[i,:])
		sts.replace('~','')
		cipher+=sts
	cipher_new = ''
	for ch in cipher:
		if ch =='~':
			break
		else:
			cipher_new+=ch
	return cipher_new
	
name = str(input('Enter a String: '))	
cipher,res = encrypt(name)
print('Encrypted Message: ',cipher)
print('Decrypted Message:',decrypt(cipher,res))



ENC = 0
DEC = 1

def parseKey(key):
	tmp = []
	key = key.upper()
	
	for i, k in enumerate(key):
		tmp.append((i, k))
	
	#Sort tmp by tmp[1]	
	tmp = sorted(tmp, key=lambda x:x[1])
	
	enc_table = {}
	dec_table = {}
	
	#Create table
	for i, r in enumerate(tmp):
		enc_table[r[0]] = i
		dec_table[i] = r[0]	
		
	return enc_table, dec_table
	
def transposition(msg, key, mode):
	msgsize = len(msg)
	keysize = len(key)
	ret = ''
	
	#Add '0' to msg empty value
	filler = ''
	if msgsize % keysize != 0:
		filler = '0' * (keysize - msgsize % keysize)
	
	msg = msg.upper()
	msg += filler
	
	enc_table, dec_table = parseKey(key)
	
	if mode is ENC:
		table = enc_table
	if mode is DEC:
		table = dec_table
	
	
	
	if mode == ENC:
		#what is..?
		buf = ['']*keysize

		for i, c in enumerate(msg):
			col = i % keysize
			index = table[col]
			buf[index] += c
			
		for text in buf:
			ret += text	
	else:
		blocksize = int(msgsize/keysize)
		buf = ['']*keysize
		pos = 0
		
		for i in range(keysize):
			#Slice mssg from pos to pos+blocksize
			text = msg[pos:pos+blocksize]
			index = table[i]
			buf[index] += text
			pos += blocksize
		
		for i in range(blocksize):
			for j in range(keysize):
				if buf[j][i] != '0':
					ret += buf[j][i]
		
	return ret
	
def main():
	key = 'BRAIN'
	msg = 'TREASUREBOXISBURRIEDATTWOHUNDREDFEETTONORTHEASTAWAYFROMYOURHOME'
	print('Original:\t%s' %msg.upper())
	
	ciphertext = transposition(msg, key, ENC)
	print('Ciphered:\t%s' %ciphertext)
	
	deciphertext = transposition(ciphertext, key, DEC)
	print('Deciphered:\t%s' %deciphertext)


if __name__ == '__main__':
	main()













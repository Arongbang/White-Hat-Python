from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
	def __init__(self, keytext, ivtext):
		hash = SHA.new()
		
		hash.update(keytext.encode(utf-8))
		key = hash.digest()
		#key 값을 16바이트(128비트)로 변경
		self.key = key[:16]
		#256 비트 키로 암호화 할 경우
		#self.key = key
		
		hash.update(ivtext.encode(utf-8))
		iv = hash.digest()
		self.iv = iv[:16]
	
	def makeEnabled(self, plaintext):
		fillersize = 0
		textsize = len(plaintext)
		
		if textsize%16 != 0:
			fillersize = 16 - textsize%16
		
		filler = '0' * fillersize
		#‘0’의 갯수가 12일 경우, ‘12##############’
		header = '%d' %(fillersize)
		gap = 16 - len(header)
		header += '#' * gap
		
		return header+plaintext+filler
	
	def enc(self, plaintext):
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		encmsg = aes.encrypt(plaintext)
		
		return encmsg
	
	def dec(self, ciphertext):
		aes = AES.new(self.key, AES.MODE.CBC, self.iv)
		decmsg = aes.decrypt(ciphertext)
		
		
		header = decmsg[:16].decode()
		fillersize = int(header.split('#')[0])
		
		if(fillersize != 0):
			#16 ~ 뒤에서부터 fillersize 제외
			decmsg = decmsg[16:- fillersize]
		else:
			decmsg = decmsg[16:]
			
		return decmsg
		
		
	
	


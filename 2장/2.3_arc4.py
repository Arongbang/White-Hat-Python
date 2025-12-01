from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256 as SHA

class myARC4():
	def __init__(self, keytext):
		#keytext.encode()::: 바이트 문자열로 변환
		self.key = keytext.encode()
	
	def enc(self, plaintext):
		#self.key를 key로 하여 ARC4 객체를생성하고 이를 변수 arc4에 할당
		arc4 = ARC4.new(self.key)
		encmsg = arc4.encrypt(plaintext.encode())
		return encmsg
	
	def dec(self, ciphertext):
		arc4 = ARC4.new(self.key)
		decmsg = arc4.decrypt(ciphertext)
		return decmsg
		
def main():
	keytext = 'samsjang'
	msg = 'I love python'
	
	myCipher = myARC4(keytext)
	ciphered = myCipher.enc(msg)
	deciphered = myCipher.dec(ciphered)
	
	#결과에서 b'는 바이트 객체라는 뜻
	print('ORIGINAL:\t%s' %msg)
	print('CIPHERED:\t%s' %ciphered)
	print('DECIPHERED:\t%s' %deciphered)

main()

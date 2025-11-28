#‘python3x'라는 8자로 된 문장을 3DES CBC 모드로암호화 & 암호화된 문장을 3DES로 복호화하는 소스코드

#3DES 라이브러리 사용을 위해 Psycryptodome에 필요한 모듈을 import
from Crypto.Cipher import DES3
#3DES의 암호키와 초기화 벡터를 사용하기 위해
from Crypto.Hash import SHA256 as SHA

class myDES():
	#클래스 생성자
	#keytext : 3DES 암호키 생성을 위한 문자열
	#ivtext : 초기화 벡터
	def __init__(self, keytext, ivtext):
		#SHA256 객체 생성
		hash = SHA.new()
		#SHA256 해시 갱신(인자로 keytext 사용)
		hash.update(keytext.encode('utf-8'))
		
		#해시 값을 추출하여 변수 key에 할당
		key = hash.digest()
		#Psycrptodome의 3DES 키 크기는 16바이트 혹은 24바이트라서 24바이트만큼 슬라이싱
		#key : 암호키
		self.key = key[:24]
		
		hash.update(ivtext.encode('utf-8'))
		iv = hash.digest()
		#iv : 초기화 벡터
		self.iv = iv[:8]
	
	#!주의!  DES3 객체(des3)는 각각 함수에서 항상 생성해야 함 (전역 X)
	def enc(self, plaintext):
		plaintext = make8String(plaintext)
		
		#DES3.new(‘암호키’, ‘운영 모드’, ‘초기화 벡터’)
		des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
		encmsg = des3.encrypt(plaintext.encode())
		return encmsg
		
	def dec(self, ciphertext):
		des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
		decmsg = des3.decrypt(ciphertext)
		return decmsg

def make8String(msg):
	msglen = len(msg)
	filler = ''
	if msglen%8 != 0:
		filler += '0'*(8 - msglen%8)
	
	msg += filler
	return msg

def main():
	keytext = 'samsjang'
	ivtext = '1234'
	msg = 'python3xab'
	
	myCipher = myDES(keytext, ivtext)
	ciphered = myCipher.enc(msg)
	deciphered = myCipher.dec(ciphered)
	
	#결과에서 b'는 바이트 객체라는 뜻
	print('ORIGINAL:\t%s' %msg)
	print('CIPHERED:\t%s' %ciphered)
	print('DECIPHERED:\t%s' %deciphered)
	
main()

#코드 3.4는 msg에 개인키로 서명한 후 상대방에게 보내는 프로세스

from Cryptodome.Signature import pkcs1_15
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256 as SHA

def readPEM(pemfile):
	h = open(pemfile, 'r')
	key = RSA.importKey(h.read())
	h.close()
	return key

def rsa_sign(msg):
	private_key = readPEM('privatekey.pem')
	public_key = private_key.publickey()
	h = SHA.new(msg)
	#sign() : 개인키로 서명
	signature = pkcs1_15.new(private_key).sign(h)
	return public_key, signature

def rsa_verify(msg, public_key, signature):
	h = SHA.new(msg)
	
	try:
		
		#개인키로 서명이 된 정보와 해시값 일치여부 확인
		pkcs1_15.new(public_key).verify(h, signature)
		print('Authentic')
	except Exception as e:
		#공개키에 의해 확인 불가할 경우 예외 발생
		print(e)
		print('Not Authentic')
	

def main():
	msg = 'My name is samsjang'
	
	public_key, signature = rsa_sign(msg.encode('utf-8'))
	
	rsa_verify(msg.encode('utf-8'), public_key, signature)


main()

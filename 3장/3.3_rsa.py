from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256 as SHA

#PEM파일에 저장된 RSA개인키/공개키를 읽어서 리턴
def readPEM(pemfile):
	h = open(pemfile, 'r')
	key = RSA.importKey(h.read())
	h.close()
	return key
	
#RSA 공개키로 암호화
def rsa_enc(msg):
	public_key = readPEM('publickey.pem')
	cipher = PKCS1_OAEP.new(public_key)
	encdata = cipher.encrypt(msg)
	return encdata

#RSA 개인키로 복호화
def rsa_dec(msg):
	private_key = readPEM('privatekey.pem')
	cipher = PKCS1_OAEP.new(private_key)
	decdata = cipher.decrypt(msg)
	return decdata
	
def main():
	msg = 'samssjang loves python'
	ciphered = rsa_enc(msg.encode('utf-8'))
	print(ciphered)
	deciphered = rsa_dec(ciphered)
	print(deciphered)
	
main()

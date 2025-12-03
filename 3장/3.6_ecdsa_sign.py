from Cryptodome.PublicKey import ECC
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256 as SHA

def readPEM_ECC(pemfile):
	with open(pemfile, 'r') as h:
		key = ECC.importKey(h.read())
	return key


def ecdsa_sign(msg):
	private_key = readPEM_ECC('privkey_eccdsa.pem')
	sha = SHA.new(msg)
	#DSS를 이용하여 전자서명을 위한 객체 생성
	signer = DSS.new(private_key, 'fips-186-3')
	signature = signer.sign(sha)
	return signature
	

def ecdsa_verify(msg, signature):
	public_key = readPEM_ECC('pubkey_ecdsa.pem')
	sha = SHA.new(msg)
	verifier = DSS.new(public_key, 'fips-186-3')
	try:
		verifier.verify(sha, signature)
		print('Authentic')
	except ValueError:
		print('Not Athentic')
	

def main():
	msg = 'My name is samsjang'
	signature = ecdsa_sign(msg.encode('utf-8'))
	ecdsa_verify(msg.encode('utf-8'), signature)
	

main()

#Pycryptodome은 ECDSA를 위해 ECC(Elliptic Curve Cryptography)모듈을 제공
from Cryptodome.PublicKey import ECC

def createPEM_ECDSA():
	key = ECC.generate(curve='P-256')
	with open ('privkey_eccdsa.pem', 'w') as h:
		h.write(key.export_key(format='PEM'))
	
	key = key.public_key()
	with open('pubkey_ecdsa.pem', 'w') as h:
		h.write(key.export_key(format='PEM'))
	
createPEM_ECDSA()

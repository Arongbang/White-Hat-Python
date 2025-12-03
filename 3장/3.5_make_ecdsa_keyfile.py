#Pycryptodome은 ECDSA를 위해 ECC(Elliptic Curve Cryptography)모듈을 제공
from Cryptodome.PublicKey import ECC

def createPEM_ECDSA():
	#ECC.generate() : 타원 곡선 암호를 이용해 개인키를 생성
	#P-256 : 타원 곡선 암호를 만들기 위한 상수들 중 하나 (NIST에서 ’P-256'을 권장)
	key = ECC.generate(curve='P-256')
	with open ('privkey_eccdsa.pem', 'w') as h:
		h.write(key.export_key(format='PEM'))
	
	key = key.public_key()
	with open('pubkey_ecdsa.pem', 'w') as h:
		h.write(key.export_key(format='PEM'))
	
createPEM_ECDSA()

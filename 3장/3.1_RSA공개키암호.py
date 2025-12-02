from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

def rsa_enc(msg):
    # RSA 1024-bit 키 생성
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()

    # 공개키로 암호화
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    print("Encrypted:", encdata)

    # 개인키로 복호화
    cipher = PKCS1_OAEP.new(private_key)
    decdata = cipher.decrypt(encdata)
    print("Decrypted:", decdata)

def main():
    msg = 'samsjang loves python'
    rsa_enc(msg.encode('utf-8'))

main()

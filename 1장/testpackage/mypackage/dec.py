from . import enc

def decryption():
    print('Decryption')

if __name__ == '__main__':
    print('dec.py가 메인임')
    enc.encryption()
    decryption()
else:
    print('dec.py가 다른 모듈에서 임포트 되어 사용됨')

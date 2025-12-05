#hashlib 모듈의 SHA-256을 이용하여 해시값을 구하는 코드
from hashlib import sha256

msg = 'I love Python'
sha = sha256()
sha.update(msg.encode('utf-8'))
ret = sha.hexdigest()
print('SHA-2 SHA-256: ', ret)

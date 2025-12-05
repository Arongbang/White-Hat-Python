#메시지에 대한 MD5 해시값을 16진수로 출력
from hashlib import md5

msg = 'I love Python'
md5 = md5()
md5.update(msg.encode('utf-8'))
ret = md5.hexdigest()
print(ret)

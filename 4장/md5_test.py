from Cryptodome.Hash import md5

msg = 'I love Python'
m = md5()
md5.update(msg.encode('utf-8'))
ret = md5.hexdigest()
print(ret)

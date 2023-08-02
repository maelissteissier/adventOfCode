import hashlib
stri = 'bgvyzdsv'
i = 1
res = hashlib.md5(bytes(stri, 'ascii'))
while res.hexdigest()[0:6] != '000000':
    res = hashlib.md5(bytes(stri+str(i), 'ascii'))
    i = i+12

print(res.hexdigest())
print(i-1)
import time
import hashlib
f = open('Sample.txt','r')
t=''
for line in f:
    t=t+line    

mystring = t

hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())


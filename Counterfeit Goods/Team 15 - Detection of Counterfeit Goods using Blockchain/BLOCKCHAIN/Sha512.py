 
import hashlib
f = open('Sample.txt','r')
t=''
for line in f:
  t=t+line  
str = t
result = hashlib.sha512(str.encode())
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
  

  

import hashlib
f = open('Sample.txt','r')
t=''
for line in f:
    t=t+line    
string = t

encoded=string.encode()
result = hashlib.sha256(encoded)
print("String : ", end ="")
print(string)
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())
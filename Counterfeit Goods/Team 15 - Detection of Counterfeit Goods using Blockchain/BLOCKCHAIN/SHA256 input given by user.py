import hashlib

print("Give Product Details:-", end='')
string= input()

encoded=string.encode()
result = hashlib.sha256(encoded)
print("Hash Value : ", end ="")
print(result)

print("String : ", end ="")
print(string)
print("Hexadecimal equivalent: ",result.hexdigest())
print("Digest Size : ", end ="")
print(result.digest_size)
print("Block Size : ", end ="")
print(result.block_size)
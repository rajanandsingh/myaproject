
import time

from hashlib import sha256, sha512, md5
from random import randint


def pow(
        text):  
    found = False
    nonce = randint(1000, 100000)

    while not found:
        hasht = sha256(
            (text + str(nonce)).encode()).hexdigest()  

        if hasht.startswith("002") or hasht.startswith("003"):  

            found = True
            print("Hash found! " + hasht)
            print("Text and Nonce: " + text + " + " + str(nonce) + "\n")
        nonce = nonce + 1
    


def pown():  
    found = False
    nonce = randint(1000, 100000)
    count = 0
    text = input("Please type in the text: ")
    strnulls = int(input("Type in leading nulls (in decimal! like: 4 = 16 binary nulls): "))
    nulls = makeStringNulls(strnulls)
    try:
        mode = int(input("Choose mode: SHA256 = 1, SHA512 = 2, MD5 = 3 : "))
    except:
        print("ERROR! Only numbers allowed")
        return
    while not found:
        if mode == 1:
           
            hasht = sha256((text + str(nonce)).encode()).hexdigest()
            
            if hasht.startswith(nulls):
                found = True
                print("Hash found! " + str(hasht))
                print("Text and Nonce: " + text + " + " + str(nonce) + " count: " + str(count) + " \n")
            nonce += 1
            count += 1
           
        elif mode == 2:
            hasht = sha512((text + str(nonce)).encode()).hexdigest()
        
            if hasht.startswith(nulls):
                found = True
                print("Hash found! " + str(hasht))
                print("Text and Nonce: " + text + " + " + str(nonce) + " count: " + str(count) + "\n")
            nonce += 1
            count += 1

        elif mode == 3:
            hasht = md5((text + str(nonce)).encode()).hexdigest()
    
            if hasht.startswith(nulls):
                found = True
                print("Hash found! " + str(hasht))
                print("Text and Nonce: " + text + " + " + str(nonce) + " count: " + str(count) + "\n")
            nonce += 1
            count += 1

        else:
            print("ERROR! Wrong Mode!")
            found = True


def makeStringNulls(nulls):
    strnulls = ""
    for i in range(nulls):
        strnulls += "0"
    return strnulls


def start():
    starti = False

    while not starti:
        try:  
            startinput = int(input("Start Proof of Work? 1= Yes, 9= No: "))
            if startinput == 1:
                pown()
            elif startinput == 9:
                print("Stopped!")
                starti = True
            else:
                print("ERROR! Wrong entry!")
        except:
            print("ERROR!")


start()


def proof(hasht, text):  
    if hasht == sha256(text.encode()).hexdigest():
        print("Hash correct! " + hasht)
    else:
        print("Hash incorrect! " + hasht)


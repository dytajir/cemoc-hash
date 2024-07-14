import os
os.system("clear")

while True:

 print("===============================================")
 print("[1]-hash checker [2]-hash length [3]-hash type ")
 print("===============================================")

 choose = input("Enter your option : ")
 
 if choose == "1":
    print("This option for hash checker")
    hash1 = input("Enter hash [1] : ")
    hash2 = input("Enter hash [2] : ")
    if hash1 == hash2 :
        print("the hash is clean")
    else: 
        print("the hash is virus")

 if choose == "2":
    print("This option for length hash")
    length = input("Enter your hash : ")
    print("Length hash is : ", len(length))

 if choose == "3":
    print("This option for know hash type")
    hash = input("Enter the hash : ")
    length = len(hash)
    if length == 32:
        print("the hash is [MD5]")
    if length == 40:
        print("the hash is [sha1]")
    if length == 64:        
            print("the hash is [ sha256]")
            

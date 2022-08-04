import random 
import json  
import os

cipherkey = {}

def cipher_generator():

    encrypt = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0124356789!#$%&'()+*,-./:;<=>?@[]^_`{|}~ ")
    original = encrypt.copy()
    random.shuffle(encrypt)
    for i in range(len(encrypt)):
        cipherkey[str(original[i])] = str(encrypt[i])

    ciphername = input("What do you want to call this cipher")

    f = open(f"cipherkeys\{ciphername}.json", "w")
    json.dump(cipherkey, f)
    f.close()
    os.system('cls')
    print(f"{ciphername} has been successfully created!")
    print(f"Cipher Key: {cipherkey}")
    





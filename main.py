import Message_Decipherer
import Cipher_Generator
import Message_Encoder
from os import system

while True:

    prompt = input("Do you want to generate a cipher, encode a message, or decipher one? ")

    if prompt == "generate":
        Cipher_Generator.cipher_generator()
        system('pause && cls')
        continue
    elif prompt == "encode":
        Message_Encoder.message_encoder()
        system('pause && cls')
        continue
    elif prompt == "decipher":
        Message_Decipherer.message_decipherer()
        system('pause && cls')
        continue
    elif prompt == "q":
        break
 
import json
from tkinter import filedialog
import re
pattern="[A-Z]"

def message_decipherer():
    deciphered_message = ""
    m = input("Enter the text you want to decipher ")
    filepath = filedialog.askopenfilename(initialdir="Cipher\\cipherkeys", 
    title="Choose a cipher key.",
    filetypes = (("json files", "*.json"),("all files", "*.*")))

    f = open(filepath, "r")
    cipherkey = json.load(f)
    inv_map = {v: k for k, v in cipherkey.items()}
    l = list(m)

    for words in l:
        characterlist = list(words)
        for i in characterlist:
            deciphered_message += inv_map[i]
    print(deciphered_message)
    f.close()
import json 
from tkinter import filedialog

def message_encoder():
    filepath = filedialog.askopenfilename(initialdir="\\Cipher", 
    title="Choose a cipher key.",
    filetypes = (("json files", "*.json"),("all files", "*.*")))

    f = open(filepath, "r")
    cipherkey = json.load(f)

    encoded_message = ""
    m = input("Enter the Message you want to encode")
    l = list(m)

    for words in l:
        characterlist = list(words)
        for i in characterlist:
            encoded_message += cipherkey[i]

    f.close()
    print(encoded_message)
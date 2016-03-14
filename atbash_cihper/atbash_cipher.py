from string import ascii_lowercase
ascii_reversed = ascii_lowercase[:-1]
import string 

def atbash(text):
    alphabet = string.ascii_lowercase
    cyphered = [c if c not in alphabet else alphabet[-(alphabet.index(c) + 1)] for c in text]
    return "".join(cyphered)

if __name__ == "__main__":
    for text in ["foobar", "wizard", "/r/dailyprogrammer", "gsrh rh zm vcznkov lu gsv zgyzhs xrksvi"]:
        print(text + ":", atbash(text))

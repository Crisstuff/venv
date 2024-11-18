from Crypto. Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

iv = get_random_bytes(16)

# Denne er for å starte krypteringen av meldingen 
def pad(s): # s kunne også het stringIn
    padding = 16 - len(s) % 16
    return s + padding * chr(padding)

# Denne er for å de kryptere koden
def unpad(s):
    padding_verdi = s[-1]
    return s[:-padding_verdi]

# første
melding = "dette er en hemmelig melding"
melding = pad(melding).encode()
cipher = AES.new(key, AES.MODE_CBC, iv)
kryptogram = cipher. encrypt(melding)
print("kryptogram:", kryptogram)


# neste
cipher = AES.new(key, AES.MODE_CBC, iv)
dekryptert = cipher.decrypt(kryptogram)
dekryptert = unpad(dekryptert).decode()
print("dekryptert melding:", dekryptert)
from Crypto. Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

iv = get_random_bytes(16)

def pad(s):
    padding = 16 - len(s) % 16
    return s + padding * chr(padding)

def unpad(s):
    padding_verdi = s[-1]
    return s[:-padding_verdi]

#første
melding = "dette er en hemmelig melding"
melding = pad(melding).encode()
cipher = AES.new(key, AES.MODE_CBC, iv)
kryptogram = cipher. encrypt(melding)
print("kryptert melding:", kryptogram)


# neste
cipher = AES.new(key, AES.MODE_CBC, iv)
dekryptert = cipher.decrypt(kryptogram)
dekryptert = unpad(dekryptert).decode()
print("dekryptert melding:", dekryptert)
print("dette er den krypterte meldingen:", melding)

# For & teste om denne meldi

# Hva som skjer hvis man prøver å unpad en tekst som ikke er korrekt paddet?
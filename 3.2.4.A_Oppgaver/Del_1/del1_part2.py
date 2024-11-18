#   Feilhåndtering ved dekryptering 
#   Modifiser koden slik at den håndterer tilfeller der IV eller nøkkel er feil. Hva skjer hvis du endrer 
#   én byte i IV eller nøkkel under dekryptering? Legg til try-except for å fange opp feil. 

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

# kryptering
try:
    melding = "dette er en hemmelig melding"
    melding = pad(melding).encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    kryptogram = cipher. encrypt(melding)
    print("kryptogram:", kryptogram)
except Exception as e:
    print(" Kryptering Error ")
    print(f"Feil: {e}")


# dekryptering
try:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dekryptert = cipher.decrypt(kryptogram)
    dekryptert = unpad(dekryptert).decode()
    print("dekryptert melding:", dekryptert)
except ValueError as e:
    print(" Dekryptering Error: Sannsynligvis feil med nøkkel eller IV. ")
    print(f"Feil: {e}")
    
except Exception as e:
    print("En ukent feil oppstod under dekryptering ")
    print(f"Feil: {e}")

# Dette programmet håndterer 

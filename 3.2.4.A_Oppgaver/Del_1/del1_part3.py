#   Feilhåndtering ved dekryptering 
#   Modifiser koden slik at den håndterer tilfeller der IV eller nøkkel er feil. Hva skjer hvis du endrer 
#   én byte i IV eller nøkkel under dekryptering? Legg til try-except for å fange opp feil. 

from Crypto. Cipher import AES
from Crypto.Random import get_random_bytes

bin_fil = "Del_1/bin.txt"

key = get_random_bytes(16)
iv = get_random_bytes(16)

# Denne er for å starte krypteringen av meldingen 
def pad(s): # s kunne også het stringIn
    padding = 16 - len(s) % 16
    return s + padding * chr(padding)

# kryptering
def kryptering(key, iv):
    try:
        melding = "dette er en hemmelig melding"
        melding = pad(melding).encode()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        kryptogram = cipher.encrypt(melding)
        with open(bin_fil, "w") as fil:
            fil.write(kryptogram.hex())
            print("Kryptogrammet er overført.")
    except Exception as e:
        print("Kryptering Error")
        print(f"Feil: {e}")
        return None





# Dette programmet håndterer 
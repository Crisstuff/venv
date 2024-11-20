import hashlib# Oppgave1 
# Oppgave2: Valgt SHA-256
txt_fil = "3.2.5.A_Ovelsesoppgaver/passord_hash.txt"

# Oppgave3: Bruker skriver inn passordet som skal hashes
passord = input("Skriv inn passordet du ønsker å hashe: ")

# Oppgave4: Hashing av passordet
hash_objekt = hashlib.sha256(passord.encode())  # Legg merke til parentesene etter encode
hash_hex = hash_objekt.hexdigest()

# Oppgave5: Skriver hashen til filen
with open(txt_fil, "w") as fil:
    fil.write(hash_hex)
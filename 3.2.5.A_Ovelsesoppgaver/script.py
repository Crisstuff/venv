import hashlib # Oppgave1 
from passord_sjekker import p_sjekker
# Oppgave2 så valgte jeg SHA-256

passord = input("skriv inn passordet du ønsker å hashe: ")#Oppgave 3 vaøgte passord

#Oppgave4
hash_objekt = hashlib.sha256(passord.encode)
hash_hex = hash_objekt.hexdigest()

with open ("passord_hash.txt", "w") as fil:# Oppgave5 
    fil.write(hash_hex)
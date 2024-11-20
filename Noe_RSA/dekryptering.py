from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
import base64 

 

#Henter inn privat nøkkel 
privateFile = input("Filnavn til din private nøkkel: ") 
with open (privateFile,"rb") as file: 
private_key = RSA.import_key(file.read()) 

#Initialiser RSA cipher for dekryptering 
cipherRsa = PKCS1_OAEP.new(private_key) 

#Leser inn kryptert melding, og dekrypterer den 
kryptert_melding_b64 = input("Skriv inn den krypterte meldingen: ") 
kryptert_melding = base64.b64decode(kryptert_melding_b64) 
melding = cipherRsa.decrypt(kryptert_melding) 

print(melding.decode())  
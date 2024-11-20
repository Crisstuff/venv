
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
import base64 

#hente offentlig nøkkel til mottaker 
pubFile = input("Public key filnavn: ") 
with open(pubFile,"rb") as file: 
public_key = RSA.import_key(file.read()) 

#Initialiserer RSA cipher for kryptering 
cipherRsa = PKCS1_OAEP.new(public_key) 

#Ta i mot melding som bytes, og krypter 
melding = input("Skriv inn melding som skal krypteres: ").encode() 
kryptert_melding = cipherRsa.encrypt(melding) 

print(base64.b64encode(kryptert_melding).decode()) 
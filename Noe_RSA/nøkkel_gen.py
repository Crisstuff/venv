from Crypto.PublicKey import RSA 

#Generer RSA nøkkelpar 

key = RSA.generate(2048) 

 

#Lagre privat nøkkel til fil 

private_key = key.export_key() 

with open("private.pem", "wb") as file: 

    file.write(private_key) 

 

#Lagre offentlig nøkkel til fil 

public_key = key.publickey().export_key() 

with open("public.pem","wb") as file: 

    file.write(public_key) 

 

print("Nøkler generert!") 
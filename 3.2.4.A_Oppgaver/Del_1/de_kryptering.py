#!/bin/bash
from del1_part3 import dekrykryptering, unpad, key, iv
from Crypto. Cipher import AES
from Crypto.Random import get_random_bytes


# dekryptering
def dekrykryptering(kryptogram,iv):
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

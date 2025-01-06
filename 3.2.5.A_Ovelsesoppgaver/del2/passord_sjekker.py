from  import txt_fil, hash_hex, passord

def passord_sjekker(): 
    with open (txt_fil,"r") as fil: 
        save_hash = fil.read(txt_fil)
        test_hash = passord
        print("Passordet er riktig")
    if ValueError(print"Error")

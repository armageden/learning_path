# Home Task 5: Key Generator
def key_generator(*names):
    ecrpt_keys=[]
    for name in names:
        ecrpt_key=chr(ord(name[0])+32)
        for i in name[1:-1]:
            ecrpt_key+=str(ord(i))
        ecrpt_key+=chr(ord(name[-1])-32)    
        ecrpt_keys.append(ecrpt_key)
        
    print(ecrpt_keys)
key_list = key_generator ("Alex", "Bob", "Trudy")


            
                
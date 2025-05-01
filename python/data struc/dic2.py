# Home Task 1: Hospital Fee
def hospital_fee(**names):
    high,high_payer=0,[]
    for name, fee in names.items():
        if fee==high:
           high_payer.append(name)
            
        elif fee >high:
            high =fee
            high_payer=[name] 

    return high, high_payer        
max_amount, max_payer = hospital_fee(Neymar=1000, Dembele=600, Reus=500, Bale=1000)
cr=", ".join(max_payer)+"."
print(f"Highest fee was {max_amount} tk which was paid by {cr}")

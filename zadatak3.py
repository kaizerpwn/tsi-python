# Svaki broj od 1 do 1000 koji je dijeljiv sa sobom i sa jedinicom
def primarni_broj(broj):
    for i in range(2, broj): 
        if i > 1:
            if broj % i == 0:
                print(f"{i} je dijeljiv sa 1 ili sa samim sobom")
                
primarni_broj(51)
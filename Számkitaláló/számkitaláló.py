import random
print("Üdvözöllek! Gondoltam egy számra 1 és 100 között! Az a feladatod hogy kitaláld! De figyelj oda, mert csak 10 próbálkozásod van!")


random_num = random.randint(1, 100)

prób_szám = 0

while True:
    prób_szám+=1
    tipp = int(input("Kérlek add meg a tipped: "))
    
    if tipp == random_num:
        print("Ügyes vagy! Sikerült kitalálnod a számot!")
        break
    elif tipp<random_num:
        print("Nagyobb számra gondoltam! Hátramaradt próbálkozások száma: ",prób_szám)
        if prób_szám==10:
            print("Sajnos kifogytál a próbálkozásokból!")
            break
    else:
        print("Kissebb számra gondoltam! Hátramaradt próbálkozások száma: ",prób_szám)
        if prób_szám==10:
            print("Sajnos kifogytál a próbálkozásokból! Legközelebb ügyesebb leszel!")
            break

    



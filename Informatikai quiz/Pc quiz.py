játszol = str(input("Szeretnél játszani?(igen/nem): "))
pontok = 0

if játszol == "igen":
    print("Rendben. A feladatod az hogy fel fogok tenni számodra rövidítéseket, neked pedig ki kell írnod a teljes angol kifejezését.")
    válasz = str(input("Mit rövidít a GPU kifejezés?"))
    if válasz.lower() == "graphics processing unit":
        print("A válaszod helyes :D")
        pontok+=1
    else:
        print("Sajnálom, de a válaszod helytelen")
    válasz = str(input("Mit rövidít a CPU kifejezés?"))
    if válasz.lower() == "central processing unit":
        print("A válaszod helyes :D")
        pontok+=1
    else:
        print("Sajnálom, de a válaszod helytelen")
    válasz = str(input("Mit rövidít a RAM kifejezés?"))
    if válasz.lower() == "random acces memory":
        print("A válaszod helyes :D")
        pontok+=1
    else:
        print("Sajnálom, de a válaszod helytelen")
    válasz = str(input("Mit rövidít a PSU kifejezés?"))
    if válasz.lower() == "power supply":
        print("A válaszod helyes :D")
        pontok+=1
    else:
        print("Sajnálom, de a válaszod helytelen")
    válasz = str(input("Mit rövidít a ROM kifejezés?"))
    if válasz.lower() == "read only memory":
        print("A válaszod helyes :D")
        pontok+=1
    else:
        print("Sajnálom, de a válaszod helytelen")
    if pontok==5 or 4:
        print("Ügyes vagy, sikerült kitalálnod",pontok,"rövidítést!")
    elif pontok==3 or 2:
        print("Nem rossz, de lehetne jobb is!", pontok,"pontot értél el!")
    elif pontok==1 or 0:
        print("Tanuld csak még egy kicsit azt az informatikát :D. Pontjaid száma: ",pontok)
elif játszol == "nem":
    print("Na sebaj, azért köszi hogy elindítottál :D. Szia :D.")

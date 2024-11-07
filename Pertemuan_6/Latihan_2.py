# Nama : Zaky Rizzan Zain
# NIM : 2403342
# Kelas : 1B

Bilangan = int(input("Masukkan Bilangan: "))
if (Bilangan % 2 == 0):
    if(Bilangan > 0):
        print(f"Bilangan {Bilangan} adalah bilangan Genap positif")
    elif(Bilangan == 0):
        print(f"Bilangan {Bilangan} adalah Nol, Bukan Positif atau Negatif")
    else:
        print(f"Bilangan {Bilangan} adalah bilangan Genap negatif")
else:
    if(Bilangan > 0):
        print(f"Bilangan {Bilangan} adalah bilangan Ganjil positif")
    elif(Bilangan == 0):
        print(f"Bilangan {Bilangan} adalah Nol")
    else:
        print(f"Bilangan {Bilangan} adalah bilangan Ganjil negatif")
        


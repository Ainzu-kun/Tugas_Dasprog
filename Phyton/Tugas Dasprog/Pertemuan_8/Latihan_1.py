# Nama = Zaky Rizzan Zain
# NIM = 2403342
# Kelas = 1B

# Menghitung voleme tabung yang dibuat dalam sebuah fungsi
def hitung_voleme_tabung(r,h):
    if(r%7 == 0):
        print("Merupakan Kelipatan 7")
        volume = (22/7) * (r**2) * h
    else:
        volume = 3.14 * (r**2) * h
    return volume

r = int(input("Masukkan Jari-jari: "))
h = int(input("Masukkan Tinggi: "))

print("Volume tabung adalah",(hitung_voleme_tabung(r,h)))

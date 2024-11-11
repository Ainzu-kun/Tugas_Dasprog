# Nama      : Ainz Sama
# NIM       : 2403342
# Kelas     : RPL 1B
# Matkul    : Dasar Pemrograman

print("Program Kalkulator Jadul")
a = int(input("Masukkan Bilangan Ke-1 : "))
b = int(input("Masukkan Bilangan Ke-1 : "))
c = int(input("Masukkan Bilangan Ke-1 : "))

hasil = a + b + c
print(f"Hasil dari penjumlahan {a} + {b} + {c} adalah = {hasil}")


# UPDATE

import math

class Kalkulator:
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            return "Error: Pembagi tidak boleh nol"
        return a / b

    def modulus(self, a, b):
        return a % b

    def pangkat(self, a, b):
        return a ** b

    def akar(self, a):
        if a < 0:
            return "Error: Tidak bisa mengambil akar dari bilangan negatif"
        return math.sqrt(a)

    def nilai_maksimum(self, list_bilangan):
        if not list_bilangan:
            return "Error: List kosong"
        return max(list_bilangan)

    def nilai_minimum(self, list_bilangan):
        if not list_bilangan:
            return "Error: List kosong"
        return min(list_bilangan)

# Contoh penggunaan
if __name__ == "__main__":
    kalkulator = Kalkulator()

    # Operasi dasar
    print("Penjumlahan:", kalkulator.tambah(10, 5))
    print("Pengurangan:", kalkulator.kurang(10, 5))
    print("Perkalian:", kalkulator.kali(10, 5))
    print("Pembagian:", kalkulator.bagi(10, 5))
    print("Modulus:", kalkulator.modulus(10, 3))
    print("Pangkat:", kalkulator.pangkat(2, 3))
    print("Akar:", kalkulator.akar(16))

    # Mencari nilai maksimum dan minimum
    list_bilangan = [10, 20, 5, 40, 15]
    print("Nilai maksimum:", kalkulator.nilai_maksimum(list_bilangan))
    print("Nilai minimum:", kalkulator.nilai_minimum(list_bilangan))




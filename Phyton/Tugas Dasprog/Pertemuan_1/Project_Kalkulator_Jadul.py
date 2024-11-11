# Nama      : Ainz Sama
# NIM       : 2403342
# Kelas     : RPL 1B
# Matkul    : Dasar Pemrograman

# print("Program Kalkulator Jadul")
# a = int(input("Masukkan Bilangan Ke-1 : "))
# b = int(input("Masukkan Bilangan Ke-1 : "))
# c = int(input("Masukkan Bilangan Ke-1 : "))

# hasil = a + b + c
# print(f"Hasil dari penjumlahan {a} + {b} + {c} adalah = {hasil}")


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

def main():
    kalkulator = Kalkulator()

    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Modulus")
        print("6. Pangkat")
        print("7. Akar")
        print("8. Nilai Maksimum dari List")
        print("9. Nilai Minimum dari List")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-9): ")

        if pilihan == '0':
            print("Terima kasih telah menggunakan kalkulator.")
            break

        if pilihan in ['1', '2', '3', '4', '5', '6']:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))

            if pilihan == '1':
                print("Hasil Penjumlahan:", kalkulator.tambah(a, b))
            elif pilihan == '2':
                print("Hasil Pengurangan:", kalkulator.kurang(a, b))
            elif pilihan == '3':
                print("Hasil Perkalian:", kalkulator.kali(a, b))
            elif pilihan == '4':
                print("Hasil Pembagian:", kalkulator.bagi(a, b))
            elif pilihan == '5':
                print("Hasil Modulus:", kalkulator.modulus(a, b))
            elif pilihan == '6':
                print("Hasil Pangkat:", kalkulator.pangkat(a, b))

        elif pilihan == '7':
            a = float(input("Masukkan bilangan untuk akar: "))
            print("Hasil Akar:", kalkulator.akar(a))

        elif pilihan in ['8', '9']:
            list_bilangan = input("Masukkan list bilangan (pisahkan dengan koma): ")
            list_bilangan = [float(x) for x in list_bilangan.split(",")]

            if pilihan == '8':
                print("Nilai Maksimum:", kalkulator.nilai_maksimum(list_bilangan))
            elif pilihan == '9':
                print("Nilai Minimum:", kalkulator.nilai_minimum(list_bilangan))

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
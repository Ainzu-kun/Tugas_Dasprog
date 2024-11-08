# Nama      : Ainz Sama
# NIM       : 2403342
# Kelas     : RPL 1B
# Matkul    : Dasar Pemrograman

# buat kode kalkulator yang dapat melakukan operasi penjumlahan, pengurangan, perkalian, pembagian, akar , pangkat?

import math

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Akar (√)")
    print("6. Pangkat (^)")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

    if pilihan in ['1', '2', '3', '4', '6']:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == '2':
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif pilihan == '3':
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    elif pilihan == '5':
        angka = float(input("Masukkan angka untuk akar: "))
        hasil = math.sqrt(angka)
        print(f"Hasil: √{angka} = {hasil}")
    elif pilihan == '6':
        hasil = math.pow(angka1, angka2)
        print(f"Hasil: {angka1} ^ {angka2} = {hasil}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    kalkulator()
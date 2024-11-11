# Nama : Zaky Rizzan Zain
# NIM : 2403342
# Kelas : 1B


"""Buatlah sebuah program untuk melakukan pengecekan nilai yang di input oleh
user, apabila nilai >= 90 maka bernilai A, apabila 90 < nilai >= 80 bernilai B,
apabila 80 < nilai <= 70 maka bernilai C, dan apabila nilai < 70 dari maka nilainya
D"""

Nilai = int(input("Masukkan Nilainya Boss: "))

if (Nilai >= 90):
    print("Grade A")
elif( Nilai <90 and Nilai >= 80):
    print("Grade B")
elif (Nilai < 80 and Nilai >= 70):
    print("Grade C")
else:
    print("Grade D")

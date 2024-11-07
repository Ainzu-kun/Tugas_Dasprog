"""PERULANGAN"""
# FOR
# for index in range(Jumlah_Perulangan)
    # eksekusi program ini sebanyak jumlah_Perulangan
# eksekusi program ini sekali

# contoh
jumlah_perulangan = 5
for index in range(jumlah_perulangan):
    print("Halo, saya akan mengulang ini sebanyak", jumlah_perulangan,)

for i in "Python":
    print(f"Huruf: {i}")

# Print dari List
buah = ["Apel", "Belimbing", "ceri", "Durian"]

for i in buah:
    print(f"Buah : {i}")

# Pakai Range
buah = ["Apel", "Belimbing", "ceri", "Durian"]
for i in range (len(buah)):
    print(f"Buah : {buah[i]}")


"""Perulangan"""
# While
# while(kondisi):
    # Jalankan  program ini selama kondisi bernilai True
# jalankan perintah ini hanya sekali    

angka = 0
while (angka < 8):
    print(f"Angka Sekarang:  {angka}")
    angka +=1
    
    
# Buatlah program dengan looping sebanyak n = 10, setelah itu hitung jumlah dari angka tersebut output nya: 55?

n  = 10
jumlah = 0
for angka in range(1, n  + 1):
    jumlah += angka
print(f"Jumlah dari angka 1 sampai {n} adalah {jumlah}")

# Break
# break digunakan untuk menghentikan perulangan saat kondisi tertentu terp

# Continue
# continue digunakan untuk melompati perulangan saat kondisi tertentu terp
angka = [1,2,3,4,5]
for i in angka:
    if i == 3:
        continue
    print(f"Angka : {i}")


# Range
# range(start, stop, step)
# start: angka awal
# stop: angka akhir
# step: beda antara angka awal dan akhir

for i in range(2,6):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range (10, 0,-1):
    print(i)
    


# Nested Loops
# Nested Loops adalah perulangan yang ada didalam perulangan lainnya
# Contoh:

buah =  ["Apel", "Mangga", "Jeruk"]
angka =  [1,2,3]

for i in buah:
    for  j in angka:
        print(i)
        print(j)

# If Else di Loop
# If Else di Loop digunakan untuk mengecek kondisi tertentu dan melakukan perul



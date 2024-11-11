# NAMA      : Zaky Rizzan Zain
# NIM       : 2403342
# Tugas 1
# Tanggal    : 23 Oktober 2024

# Buatlah program dengan looping sebanyak n = 10, setelah itu hitung jumlah dari angka tersebut 
# output nya: 55

# Inisialisasi Variable
n  = 10
for i in range(1,n):
   n += i
   print(f"Penjumlahan ke {i} adalah {n-i} + {i} = {n} ")
   
# Cara Kedua (Menggunakan While dan Disimpan Dalam List)
#  By Rafi
# n = 0
# List_Angka =  []

# while(List_Angka <= 10):
#     print(n)
#     List_Angka.append(n)
#     n += 1
    
# jumlah = sum(List_Angka)
# print(f" Hasil penjumlahan dari {List_Angka} adalah {jumlah}")

# Lah Kok Error?

# Cara Tiga
n = 10
x = 0
for i in range(1,11):
    angka = x
    x += i
    print(f"Penjumlahan {x-i} + {i} adalah {x}")
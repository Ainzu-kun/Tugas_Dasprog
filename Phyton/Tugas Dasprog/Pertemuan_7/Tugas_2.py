# NAMA      : Zaky Rizzan Zain
# NIM       : 2403342
# Tugas 2
# Tanggal    : 23 Oktober 2024

# Buatlah sebuah program yang meminta pengguna memasukkan angka-angka berturut-turut.
# Program akan menghitung total angka yang dimasukkan pengguna hingga pengguna memasukkan angka negatif?

Total = 0

# Mulai Loop
while True:
    # Input Mas
    UserInput = int(input("Masukkan Angkanya (Akan  Berhenti Jika Masukkan Angka Negatif): "))

    
    # Memeriksa Angka Negatif
    if UserInput < 0 :
        print("Angka Yang Anda Masukkan Negatif, Program Akan Mulai Menghitung")
        break
    
    # Menambahkan angka ke total
    Total += UserInput
    
# Menampilkan Hasil
print("Total angka yang dimasukkan adalah: ", Total)

    
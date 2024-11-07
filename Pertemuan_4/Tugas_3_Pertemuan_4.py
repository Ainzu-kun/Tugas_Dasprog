# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro


Mahasiswa_Info = {
    "Alice" : {"Age" : 20, "Major" : "Computer Science"},
    "Bob" : {"Age" : 21, "Major" : "Mathematics"},
    "Charlie" : {"Age" : 19, "Major" : "Physics"},
}

# Meminta Input dari user
Search_Nama = input("Masukkan Nama Mahasiswa : ")
# Menggunakan Get untuk akses item di Dictionary
Data_Mahasiswa = Mahasiswa_Info.get(Search_Nama)
# Menampilkan data mahasiswa yang dicari dari Dictionary
print(f"Umur {Search_Nama} adalah {Data_Mahasiswa ["Age"]} dan Prodinya adalah {Data_Mahasiswa ["Major"]}")


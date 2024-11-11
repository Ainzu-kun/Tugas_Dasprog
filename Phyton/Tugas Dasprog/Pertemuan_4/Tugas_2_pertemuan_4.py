# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro

Students = {
    "Alice" : "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics"
}

X = list(Students.values()).count("Computer Science")
Y = list(Students.values()).count("Mathematics")
Z = list(Students.values()).count("Physics")

print("Prodi Computer Science Sebanyak : ", X)
print("Prodi Mathematics Sebanyak : ", Y)
print("Prodi Physics Sebanyak : ", Z)

# ============================================Batas Tugas ===========================================

# Cara lain
List_Jurusan = list(Students.values())#Merubah semua Set Student menjadi List

print("Prodi Computer Science Sebanyak : ", List_Jurusan.count("Computer Science"))
print("Prodi Computer Science Sebanyak : ", List_Jurusan.count("Mathematics"))
print("Prodi Computer Science Sebanyak : ", List_Jurusan.count("Physics"))

# Input
Nama_Prodi = input("Masukkan Nama Prodi : ")
print(f"Prodi {Nama_Prodi} Ada Sebanyak :", List_Jurusan.count(Nama_Prodi))




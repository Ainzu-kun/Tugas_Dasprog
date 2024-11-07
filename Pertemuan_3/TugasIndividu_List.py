# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro


# List Nilai Mahasiswa
Nilai_Mahasiswa = [88,75,63,97,82,74,91,80,81,63]

# Nilai Max
Nilai_Maksimal = max(Nilai_Mahasiswa)
print(f"Nilai Maksimal Mahasiswa Adalah :",Nilai_Maksimal)

# Nilai Min
Nilai_Minimal = min(Nilai_Mahasiswa)
print(f"Nilai Minimal Mahasiswa Adalah :",Nilai_Minimal)

# Nilai AVG
Nilai_AVG = sum(Nilai_Mahasiswa)/len(Nilai_Mahasiswa)
print(f"Nilai Rata-Rata Mahasiswa Adalah :", Nilai_AVG)

# Nilai Terbesar Kedua
Urutan_Nilai_Mahasiswa = Nilai_Mahasiswa.sort()
Panjang_Nilai_Mahasiswa = len(Nilai_Mahasiswa) - 2
# print(Nilai_Mahasiswa)
# print(Panjang_Nilai_Mahasiswa)
print(Nilai_Mahasiswa[Panjang_Nilai_Mahasiswa])





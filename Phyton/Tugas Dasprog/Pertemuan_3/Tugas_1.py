# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro
# append, Insert, Pop

X = ("Jajang", "Nabil", "Ambatukam", "Rafi", "Ikhsan")

# ===Merubah Tuple Menjadi List===

a = list(X)#Mengubah tupple menjadi list
a.append("Mulyono")#Menambah nilai di akhir urutan
a.insert(1,"Mega")#menambah nilai di urutan tertentu
a.pop(4)#menghapus nilai tertentu

# ===Mengubah List to Tuple====
X = tuple(a)#mengubah list menjadi tuple
print(X)



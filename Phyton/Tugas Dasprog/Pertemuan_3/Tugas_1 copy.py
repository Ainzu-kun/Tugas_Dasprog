# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro
# append, Insert, Pop

X = ("Jajang", "Nabil", "Ambatukam", "Rafi", "Ikhsan")

# ===Merubah Tuple Menjadi List===

a = list(X)#Mengubah tupple menjadi list
a.append("Mulyono")#Menambah nilai di akhir urutan

#===========================================

Y = ("Jajang", "Nabil", "Ambatukam", "Rafi", "Ikhsan")
b = list(Y)

b.insert(1,"Mega")#menambah nilai di urutan tertentu

#===============================================
Z = ("Jajang", "Nabil", "Ambatukam", "Rafi", "Ikhsan")
c = list(Z)
c.pop(4)#menghapus nilai tertentu


# ===Mengubah List to Tuple====
X = tuple(a)#mengubah list menjadi tuple
Y = tuple(b)
Z = tuple(c)
print(X)
print(Y)
print(Z)





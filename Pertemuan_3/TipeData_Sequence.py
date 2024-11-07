#===Zaky RZ | RPL 1A/1B | Daspro Pertemuan 3 | 18-09-2024
# Tipe data list
# Digunakan untuk menyimpan beberapa item dalam 1 variable
# dan dapat di modifikasi
# dibuat dengan tanda kurung siku "[]"
# Pakai Fingsi len

a = ["Apel", "Jeruk", "Ceri", "Durian", "Apel"]
print(len(a))
print(a[1:3])

# Append (Mengubah item diakhir list)
b = ["Apel", "Jeruk", "Ceri", "Durian", "Apel"]
b.append("Razz Berry")
print(b)
print(type(len(b))) #Cara Cek type data len
print(b[2:6])
print(b[1][4])#Cari kata dari list "Jeruk"
print(b[1],b[3]) #Cari 2 kata berjauhan dari list

# Insert 
# a.insert(No index,"Semangka"), menambah nilai di index tertentu

# mengganti index tertentu pada list yang sudah ada
c = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan"]
c[1] = "Nugi" 

print(c)
 
#  Mengganti item di index tertentu

d = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan"]
d.insert(1, "Haikal")
print(d)

# menghapus item pada list dengan pop
e = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan"]
e.pop(4)
print(e)

# menambah item di list dari list lainnya dengan extend
f = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan"]
g = ["Jajang", "Inoen"]
# sebelum extend
print(f)
# Seteleh extend
f.extend(g)
print(f)

# mengurutkan item sesuai abjad dengan sort
h = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan"]
h.sort()
print(h)

# Remove
i = ["Rafi", "Nabil", "Ikhsan", "Shina", "Dede Zidan","Rafi"]
i.remove("Rafi") #Mulai baca dari awal
print(i) # Makanya rafi diakhir tetap ada

# revers untuk membalikan urutan item
# count untuk menghitung panjang
# len menghitung panjang
# clear menghapus semuanya



"""Tipe data Tupple"""
"""Tipe data mirip list 
tapi tak bisa diubah"""

A = ("Aple", "Jeruk", "Ceri", "Durian", "Apel")
print(A[1:3]) #Format <data  terakhir

# ====mengubah data tuple ke list=====
A = ("Aple", "Jeruk", "Ceri", "Durian", "Apel")
x = list(A) # Var X mengubah Var A dari Tuple ke List
x[1]="melon" #Mengganti index 1 pada variabel A menjadi melon
A = tuple(x) #Mengubah list  x menjadi Tuple

print(A)#Output

#setiap kita mengubah data pada tuple harus diubah ke list
#baru ditambah fungsi, fungsinya sama seperti fungsi list

A = ("Aple", "Jeruk", "Ceri", "Durian", "Apel")
x = list(A)
# x[1] = "melon"
x.pop(3)
A = tuple(x)

print(A)


# =============================================================


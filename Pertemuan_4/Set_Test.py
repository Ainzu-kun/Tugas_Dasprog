# Set ==============================================================================================
"""Set adalah salah salah satu tipe data
yang digunakan untuk menyimpan variable tunggal"""
# Set ketika di print akan mengacak item di dalam list, karena Unindex ======================
Waifu = {"Raiden", "Yae Miko", "Fischl", "Lisa", "Furina"}
print(Waifu)

# Tidak bisa memuat item duplikat
Waifu_1 = {"Raiden", "Yae Miko", "Fischl", "Lisa", "Lisa", "Furina"}
print(Waifu_1)

# True = 1, punya nilai yang sama
Data = {"Ujang",True, False, 1, 2, "Jajang Cicak", "Kadal Mulyono"}
print(Data)

# False = 0, Punya nilai yang sama
Data_Cuk = {"Ujang",True, False, 2, 0, "Jajang Cicak", "Kadal Mulyono"}
print(Data_Cuk)

# len pada Set, Untung hitung banyak data dalam variable
Data_Joko = {"Ujang",True, False, 2, 0, "Jajang Cicak", "Kadal Mulyono"}
print(len(Data_Joko))

# ========================= Jawaban Bahan Ajar Pertemuan 4 di G Form ==================
# s = ("python")
# print(s[1:4])

# x = 4//2
# print(x)

# print(type(3.14))

# y = [1,2,3,4]
# y[2] = 10
# print(y)

# z = ["Zaky", 1,1]
# print(z)

# ======================================================================================
# Dalam Set tak bisa dimasukan tipe data list
# Data_List = {"Zaky", 10, [10,11]}
# print(Data_List)
# Data_List2 = ["Zaky", 10 , {11}]
# print(Data_List2)

# Add
WaifuX = {"Raiden", "Yae Miko", "Fischl", "Lisa", "Furina"}
WaifuX.add("Mavuika")

print(WaifuX)

# Update (Menambah item dari set lainnya)
WaifuS = {"Raiden", "Yae Miko", "Fischl", "Lisa", "Furina"}
Waifi = {"Maulani", "Beido"}
WaifuS.update(Waifi)
 
print(WaifuS)


# Hanya menyimpan item yang sama dari dua buah set menggunakan metode intersection_update()
a = {"appel", "jeruk", "ceri", "Durian"}
b = {"Strawberi", "Blueberry", "appel", "jeruk"}

a.intersection_update(b)

print(a)

# Hanya menyimpan item yang sama dari dua buah set menggunakan metode intersection() 
# sama aja cuman (harus disimpan dalam set/variable yang baru)

ai = {"appel", "jeruk", "ceri", "Durian"}
bi = {"Strawberi", "Blueberry", "appel", "jeruk"}

c = ai.intersection(bi)
print(c)

# hanya menyimpan item yang berbeda dari 2 buah set
au = {"appel", "jeruk", "ceri", "Durian"}
bu = {"Strawberi", "Blueberry", "appel", "jeruk"}

au.symmetric_difference_update(bu)
print(au)

# hanya menimpan item yang berbeda dari 2 buah set
# sama aja cuman (harus disimpan dalam set/variable yang baru)
au = {"appel", "jeruk", "ceri", "Durian"}
bu = {"Strawberi", "Blueberry", "appel", "jeruk"}
cu = au.symmetric_difference(bu)
print(cu)

# mengambil salah satu set saja dengan differents_update()
au.difference_update(bu)
print(au)

# mengambil salah satu set saja dengan differents_update()
# sama aja cuman (harus disimpan dalam set/variable yang baru)
au.difference(bu)
cx = print(au)

print(cx)

# menambah item di set dari sebuah list
a_set = {"apel", "jeruk", "ceri", "durian"}
b_list = ["apel", "jeruk", "Mulyono"]

a_set.update(b_list)
print(a_set)

# menghapus item terakhir dengan pop() methode
a.pop()

# menghapus seluruh item secara sekaligus pada set
a.clear


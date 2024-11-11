# Nama      : Zaky Rizzan Zain
# NIM       : 2403342
# Kelas     : Kelas 1B
# Matkul    : Daspro

list = ["Apel", "Jeruk", "Ceri", "Durian","Apel", "Mangga"]
# Panjang_List = len(list)
# print(Panjang_List)
# No 1
list[2]="Cherry"
print(list)

# list.pop("Ceri")
# list.insert(2,"Cherry")

# No 2
No_Index = (int(input(f"Masukkan No Index Yang Ingin Ditambahkan : ")))
Nama_Item = input("Masukkan Nama Item Yang Ingin Ditambahkan :  ")
list.insert(No_Index,Nama_Item)
print(list)

# No 3
list.sort()
print(list)


print(type(list))#cek tipe data variabel "list"
print(type(No_Index))#cek tipe data variable "No_Index"

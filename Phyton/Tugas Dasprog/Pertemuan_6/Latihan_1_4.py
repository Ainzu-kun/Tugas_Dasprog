# Nama : Zaky Rizzan Zain
# NIM : 2403342
# Kelas : 1B

barang = int(input("Masukkan Jumlah Barang: "))

if (barang > 150):
    total = barang*2500
    print("Maka Total Harga Barang", total)
elif (barang < 100):
    total = barang*5000
    print("Maka Total Harga Barang", total)
elif (barang >= 100):# bisa ditambah and untuk batas jadi, elif (barang >= 100 and barang <=150):
    total = barang*4000
    print("Maka Total Harga Barang", total)


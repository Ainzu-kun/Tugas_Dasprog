"""digunakan untuk menyimpan data dengan format key:Value"""

# contoh
kucing = {
    "nama" : "rafi",
    "Umur" : "200",
    "ras" : "nekmimi",
    "jantan" : True,
    "hobi" : ["Main Genshin", "Tidur"]
}

print(kucing)
print(len(kucing))

# membuat dictionari baru dengan method dict()
buah = dict(nama = "Aple", Jenis = "Buah")
print(buah)

# mengakses item dengen nama key

print(kucing["nama"])

# mengakses item dengan metode get
print(kucing.get("ras"))

# update
kucing["Umur"] = 100
kucing.update({"Umur" : 400, "nama" : "Cicak"})
kucing.update({"Warna" : ["putih", "hitam"]})
print(kucing)

# nambah key
kucing["kaki"] = 4
print(kucing)

# menghapus item 
kucing.pop("jantan")
print(kucing)






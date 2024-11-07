# Function
# merupakan proses diantara sebuah input dan output
# punya perintah "return"

# contoh function
def penjumlahan (a,b):
    hasil = a + b
    return hasil

penjumlahan (2,3)

# Contoh Procedure
def greeting (nama):
    print(f"Halo, {nama}!")

greeting ("Rizky")

# Jangkauan Variable
# Contoh global variable

gloobalVar = 10

def globalFunction ():
    print(f"Hitung  {gloobalVar}")

# Contoh local variable
def localFunction ():
    localVar = 10
    print(f"Hitung {localVar}")

# Arguments
def pengurangan (c,d):
    print (f"Hasil pengurangan {c} - {d} = {c-d}")

pengurangan (10,5)

# Keyword argument
def pengurangan (c,d):
    print (f"Hasil pengurangan {c} - {d} = {c-d}")

# menggunakan keyword argument
# arbitary argument

def funck (*angka):
    print("angka terakhir")


# arbitary keyword argument

def  funck (**angka):
    print("angka terakhir")





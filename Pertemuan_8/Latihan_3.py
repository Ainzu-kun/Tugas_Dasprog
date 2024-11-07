# Nama = Zaky Rizzan Zain
# NIM = 2403342
# Kelas = 1B

# Deret Fibonacci dengan menggunakan fungsi?

def fibonacci (n):
    deret = []
    awal,kedua = int(input("Masukkan angka awal:  ")), int(input("Masukkan angka kedua: "))
    for i in range(n):
        deret.append(awal)
        awal, kedua = kedua, awal + kedua
    return deret

n = int(input("Masukkan banyak angka: "))
print(f"Deret Fibonacci untuk n = {n}:  {fibonacci(n)}")
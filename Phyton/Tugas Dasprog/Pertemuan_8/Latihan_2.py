# Nama = Zaky Rizzan Zain
# NIM = 2403342
# Kelas = 1B



# Menghitung fungsi nilai total dan nilai rata-ratanya
# berdasarkan nilai yang diinputkan dari total nilai
# dimana banyaknya angka tidak di deklarasikan?

def hitung_total(*angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return total, rata_rata

angka_input = []
print("Masukkan angka (0 untuk berhenti):")
while True:
    try:
        nilai = int(input())
        if nilai == 0:
            break
        angka_input.append(nilai)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

total, rata_rata = hitung_total(*angka_input)
print(f"Total nilai adalah {total}, rata rata adalah {rata_rata}")






        

    



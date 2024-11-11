# def hitung_total_dan_rata_rata():
#     total_nilai = 0
#     jumlah_nilai = 0

    

#     while True:
#         input_nilai = input("Nilai: ")
        
#         if input_nilai.lower() == 'selesai':
#             break  # Keluar dari loop jika pengguna mengetik 'selesai'
        
#         try:
#             # Mengonversi input ke float dan menambahkan ke total
#             nilai = float(input_nilai)
#             total_nilai += nilai
#             jumlah_nilai += 1
#         except ValueError:
#             print("Silakan masukkan angka yang valid.")

#     # Menghitung rata-rata jika jumlah_nilai tidak nol
#     if jumlah_nilai > 0:
#         rata_rata = total_nilai / jumlah_nilai
#         print(f"Total nilai: {total_nilai}")
#         print(f"Rata-rata nilai: {rata_rata}")
#     else:
#         print("Tidak ada nilai yang dimasukkan.")

# # Memanggil fungsi
# hitung_total_dan_rata_rata()







def hitung_nilai(*nilai):
    # Menghitung total nilai
    total_nilai = sum(nilai)
    
    # Menghitung rata-rata nilai
    if len(nilai) > 0:
        rata_rata = total_nilai / len(nilai)
    else:
        rata_rata = 0  # Jika tidak ada nilai yang diinputkan
    
    return total_nilai, rata_rata

# Contoh penggunaan
total, rata = hitung_nilai(80, 90, 75, 85, 95)
print(f"Total Nilai: {total}")
print(f"Rata-rata Nilai: {rata:.2f}")
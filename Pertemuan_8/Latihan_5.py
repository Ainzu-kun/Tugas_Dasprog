# Nama = Zaky Rizzan Zain
# NIM = 2403342
# Kelas = 1B


print("\nInput Mulai\n")
jam_mulai = int(input("Jam mulai: "))
menit_mulai = int(input("Menit mulai: "))
detik_mulai = int(input("Detik mulai: "))

print("\nInput Selesai\n")
jam_selesai = int(input("Jam selesai: "))
menit_selesai = int(input("Menit selesai: "))
detik_selesai = int(input("Detik selesai: "))

selisih_jam = jam_selesai - jam_mulai
selisih_menit = menit_selesai - menit_mulai
selisih_detik = detik_selesai - detik_mulai

print("\nHitung Selisih")
print(f"Output: {selisih_jam} jam, {selisih_menit} menit, {selisih_detik} detik\n")

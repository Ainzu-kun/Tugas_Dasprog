# Dictionary untuk nilai tukar sampah per kilogram berdasarkan jenis sampah
harga_sampah = {
    "Plastik": 5000,    # Nilai tukar plastik per kg
    "Kertas": 3000,     # Nilai tukar kertas per kg
    "Logam": 10000,     # Nilai tukar logam per kg
    "Kaca": 4000        # Nilai tukar kaca per kg
}
# Input dari pengguna
jenis_sampah = input("Masukkan jenis sampah (Plastik/Kertas/Logam/Kaca): ")
berat_kg = float(input("Masukkan berat sampah dalam kg: "))


def hitung_nilai_tukar(jenis_sampah, berat_kg):
    if jenis_sampah in harga_sampah:
        nilai_tukar = harga_sampah[jenis_sampah] * berat_kg
        return nilai_tukar
    else:
        return "Jenis sampah tidak ditemukan."

# Hitung nilai tukar
nilai_tukar = hitung_nilai_tukar(jenis_sampah, berat_kg)

if isinstance(nilai_tukar, str):
    print(nilai_tukar)
else:
    print(f"Nilai tukar untuk {berat_kg} kg sampah {jenis_sampah} adalah Rp {nilai_tukar:,}")


# Nama : Zaky Rizzan Zain
# NIM : 2403342
# Kelas : 1B

"""Buatlah program yang mampu memprediksi apakah seseorang dapat menjadi
seorang model catwalk. Beberapa ketentuan sebagai berikut:

1. Wanita/pria berumur 18-25 tahun
2. Tinggi badan 170 (Wanita), dan 175 (pria)
3. Memiliki pengetahuan luas dengan memiliki IQ minimal 130"""

Gender = input("Masukkan Jenis Kelamin Anda: ")
Umur = int(input("Masukkan Umur Anda: "))
Tb = int(input("Masukkan Tinggi Badan Anda: "))
Iq = int(input("Masukkan Hasil Test IQ Anda: "))

if(Gender.lower() == "pria"):
    if(Umur >= 18 and Umur <= 25):
        if(Tb >= 175):
            if(Iq >= 130):
                print("Selamat Anda Dapat Menjadi Model Catwalk!")
            else:
                print("Maaf Anda Belum Lulus")
        else:
              print("Maaf Anda Belum Lulus")
    else:
          print("Maaf Anda Belum Lulus")
if(Gender.lower() == "wanita"):
    if(Umur >= 18 and Umur <= 25):
        if(Tb >= 170):
            if(Iq >= 130):
                print("Selamat Anda Dapat Menjadi Model Catwalk!")
            else:
                print("Maaf Anda Belum Lulus")
        else:
              print("Maaf Anda Belum Lulus")
    else:
          print("Maaf Anda Belum Lulus")


          



# Nama = Zaky Rizzan Zain
# NIM = 2403342
# Kelas = 1B


"""Pak Dedi merupakan seorang Kepala Laboratorium Komputer di SMAN 2 Harapan.
Dia ingin membuat sebuah menu login yang dapat memberi kesempatan user untuk 
memasukkan password kembali ketika dia salah sebanyak 3 kali. Ketika user terus
memasukkan password yang salah, maka user tersebut akan keluar dari menu login tersebut. 
Pak budi juga menambahkan bahwa password ini harus sudah ada dalam sistem yang di buat, 
sehingga sistem itu hanya mengecek password saja tanpa memperdulikan username.

Login dengan 3 kesempatan Admin
username : Daspro2023
password : Latihan"""


print ("\nSilahkan Login\n")

def login ():
    Coba_login = 3

    while Coba_login > 0:
        username = input("Masukkan Username: ")
        Password = input("Masukkan Password: ")
        
        if  Password == "Latihan":
            print(f"\nSelamat Datang {username} di Lab Komputer SMAN 2 Harapan\n")
            break
        else:
            Coba_login -= 1
            if Coba_login > 0 :
                print(f"\nLogin Salah, Kesempatan Anda {Coba_login} Kali Lagi\n")
            else:
                print("\nLogin gagal, silahkan keluar dan coba lagi!\n")
login()




def tampilkan_daftar(daftar):
    print("{:<5} {:<20} {:<30} {:<15} {:<10}".format("Id", " Nama", "  Alamat", "   Telepon", "    Region"))
    print("=========================================================================================")

    for kontak in sorted(daftar, key=lambda k: k["Nama"], reverse=False):
        print("{:<5} |{:<20} |{:<30} |{:<15} |{:<10}".format(kontak["Id"], kontak["Nama"], kontak["Alamat"], kontak["Telepon"], kontak["Region"]))
    print("=========================================================================================")

def tampilkan_daftar1(daftar):
    print("{:<5} {:<20} {:<30} {:<15} {:<10}".format("Id", " Nama", "  Alamat", "   Telepon", "    Region"))
    print("=========================================================================================")

    for kontak in sorted(daftar, key=lambda k: k["Nama"], reverse=True):
        print("{:<5} |{:<20} |{:<30} |{:<15} |{:<10}".format(kontak["Id"], kontak["Nama"], kontak["Alamat"], kontak["Telepon"], kontak["Region"]))
    print("=========================================================================================")

def tampilkan_daftar_region(daftar):
    region = input("Masukkan region: ")
    matching_contacts = []
    for kontak in daftar:
        if kontak["Region"].lower() == region.lower():
            matching_contacts.append(kontak)
            
    if len(matching_contacts) == 0:
        print("Tidak ada kontak dengan region tersebut.")
    else:
        print("{:<5} |{:<20} |{:<30} |{:<15} |{:<10}".format("Id", "Nama", "Alamat", "Telepon", "Region"))
        print("=========================================================================================")
        for kontak in matching_contacts:
            print("{:<5} |{:<20} |{:<30} |{:<15} |{:<10}".format(kontak["Id"], kontak["Nama"], kontak["Alamat"], kontak["Telepon"], kontak["Region"]))
        print("=========================================================================================")

def tambah_kontak(daftar):
    tampilkan_daftar(daftar)
    while True:
        Id = input("Masukkan Id Kontak: ")
        if Id.isdigit():
            break
        print("Id harus berupa angka. Silakan coba lagi.")
        
    a = input("Masukkan Nama Kontak :")
    b = input("Masukkan Alamat Kontak :")
    
    while True:
        c = input("Masukkan Nomor Telepon: ")
        if c.isdigit():
            break
        print("Nomor Telepon harus berupa angka. Silakan coba lagi.")
        
    d = input("Masukkan Region :")

    while True:
        konfirmasi = input("Apakah Anda yakin ingin menambahkan kontak baru? (y/n): ")
        if konfirmasi.capitalize() == "Y":
            daftar.append({"Id": Id, "Nama": a, "Alamat": b, "Telepon": c, "Region": d})
            tampilkan_daftar(daftar)
            print("Berhasil menambahkan Kontak baru!")
            break
        elif konfirmasi.capitalize() == "N":
            print("Batal menambahkan Kontak baru.")
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")



def hapus_kontak(daftar):
    tampilkan_daftar(daftar)
    Id_hapus = input("Masukkan Id kontak yang ingin dihapus: ")

    for i in range(len(daftar)):
        if daftar[i]["Id"] == Id_hapus:
            while True:
                yakin_hapus = input("Apakah anda yakin ingin menghapus kontak ini? (Y/N): ")
                if yakin_hapus.upper() == "Y":
                    del daftar[i]
                    tampilkan_daftar(daftar)
                    print("Berhasil menghapus kontak!")
                    break
                elif yakin_hapus.upper() == "N":
                    print("Penghapusan kontak dibatalkan.")
                    break
                else:
                    print("Mohon masukkan input Y atau N.")
            break
    else:
        print("Kontak tidak ditemukan.")



def ubah_kontak(daftar):
    tampilkan_daftar(daftar)
    Id_ubah = input("Masukkan Id kontak yang ingin diubah :")

    
    for edit in daftar:
        if edit["Id"] == Id_ubah:
            print("Informasi kontak yang akan diubah:")
            print("Nama kontak      : ", edit["Nama"])
            print("Alamat kontak    : ", edit["Alamat"])
            print("Telepon kontak   : ", edit["Telepon"])
            print("Region Kontak    : ", edit["Region"])

            
            konfirmasi = input("Apakah anda yakin ingin mengedit kontak tersebut? (Y/N) ")
            if konfirmasi.upper() == "Y":
                edit["Nama"] = input("Masukkan Nama Kontak :")
                edit["Alamat"] = input("Masukkan Alamat Kontak :")
                while True:
                    no_telp = input("Masukkan No Telepon: ")
                    if no_telp.isdigit():
                        break
                    print("No Telepon harus berupa angka. Silakan coba lagi.")
                edit["Telepon"] = no_telp
                edit["Region"] = input("Masukkan Region :")
                tampilkan_daftar(daftar)
                print("Kontak berhasil diubah.")
            elif konfirmasi.upper() == "N":
                print("Edit kontak dibatalkan.")
            else :
                print("Masukkan statement yang benar")
            break
    else:
        print("Tidak ada Kontak dengan Id tersebut dalam list")


def menu():
    print("\n========== Aplikasi Find My Contact ==========")
    print("1. Tampilkan daftar kontak")
    print("2. Tambah kontak")
    print("3. Hapus kontak")
    print("4. Edit kontak")
    print("5. Keluar")

def menu1():
    print("\n========== Aplikasi Find My Contact ==========")
    print("1. Tampilkan daftar kontak")
    print("2. Tampilkan daftar kontak dari Z ke A")
    print("3. Tampilkan daftar kontak berdasarkan region")
    print("4. Kembali Ke Menu Utama")

def menu2():
    print("\n========== Aplikasi Find My Contact ==========")
    print("1. Tambahkan kontak")
    print("2. Kembali Ke Menu Utama")

def menu3():
    print("\n========== Aplikasi Find My Contact ==========")
    print("1. Hapus kontak")
    print("2. Kembali Ke Menu Utama")

def menu4():
    print("\n========== Aplikasi Find My Contact ==========")
    print("1. Edit kontak")
    print("2. Kembali Ke Menu Utama")

daftar = [
{"Id": "891", "Nama": "Jason Hartono", "Alamat": "Jl. Pancasila no 12", "Telepon": "084621987", "Region": "Jakarta"},
{"Id": "237", "Nama": "Zara Permata Sari", "Alamat": "Jl. Merdeka no 2", "Telepon": "082145789", "Region": "Surabaya"},
{"Id": "199", "Nama": "Andi Saputra", "Alamat": "Jl. Diponegoro no 6", "Telepon": "081234567", "Region": "Jakarta"},
{"Id": "322", "Nama": "Marcell Pangestu", "Alamat": "Perum. Lestari Blok A6", "Telepon": "081528916", "Region": "Bandung"}
]

while True:
    menu()
    pilihan = input("Masukkan pilihan Anda: ")
    if pilihan == "1":
        while True:
            menu1()
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                tampilkan_daftar(daftar)
            elif pilihan == "2":
                tampilkan_daftar1(daftar)
            elif pilihan == "3":
                tampilkan_daftar_region(daftar)
            elif pilihan == "4":
                pilihan = input("Apakah anda ingin kembali ke menu utama? Y/N :")
                if pilihan.capitalize() == "Y":
                    break
                elif pilihan.capitalize() == "N":
                    continue
                else:
                    print("Masukkan statement yang benar!")
            else:
                print("Masukkan angka yang benar")
    
    elif pilihan == "2":
        while True:
            menu2()
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                tambah_kontak(daftar)
            elif pilihan == "2":
                pilihan = input("Apakah anda ingin kembali ke menu utama? Y/N :")
                if pilihan.capitalize() == "Y":
                    break
                elif pilihan.capitalize() == "N":
                    continue
                else:
                    print("Masukkan statement yang benar!")
            else:
                print("Masukkan angka yang benar")
    elif pilihan == "3":
        while True:
            menu3()
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                hapus_kontak(daftar)
            elif pilihan == "2":
                pilihan = input("Apakah anda ingin kembali ke menu utama? Y/N :")
                if pilihan.capitalize() == "Y":
                    break
                elif pilihan.capitalize() == "N":
                    continue
                else:
                    print("Masukkan statement yang benar!")
            else:
                print("Masukkan angka yang benar")
    elif pilihan == "4":
        while True:
            menu4()
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                ubah_kontak(daftar)
            elif pilihan == "2":
                pilihan = input("Apakah anda ingin kembali ke menu utama? Y/N :")
                if pilihan.capitalize() == "Y":
                    break
                elif pilihan.capitalize() == "N":
                    continue
                else:
                    print("Masukkan statement yang benar!")
            else:
                print("Masukkan angka yang benar")
    elif pilihan == "5":
        print("Terima kasih telah menggunakan Aplikasi Find My Contact!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

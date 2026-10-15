import os

database_user = [
    ["admin", "admin123"],
    ["user", "user123"]
]

katalog_baju = [
    ["BA01", "Bugis", "M", 85000, "Tersedia", ("Baju Bodo", "Lipa Sabbe", "Ponto")],
    ["BA02", "Buton", "L", 90000, "Tersedia", ("Baju kaboroko", "Sarung Samasili Kumbaea", "Mahkota Adat Buton")]
]

transaksi_sewa = []
user_login = ""
role_login = ""
status_login_berhasil = False   

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("SISTEM SEWA BAJU ADAT")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")
    
    menu_awal = input("Pilih menu (1-3): ")
    
    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("HALAMAN LOGIN")
        username_input = input("Username: ")
        password_input = input("Password: ")
        
        status_login_berhasil = False
        for akun in database_user:
            if akun[0] == username_input and akun[1] == password_input:
                user_login = akun[0]

                if user_login == "admin":
                    role_login = "Admin"
                else:
                    role_login = "Pengguna"
                status_login_berhasil = True
                break
        
        if status_login_berhasil:
            print("Login berhasil sebagai", role_login)
            input("Tekan Enter untuk lanjut...")
            
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("MENU UTAMA - Halo", user_login, "(", role_login, ")")
                print("1. Lihat Katalog Baju Adat")
                print("2. Tambah Data (Sewa / Katalog)")
                print("3. Lihat Daftar Transaksi")
                print("4. Logout")
                
                pilihan_menu = input("Pilih menu (1-4): ")
                
                if pilihan_menu == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("KATALOG PERSEDIAAN BAJU ADAT")
                    for idx, baju in enumerate(katalog_baju):
                        print(idx + 1, ". Kode:", baju[0], "| Daerah:", baju[1], "| Ukuran:", baju[2], "| Tarif: Rp", baju[3], "| Status:", baju[4])
                        print("   Set Busana & Aksesori:", baju[5])
                    input("\nTekan Enter untuk kembali...")
                
                elif pilihan_menu == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("MENU TAMBAH DATA")
                    print("1. Tambah Transaksi Sewa")
                    if role_login == "Admin":
                        print("2. Tambah Katalog Baju Baru")
                    
                    sub_pilihan = input("Pilih menu tambah: ")
                    
                    if sub_pilihan == "1":
                        print("--- INPUT TRANSAKSI SEWA BARU ---")
                        nama = input("Masukkan Nama Penyewa: ")
                        hp = input("Masukkan Nomor HP: ")
                        kode = input("Masukkan Kode Baju yang dipilih: ")
                        tgl_sewa = input("Tanggal Sewa (DD-MM-YYYY): ")
                        tgl_kembali = input("Tanggal Pengembalian (DD-MM-YYYY): ")
                        
                        baju_ditemukan = False
                        for baju in katalog_baju:
                            if baju[0] == kode:
                                if baju[4] == "Tersedia":
                                    baju[4] = "Disewa"
                                    baju_ditemukan = True
                                    break
                                else:
                                    print("Maaf, baju tersebut sedang tidak tersedia.")
                                    break
                        
                        if baju_ditemukan:
                            id_trx = len(transaksi_sewa) + 1
                            transaksi_sewa.append([id_trx, nama, hp, kode, tgl_sewa, tgl_kembali, "DP"])
                            print("Sukses! Transaksi sewa berhasil dicatat.")
                        else:
                            print("Gagal mencatat transaksi, pastikan kode baju benar.")
                        input("\nTekan Enter untuk kembali...")
                    
                    elif sub_pilihan == "2" and role_login == "Admin":
                        print("--- TAMBAH KATALOG BAJU BARU ---")
                        kode_baru = input("Kode Baju (contoh: BA03): ")
                        daerah_baru = input("Asal Daerah: ")
                        ukuran_baru = input("Ukuran (S/M/L/XL): ")
                        tarif_baru = int(input("Tarif Sewa per Hari (angka): "))
                        baju_utama = input("Nama Baju: ")
                        sarung = input("Nama Sarung: ")
                        aksesori = input("Aksesori / Pelengkap: ")
                        tuple_set = (baju_utama, sarung, aksesori)
                        
                        katalog_baju.append([kode_baru, daerah_baru, ukuran_baru, tarif_baru, "Tersedia", tuple_set])
                        print("Baju adat baru berhasil ditambahkan ke katalog!")
                        input("\nTekan Enter untuk kembali...")
                
                elif pilihan_menu == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("DAFTAR TRANSAKSI PENYEWAAN")
                    if len(transaksi_sewa) == 0:
                        print("Belum ada data transaksi sewa.")
                    else:
                        for trx in transaksi_sewa:
                            print("ID:", trx[0], "| Nama:", trx[1], "| HP:", trx[2], "| Kode Baju:", trx[3], "| Periode:", trx[4], "s.d", trx[5], "| Bayar:", trx[6])
                    input("\nTekan Enter untuk kembali...")
                
                elif pilihan_menu == "4":
                    break
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut...")
            
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("HALAMAN REGISTER AKUN")
        user_baru = input("Buat Username Baru: ")
        pass_baru = input("Buat Password Baru: ")
        
        database_user.append([user_baru, pass_baru])
        print("Registrasi berhasil! Silakan login menggunakan akun baru.")
        input("Tekan Enter untuk lanjut...")
        
    elif menu_awal == "3":
        print("Keluar dari program. Terima kasih.")
        break

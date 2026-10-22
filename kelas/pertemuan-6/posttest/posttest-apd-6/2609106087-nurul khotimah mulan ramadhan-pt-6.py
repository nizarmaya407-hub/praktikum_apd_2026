import os

database_user = {
    "admin": ["admin123", "Admin"],
    "user": ["user123", "Pengguna"]
}

katalog_baju = {
    "BA01": {
        "daerah": "Bugis",
        "ukuran": "M",
        "tarif": 85000,
        "status": "Tersedia",
        "aksesoris": ("Baju Bodo", "Lipa Sabbe", "Ponto")
    },
    "BA02": {
        "daerah": "Buton",
        "ukuran": "L",
        "tarif": 90000,
        "status": "Tersedia",
        "aksesoris": ("Baju Kaboroko", "Sarung Samasili Kumbaea", "Mahkota Adat Buton")
    }
}

transaksi_sewa = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM SEWA BAJU ADAT ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")
    
    menu_awal = input("Pilih menu (1-3): ")
    
    if menu_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        break
        
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- REGISTRASI AKUN BARU ---")
        username_baru = input("Buat Username baru: ")
        
        if username_baru in database_user:
            print("Username sudah terdaftar! Gunakan username lain.")
        else:
            password_baru = input("Buat Password baru: ")
            database_user[username_baru] = [password_baru, "Pengguna"]
            print("Registrasi berhasil! Silakan login.")
        input("\nTekan Enter untuk melanjutkan...")
        
    elif menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- HALAMAN LOGIN ---")
        username_input = input("Username: ")
        password_input = input("Password: ")
        
        if username_input in database_user and database_user[username_input][0] == password_input:
            user_login = username_input
            role_login = database_user[username_input][1]
            print(f"Login berhasil sebagai {role_login}!")
            input("Tekan Enter untuk masuk ke Menu Utama...")
            
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"=== MENU UTAMA - Halo {user_login} ({role_login}) ===")
                print("1. Lihat Katalog Baju Adat")
                print("2. Tambah Data (Sewa / Katalog)")
                print("3. Lihat Daftar Transaksi")
                print("4. Logout")
                
                pilihan_menu = input("Pilih menu (1-4): ")
                
                if pilihan_menu == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== KATALOG PERSEDIAAN BAJU ADAT ===")
                    for kode, detail in katalog_baju.items():
                        print(f"- Kode: {kode} | Daerah: {detail['daerah']} | Ukuran: {detail['ukuran']} | Tarif: Rp {detail['tarif']} | Status: {detail['status']}")
                        print(f"  Set Busana & Aksesori: {detail['aksesoris']}")
                    input("\nTekan Enter untuk kembali...")
                    
                elif pilihan_menu == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU TAMBAH DATA ===")
                    if role_login == "Admin":
                        print("1. Sewa Baju Adat")
                        print("2. Tambah Katalog Baju Baru")
                        sub_pilihan = input("Pilih sub-menu (1/2): ")
                    else:
                        sub_pilihan = "1"
                        
                    if sub_pilihan == "1":
                        print("\n--- INPUT TRANSAKSI SEWA BARU ---")
                        nama = input("Masukkan Nama Penyewa: ")
                        hp = input("Masukkan Nomor HP: ")
                        kode = input("Masukkan Kode Baju yang dipilih: ")
                        tgl_sewa = input("Tanggal Sewa (DD-MM-YYYY): ")
                        tgl_kembali = input("Tanggal Pengembalian (DD-MM-YYYY): ")
                        
                        if kode in katalog_baju:
                            if katalog_baju[kode]["status"] == "Tersedia":
                                katalog_baju[kode]["status"] = "Disewa"
                                id_trx = len(transaksi_sewa) + 1
                                transaksi_sewa.append([id_trx, nama, hp, kode, tgl_sewa, tgl_kembali, "DP"])
                                print("Sukses! Transaksi sewa berhasil dicatat.")
                            else:
                                print("Maaf, baju tersebut sedang tidak tersedia.")
                        else:
                            print("Gagal mencatat transaksi, pastikan kode baju benar.")
                        input("\nTekan Enter untuk kembali...")
                        
                    elif sub_pilihan == "2" and role_login == "Admin":
                        print("\n--- TAMBAH KATALOG BAJU BARU ---")
                        kode_baru = input("Kode Baju (contoh: BA03): ")
                        
                        if kode_baru in katalog_baju:
                            print("Kode baju sudah terdaftar di katalog!")
                        else:
                            daerah_baru = input("Asal Daerah: ")
                            ukuran_baru = input("Ukuran (S/M/L/XL): ")
                            tarif_str = input("Tarif Sewa per Hari (angka): ")
                            
                            if tarif_str.isdigit():
                                tarif_baru = int(tarif_str)
                                baju_utama = input("Nama Baju: ")
                                sarung = input("Nama Sarung: ")
                                aksesori = input("Aksesori / Pelengkap: ")
                                tuple_set = (baju_utama, sarung, aksesori)
                                
                                katalog_baju[kode_baru] = {
                                    "daerah": daerah_baru,
                                    "ukuran": ukuran_baru,
                                    "tarif": tarif_baru,
                                    "status": "Tersedia",
                                    "aksesoris": tuple_set
                                }
                                print("Baju adat baru berhasil ditambahkan ke katalog!")
                            else:
                                print("Tarif harus berupa angka!")
                        input("\nTekan Enter untuk kembali...")
                    else:
                        print("Pilihan menu tambah tidak valid!")
                        input("\nTekan Enter untuk kembali...")
                        
                elif pilihan_menu == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR TRANSAKSI SEWA ===")
                    if len(transaksi_sewa) == 0:
                        print("Belum ada transaksi sewa yang tercatat.")
                    else:
                        for trx in transaksi_sewa:
                            print(f"ID: {trx[0]} | Nama: {trx[1]} | HP: {trx[2]} | Kode Baju: {trx[3]} | Sewa: {trx[4]} s.d {trx[5]} | Status: {trx[6]}")
                    input("\nTekan Enter untuk kembali...")
                    
                elif pilihan_menu == "4":
                    print("Logout berhasil.")
                    user_login = ""
                    role_login = ""
                    input("Tekan Enter untuk kembali ke halaman login...")
                    break 
                else:
                    print("Pilihan menu tidak valid!")
                    input("\nTekan Enter untuk kembali...")
        else:
            print("Login Gagal! Username atau Password salah.")
            input("\nTekan Enter untuk kembali...")
    else:
        print("Pilihan menu tidak valid!")
        input("\nTekan Enter untuk kembali...")
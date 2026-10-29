import os

database_user = {
    "admin": ["Admin12345", "Admin"],
    "user": ["User123456", "Pengguna"]
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

def cetak_header(judul):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print(f"    {judul}")
    print("=" * 40)

def tampilkan_info_penutupan():
    pesan = "Terima kasih telah menggunakan sistem sewa baju adat kami."
    print(pesan)

def hitung_total_transaksi():
    total = len(transaksi_sewa)
    return total

def validasi_tarif_baju(tarif_str):
    try:
        hasil_angka = int(tarif_str)
        if hasil_angka <= 0:
            raise ValueError("Tarif harus bernilai positif lebih dari 0!")
        return hasil_angka
    except ValueError as e:
        print(f"Error Input Tarif: {e}")
        return None

def konfirmasi_hitung_mundur(detik):
    if detik <= 0:
        print("Selesai!")
        return
    else:
        print(f"Mengembalikan dalam {detik} detik...", end="\r")
        konfirmasi_hitung_mundur(detik - 1)

while True:
    cetak_header("SISTEM SEWA BAJU ADAT")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    try:
        menu_awal_input = input("Pilih menu (1-3): ")
        if not menu_awal_input.isdigit():
            raise ValueError("Pilihan menu harus berupa angka (1, 2, atau 3)!")
        
        menu_awal = int(menu_awal_input)
        if menu_awal < 1 or menu_awal > 3:
            raise IndexError("Pilihan menu di luar jangkauan (1 sampai 3).")
            
    except ValueError as err_val:
        print(f"[ValueError Terdeteksi]: {err_val}")
        input("\nTekan Enter untuk mencoba lagi...")
        continue
    except IndexError as err_idx:
        print(f"[IndexError Terdeteksi]: {err_idx}")
        input("\nTekan Enter untuk mencoba lagi...")
        continue
    else:

        if menu_awal == 3:
            cetak_header("KELUAR PROGRAM")
            tampilkan_info_penutupan()
            break
            
        elif menu_awal == 2:
            cetak_header("REGISTRASI AKUN BARU")
            username_baru = input("Buat Username baru: ")
            
            try:
                if len(username_baru) < 4:
                    raise ValueError("Username minimal harus memiliki 4 karakter!")
                if username_baru in database_user:
                    print("Username sudah terdaftar! Gunakan username lain.")
                else:
                    password_baru = input("Buat Password baru (min 6 karakter, ada angka): ")
                    if len(password_baru) < 6:
                        raise ValueError("Password terlalu pendek, minimal 6 karakter!")
                    
                    database_user[username_baru] = [password_baru, "Pengguna"]
                    print("Registrasi berhasil! Silakan login.")
            except ValueError as e_reg:
                print(f"Gagal Registrasi: {e_reg}")
            finally:
                print("[Info]: Proses registrasi selesai diproses.")
            
            input("\nTekan Enter untuk melanjutkan...")
            
        elif menu_awal == 1:
            cetak_header("HALAMAN LOGIN")
            username_input = input("Username: ")
            password_input = input("Password: ")
            
            try:
                if username_input not in database_user:
                    raise KeyError("Username tidak ditemukan di dalam database!")
                
                if database_user[username_input][0] != password_input:
                    raise ValueError("Password yang Anda masukkan salah!")
            except KeyError as ke:
                print(f"Error Login: {ke}")
                input("\nTekan Enter untuk kembali...")
                continue
            except ValueError as ve:
                print(f"Error Login: {ve}")
                input("\nTekan Enter untuk kembali...")
                continue
            else:
                user_login = username_input
                role_login = database_user[username_input][1]
                print(f"Login berhasil sebagai {role_login}!")
                input("Tekan Enter untuk masuk ke Menu Utama...")
                
                while True:
                    cetak_header(f"MENU UTAMA - Halo {user_login} ({role_login})")
                    print("1. Lihat Katalog Baju Adat")
                    print("2. Tambah Data (Sewa / Katalog)")
                    print("3. Lihat Daftar Transaksi")
                    print("4. Logout")
                    
                    try:
                        pilihan_menu_input = input("Pilih menu (1-4): ")
                        if not pilihan_menu_input.isdigit():
                            raise ValueError("Pilihan menu harus berupa angka bulat!")
                        pilihan_menu = int(pilihan_menu_input)
                    except ValueError as err_menu:
                        print(f"Kesalahan Input: {err_menu}")
                        input("\nTekan Enter untuk kembali...")
                        continue
                    
                    if pilihan_menu == 1:
                        cetak_header("KATALOG PERSEDIAAN BAJU ADAT")
                        for kode, detail in katalog_baju.items():
                            print(f"- Kode: {kode} | Daerah: {detail['daerah']} | Ukuran: {detail['ukuran']} | Tarif: Rp {detail['tarif']} | Status: {detail['status']}")
                            print(f"  Set Busana & Aksesori: {detail['aksesoris']}")
                        input("\nTekan Enter untuk kembali...")
                        
                    elif pilihan_menu == 2:
                        cetak_header("MENU TAMBAH DATA")
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
                            
                            try:
                                if kode not in katalog_baju:
                                    raise KeyError("Kode baju tidak terdaftar di dalam katalog!")
                                
                                if katalog_baju[kode]["status"] != "Tersedia":
                                    print("Maaf, baju tersebut sedang tidak tersedia.")
                                else:
                                    katalog_baju[kode]["status"] = "Disewa"
                                    id_trx = hitung_total_transaksi() + 1
                                    transaksi_sewa.append([id_trx, nama, hp, kode, tgl_sewa, tgl_kembali, "DP"])
                                    print("Sukses! Transaksi sewa berhasil dicatat.")
                            except KeyError as err_katalog:
                                print(f"Transaksi Gagal: {err_katalog}")
                            finally:
                                print("[Info]: Pemeriksaan kode katalog selesai.")
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
                                
                                tarif_baru = validasi_tarif_baju(tarif_str)
                                if tarif_baru is not None:
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
                            input("\nTekan Enter untuk kembali...")
                        else:
                            print("Pilihan menu tambah tidak valid!")
                            input("\nTekan Enter untuk kembali...")
                            
                    elif pilihan_menu == 3:
                        cetak_header("DAFTAR TRANSAKSI SEWA")
                        if len(transaksi_sewa) == 0:
                            print("Belum ada transaksi sewa yang tercatat.")
                        else:
                            for trx in transaksi_sewa:
                                print(f"ID: {trx[0]} | Nama: {trx[1]} | HP: {trx[2]} | Kode Baju: {trx[3]} | Sewa: {trx[4]} s.d {trx[5]} | Status: {trx[6]}")
                            print(f"Total Transaksi Keseluruhan: {hitung_total_transaksi()}")
                        input("\nTekan Enter untuk kembali...")
                        
                    elif pilihan_menu == 4:
                        print("Logout berhasil.")
                        user_login = ""
                        role_login = ""
                        konfirmasi_hitung_mundur(3)
                        print("\n")
                        break 
                    else:
                        print("Pilihan menu tidak valid!")
                        input("\nTekan Enter untuk kembali...")
from auth import login_akun, register_akun
from fitur import (
    cetak_header, tampilkan_info_penutupan, konfirmasi_hitung_mundur,
    lihat_katalog, tambah_transaksi, tambah_katalog_baru, lihat_transaksi
)

def main():
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
                register_akun()
                input("\nTekan Enter untuk melanjutkan...")
                
            elif menu_awal == 1:
                user_login, role_login = login_akun()
                if user_login and role_login:
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
                            lihat_katalog()
                            
                        elif pilihan_menu == 2:
                            cetak_header("MENU TAMBAH DATA")
                            if role_login == "Admin":
                                print("1. Sewa Baju Adat")
                                print("2. Tambah Katalog Baju Baru")
                                sub_pilihan = input("Pilih sub-menu (1/2): ")
                            else:
                                sub_pilihan = "1"
                                
                            if sub_pilihan == "1":
                                tambah_transaksi()
                            elif sub_pilihan == "2" and role_login == "Admin":
                                tambah_katalog_baru()
                            else:
                                print("Pilihan menu tambah tidak valid!")
                                input("\nTekan Enter untuk kembali...")
                                
                        elif pilihan_menu == 3:
                            lihat_transaksi()
                            
                        elif pilihan_menu == 4:
                            print("Logout berhasil.")
                            konfirmasi_hitung_mundur(3)
                            print("\n")
                            break 
                        else:
                            print("Pilihan menu tidak valid!")
                            input("\nTekan Enter untuk kembali...")
                else:
                    input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    main()
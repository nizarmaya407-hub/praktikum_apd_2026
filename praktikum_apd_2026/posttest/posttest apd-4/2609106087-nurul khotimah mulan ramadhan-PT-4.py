username = "mulan"
pin = "087"
saldo = 1000000

login_berhasil = False
percobaan = 0
maks_percobaan = 3

while percobaan < maks_percobaan:
    print(f"login -> Username: {username}, Pin: {pin}")
    
    input_user = input("Masukkan Username: ")
    input_pin = input("Masukkan Pin: ")
    
    if input_user == username and input_pin == pin:
        print("Login Berhasil!")
        login_berhasil = True
        break
    else:
        percobaan += 1
        sisa = maks_percobaan - percobaan
        
        if sisa > 0:
            print(f"login gagal! sisa percobaan: {sisa}")
        else:
            print("login gagal! akun anda terblokir.")

if login_berhasil == True:
    menu_aktif = True
    
    while menu_aktif:
        print("MENU UTAMA")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            print(f"Sisa saldo Anda: Rp {saldo:,}")
            
        elif pilihan == "2":
            print("TARIK TUNAI")
            tarik_str = input("Masukkan nominal tarik (kelipatan 50000): ")
            
            if tarik_str.isdigit() == False:
                print("Masukkan angka yang valid!")
            else:
                nominal = int(tarik_str)
                
                if nominal <= 0:
                    print("Nominal harus lebih dari 0!")
                elif nominal % 50000 != 0:
                    print("Nominal harus kelipatan Rp 50.000")
                elif nominal > saldo:
                    print("Saldo tidak mencukupi!")
                else:
                    saldo -= nominal
                    print("Transaksi Berhasil! Penarikan tunai sukses.")
                    print(f"Sisa saldo: Rp {saldo:,}")
                    
        elif pilihan == "3":
            print("SETOR TUNAI")
            setor_str = input("Masukkan nominal setor (kelipatan 50000): ")
            
            if setor_str.isdigit() == False:
                print("Masukkan angka yang valid!")
            else:
                nominal = int(setor_str)
                
                if nominal <= 0:
                    print("Nominal harus lebih dari 0!")
                elif nominal % 50000 != 0:
                    print("Nominal harus kelipatan Rp 50.000")
                else:
                    saldo += nominal
                    print("Transaksi Berhasil! Penyetoran tunai sukses.")
                    print(f"Total saldo: Rp {saldo:,}")
                    
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan kami. Semoga hari Anda menyenangkan!")
            menu_aktif = False
            
        else:
            print("Pilihan tidak valid! Silakan pilih nomor 1 sampai 4.")
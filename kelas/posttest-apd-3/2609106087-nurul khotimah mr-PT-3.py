print("=== SISTEM TOP UP GAME ===")

user = input("Username: ")
sandi = input("Password (2 digit NIM): ")

if user == "mulan" and sandi == "87":
    print("Login Berhasil")
    print("Selamat datang, silakan isi data dahulu")
    

    id_pl = input("Masukkan ID Player: ")
    game = input("nama game (genshin impact / minecraft / mobile legends): ")
    kategori = input("Kategori Top Up (kecil / menengah / besar): ")
    metode = input("Metode Pembayaran (pulsa / e-wallet): ")
    
    if kategori == "kecil":
        harga = 15000
    elif kategori == "menengah":
        harga = 50000
    elif kategori == "besar":
        harga = 150000
    else:
        harga = 15000  
        
    admin = 2500 if metode == "pulsa" else 500
    
    total_bayar = harga + admin
    
    print("Total yang harus dibayar: Rp", total_bayar)
    
    uang = int(input("Masukkan nominal uang yang dibayarkan: Rp "))
    
    if uang < total_bayar:
        print("Transaksi Gagal Saldo tidak mencukupi")
    else:
        kembalian = uang - total_bayar
        
        print("\n=== STRUK PEMBELIAN ===")
        print("ID Player         :", id_pl)
        print("Nama Game         :", game)
        print("Kategori Top Up   :", kategori)
        print("Metode Pembayaran :", metode)
        print("Biaya Admin       : Rp", admin)
        print("Total Bayar       : Rp", total_bayar)
        print("Uang Bayar        : Rp", uang)
        print("Kembalian         : Rp", kembalian)
        print("Transaksi Berhasil, Terima kasih telah melakukan Top Up")

else:
    print("Login Gagal")
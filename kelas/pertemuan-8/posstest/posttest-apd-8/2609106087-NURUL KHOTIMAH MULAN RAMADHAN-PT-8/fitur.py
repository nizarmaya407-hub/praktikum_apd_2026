import os
from datetime import datetime
from prettytable import PrettyTable
from database import katalog_baju, transaksi_sewa

def cetak_header(judul):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print(f"    {judul}")
    print("=" * 40)

def tampilkan_info_penutupan():
    pesan = "Terima kasih telah menggunakan sistem sewa baju adat kami."
    print(pesan)

def hitung_total_transaksi():
    return len(transaksi_sewa)

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

def lihat_katalog():
    cetak_header("KATALOG PERSEDIAAN BAJU ADAT")
    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Daerah", "Ukuran", "Tarif (Rp)", "Status", "Aksesori"]
    
    for kode, detail in katalog_baju.items():
        aksesoris_str = ", ".join(detail['aksesoris'])
        tabel.add_row([kode, detail['daerah'], detail['ukuran'], f"Rp {detail['tarif']:,}", detail['status'], aksesoris_str])
        
    print(tabel)
    input("\nTekan Enter untuk kembali...")

def tambah_transaksi():
    print("\n--- INPUT TRANSAKSI SEWA BARU ---")
    nama = input("Masukkan Nama Penyewa: ")
    hp = input("Masukkan Nomor HP: ")
    kode = input("Masukkan Kode Baju yang dipilih: ")
    waktu_sewa = datetime.now().strftime("%d-%m-%Y %H:%M")
    tgl_kembali = input("Tanggal Pengembalian (DD-MM-YYYY): ")
    
    try:
        if kode not in katalog_baju:
            raise KeyError("Kode baju tidak terdaftar di dalam katalog!")
        
        if katalog_baju[kode]["status"] != "Tersedia":
            print("Maaf, baju tersebut sedang tidak tersedia.")
        else:
            katalog_baju[kode]["status"] = "Disewa"
            id_trx = hitung_total_transaksi() + 1
            transaksi_sewa.append([id_trx, nama, hp, kode, waktu_sewa, tgl_kembali, "DP"])
            print("Sukses! Transaksi sewa berhasil dicatat pada:", waktu_sewa)
    except KeyError as err_katalog:
        print(f"Transaksi Gagal: {err_katalog}")
    finally:
        print("[Info]: Pemeriksaan kode katalog selesai.")
    input("\nTekan Enter untuk kembali...")

def tambah_katalog_baru():
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

def lihat_transaksi():
    cetak_header("DAFTAR TRANSAKSI SEWA")
    if len(transaksi_sewa) == 0:
        print("Belum ada transaksi sewa yang tercatat.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "No HP", "Kode", "Waktu Sewa", "Pengembalian", "Status"]
        for trx in transaksi_sewa:
            tabel.add_row(trx)
        print(tabel)
        print(f"Total Transaksi Keseluruhan: {hitung_total_transaksi()}")
    input("\nTekan Enter untuk kembali...")
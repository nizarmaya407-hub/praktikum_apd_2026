k1, k2, k3, k4, k5, k6 = 120000, 135000, 150000, 175000, 200000, 220000
daftar_harga = [k1, k2, k3, k4, k5, k6]

admin = 15000
jumlah_total = k1 + k2 + k3 + k4 + k5 + k6 + admin

rata_rata = jumlah_total / len(daftar_harga)
nomor_induk = 87
status_beda = nomor_induk != rata_rata

kurs_pound = 22000  # Nilai kurs bisa disesuaikan
konversi_gbp = jumlah_total / kurs_pound
empat_komponen_awal = daftar_harga[-6:-2]

print("=== PROGRAM TRANSAKSI BENGKEL MAJU MUNDUR ===")
print(f"Daftar Harga Komponen: {daftar_harga}")
print(f"Total Biaya Keseluruhan: Rp {jumlah_total}")
print(f"Total dalam Poundsterling: £ {konversi_gbp:.2f}")
print(f"Nilai Rata-rata: {rata_rata}")
print(f"Nomor NIM: {nomor_induk}")
print(f"Hasil Cek Boolean (NIM != Rata-rata): {status_beda}")
print(f"Slicing Negatif Komponen 1-4: {empat_komponen_awal}")
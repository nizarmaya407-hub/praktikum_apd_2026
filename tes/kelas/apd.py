kegiatan_resmi = ("Desain Poster", "Pemrograman", "Fotografi", "Presentasi Karya")

data_peserta = []
masih_ada_peserta = True

while masih_ada_peserta == True:
    nama = input("Masukkan nama peserta: ")
    nim = input("Masukkan NIM peserta: ")
    umur = int(input("Masukkan umur peserta: "))
    program_studi = input("Masukkan program studi peserta: ")
    nomor_kelompok = int(input("Masukkan nomor kelompok peserta: "))
    kegiatan = input("Masukkan kegiatan yang dipilih: ")

    nim_terdaftar = False
    for p in data_peserta:
        if p["nim"] == nim:
            nim_terdaftar = True

    if nim_terdaftar == True:
        print("Peserta sudah terdaftar")
    else:
        # Pengecekan kuota kegiatan
        kuota_penuh = False
        if kegiatan == "Pemrograman":
            kuota_penuh = True

        while kuota_penuh == True:
            print("Kuota kegiatan penuh, silakan pilih kegiatan lain")
            kegiatan = input("Masukkan kegiatan yang dipilih: ")
            if kegiatan == "Pemrograman":
                kuota_penuh = True
            else:
                kuota_penuh = False

        status_pembayaran = input("Masukkan status pembayaran peserta: ")

        if status_pembayaran == "Sudah Bayar":
            status_pendaftaran = "Terdaftar"
        else:
            status_pendaftaran = "Menunggu Pembayaran"

        data_peserta.append({
            "nama": nama,
            "nim": nim,
            "umur": umur,
            "program_studi": program_studi,
            "nomor_kelompok": nomor_kelompok,
            "kegiatan": kegiatan,
            "status_pembayaran": status_pembayaran,
            "status_pendaftaran": status_pendaftaran
        })

        print("Nama:", nama, "| Kegiatan:", kegiatan, "| Status Pendaftaran:", status_pendaftaran)

    pilihan_lanjut = input("Apakah masih ada peserta yang akan didata? (ya/tidak): ")
    if pilihan_lanjut == "tidak":
        masih_ada_peserta = False

print()
print("Tampilkan seluruh data peserta:")
for f in data_peserta:
    print("Nama:", f["nama"], "| NIM:", f["nim"], "| Kegiatan:", f["kegiatan"], "| Status:", f["status_pendaftaran"])

kegiatan_unik = set()
for f in data_peserta:
    kegiatan_unik.add(f["kegiatan"])

print()
print("Daftar kegiatan yang diikuti peserta (tanpa duplikasi):")
for k in kegiatan_unik:
    print("-", k)
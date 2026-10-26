# =============================================================
# fitur_nilai.py — Fungsi Fitur Utama & Tambahan
# Aplikasi SIPENA (Sistem Pencatatan Nilai Akhir)
# MORRIS Teknik Informatika 2026
# =============================================================

from utils import minta_teks, minta_nilai
from tampilan import garis, judul, pesan, tampilkan_tabel


# ─── Fungsi Konversi Huruf Mutu ────────────────────────────
def konversi_huruf_mutu(nilai):
    """
    Mengkonversi nilai angka (0-100) menjadi huruf mutu
    menggunakan percabangan bertingkat if-elif-else.

    A  = 80 - 100
    B  = 70 - 79
    C  = 56 - 69
    D  = 40 - 55
    E  = 0  - 39
    """
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 56:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


# ─── Fitur 1: Tambah Data Mahasiswa ────────────────────────
def tambah_data(data):
    """
    Menambahkan data mahasiswa baru ke dalam list 'data'.
    Input: nama mahasiswa dan nilai (0-100).
    Data disimpan sebagai dictionary {'nama': ..., 'nilai': ...}.
    """
    judul("TAMBAH DATA MAHASISWA")
    nama  = minta_teks("  Nama Mahasiswa : ")
    nilai = minta_nilai("  Nilai (0-100)  : ")

    data.append({"nama": nama, "nilai": nilai})

    print()
    pesan(f"Data '{nama}' dengan nilai {nilai} berhasil ditambahkan!", "sukses")
    pesan(f"Total data saat ini: {len(data)} mahasiswa.", "info")
    print()


# ─── Fitur 2: Tampilkan Seluruh Data ──────────────────────
def tampilkan_data(data):
    """
    Menampilkan seluruh data mahasiswa dalam bentuk tabel rapi.
    Menampilkan pesan peringatan jika data masih kosong.
    """
    judul("DAFTAR NILAI MAHASISWA")

    if len(data) == 0:
        pesan("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.", "peringatan")
        print()
        return

    tampilkan_tabel(data)
    print(f"  Total: {len(data)} mahasiswa")
    print()


# ─── Fitur 3: Cari Mahasiswa ──────────────────────────────
def cari_mahasiswa(data):
    """
    Mencari data mahasiswa berdasarkan kata kunci nama.
    Pencarian bersifat case-insensitive (huruf besar/kecil diabaikan).
    Menampilkan pesan peringatan jika data masih kosong.
    """
    judul("CARI DATA MAHASISWA")

    if len(data) == 0:
        pesan("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.", "peringatan")
        print()
        return

    kata_kunci = minta_teks("  Masukkan kata kunci nama: ")
    hasil = []

    for mhs in data:
        if kata_kunci.lower() in mhs["nama"].lower():
            hasil.append(mhs)

    print()
    if len(hasil) == 0:
        pesan(f"Tidak ditemukan mahasiswa dengan kata kunci '{kata_kunci}'.", "peringatan")
    else:
        pesan(f"Ditemukan {len(hasil)} hasil untuk '{kata_kunci}':", "sukses")
        tampilkan_tabel(hasil)
    print()


# ─── Fitur 4: Statistik Nilai ─────────────────────────────
def tampilkan_statistik(data):
    """
    Menampilkan statistik nilai mahasiswa:
    - Jumlah mahasiswa
    - Rata-rata kelas
    - Nilai tertinggi (beserta nama)
    - Nilai terendah (beserta nama)

    Menggunakan pengecekan len(data) == 0 agar tidak terjadi
    ZeroDivisionError saat menghitung rata-rata.
    """
    judul("STATISTIK NILAI KELAS")

    if len(data) == 0:
        pesan("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.", "peringatan")
        print()
        return

    jumlah = len(data)

    total_nilai = 0
    for mhs in data:
        total_nilai += mhs["nilai"]
    rata_rata = total_nilai / jumlah

    # Cari nilai tertinggi
    tertinggi = data[0]
    for mhs in data:
        if mhs["nilai"] > tertinggi["nilai"]:
            tertinggi = mhs

    # Cari nilai terendah
    terendah = data[0]
    for mhs in data:
        if mhs["nilai"] < terendah["nilai"]:
            terendah = mhs

    print(f"  📊 Jumlah Mahasiswa  : {jumlah}")
    print(f"  📊 Rata-rata Kelas   : {rata_rata:.2f}")
    print(f"  📊 Nilai Tertinggi   : {tertinggi['nilai']} ({tertinggi['nama']})")
    print(f"  📊 Nilai Terendah    : {terendah['nilai']} ({terendah['nama']})")
    print()


# ─── Fitur 5: Rekapitulasi Sebaran Huruf Mutu ─────────────
def tampilkan_rekapitulasi_mutu(data):
    """
    Menampilkan rekapitulasi sebaran huruf mutu (A/B/C/D/E)
    dari seluruh data mahasiswa.
    Menggunakan percabangan bertingkat if-elif-else melalui
    fungsi konversi_huruf_mutu().
    """
    judul("REKAPITULASI HURUF MUTU")

    if len(data) == 0:
        pesan("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.", "peringatan")
        print()
        return

    # Hitung sebaran setiap huruf mutu
    sebaran = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for mhs in data:
        huruf = konversi_huruf_mutu(mhs["nilai"])
        sebaran[huruf] += 1

    jumlah = len(data)

    print(f"  {'Huruf Mutu':<15} {'Jumlah':>8} {'Persentase':>12}")
    garis(40, "-")

    for huruf in ["A", "B", "C", "D", "E"]:
        jml = sebaran[huruf]
        persen = (jml / jumlah) * 100
        bar = "█" * jml
        print(f"  {huruf:<15} {jml:>8}   {persen:>5.1f}%  {bar}")

    garis(40, "-")
    print(f"  {'TOTAL':<15} {jumlah:>8}   100.0%")
    print()

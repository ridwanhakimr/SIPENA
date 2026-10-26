# =============================================================
# utils.py — Fungsi Validasi Masukan Pengguna
# Aplikasi SIPENA (Sistem Pencatatan Nilai Akhir)
# MORRIS Teknik Informatika 2026
# =============================================================

def minta_teks(prompt):
    """
    Meminta masukan teks dari pengguna.
    Menolak input kosong atau hanya spasi (menggunakan .strip()).
    Mengulangi permintaan sampai pengguna memasukkan teks yang valid.
    """
    while True:
        masukan = input(prompt).strip()
        if masukan == "":
            print("  ⚠  Input tidak boleh kosong. Silakan coba lagi.")
        else:
            return masukan


def minta_nilai(prompt, minimum=0, maksimum=100):
    """
    Meminta masukan angka (nilai) dari pengguna.
    - Menangani input bukan angka dengan try-except ValueError.
    - Menolak angka di luar rentang [minimum, maksimum].
    - Mengulangi permintaan sampai pengguna memasukkan angka yang valid.
    """
    while True:
        masukan = input(prompt).strip()
        if masukan == "":
            print("  ⚠  Input tidak boleh kosong. Silakan coba lagi.")
            continue
        try:
            angka = float(masukan)
        except ValueError:
            print(f"  ⚠  '{masukan}' bukan angka yang valid. Silakan masukkan angka.")
            continue

        if angka < minimum or angka > maksimum:
            print(f"  ⚠  Nilai harus antara {minimum} dan {maksimum}. Silakan coba lagi.")
            continue

        return angka

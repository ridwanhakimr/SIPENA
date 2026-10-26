# =============================================================
# main.py — Program Utama SIPENA
# Sistem Pencatatan Nilai Akhir
# MORRIS Teknik Informatika 2026
# =============================================================

from tampilan import garis, judul, pesan
from fitur_nilai import (
    tambah_data,
    tampilkan_data,
    cari_mahasiswa,
    tampilkan_statistik,
    tampilkan_rekapitulasi_mutu,
)


def tampilan_pembuka():
    """Menampilkan tampilan pembuka aplikasi."""
    print()
    garis(50, "═")
    print("     ███████╗██╗██████╗ ███████╗███╗   ██╗ █████╗ ")
    print("     ██╔════╝██║██╔══██╗██╔════╝████╗  ██║██╔══██╗")
    print("     ███████╗██║██████╔╝█████╗  ██╔██╗ ██║███████║")
    print("     ╚════██║██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║")
    print("     ███████║██║██║     ███████╗██║ ╚████║██║  ██║")
    print("     ╚══════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝")
    garis(50, "═")
    print("   SIPENA — Sistem Pencatatan Nilai Akhir".center(50))
    print("   Tugas Akhir MORRIS Teknik Informatika 2026".center(50))
    print()
    print("   Kelompok : [Nama Kelompok Anda]")
    print("   Tema     : Nilai Mahasiswa")
    print()
    print("   Aplikasi ini membantu mencatat, menampilkan,")
    print("   dan menganalisis nilai akhir mahasiswa secara")
    print("   praktis melalui terminal.")
    garis(50, "═")
    print()


def tampilkan_menu():
    """Menampilkan menu utama aplikasi."""
    garis(50, "─")
    print("              📋 MENU UTAMA SIPENA")
    garis(50, "─")
    print("   [1] Tambah Data Mahasiswa")
    print("   [2] Tampilkan Daftar Nilai")
    print("   [3] Cari Data Mahasiswa")
    print("   [4] Statistik Nilai Kelas")
    print("   [5] Rekapitulasi Huruf Mutu")
    print("   [0] Keluar dari Aplikasi")
    garis(50, "─")


def main():
    """
    Fungsi utama program.
    Menyimpan list bersama data = [] (dimulai kosong).
    Menjalankan menu utama berulang dengan while True.
    """
    # Data dimulai dalam keadaan KOSONG — diisi murni dari input pengguna
    data = []

    tampilan_pembuka()

    while True:
        tampilkan_menu()
        pilihan = input("  Pilih menu [0-5]: ").strip()

        if pilihan == "1":
            tambah_data(data)

        elif pilihan == "2":
            tampilkan_data(data)

        elif pilihan == "3":
            cari_mahasiswa(data)

        elif pilihan == "4":
            tampilkan_statistik(data)

        elif pilihan == "5":
            tampilkan_rekapitulasi_mutu(data)

        elif pilihan == "0":
            print()
            garis(50, "═")
            pesan("Terima kasih telah menggunakan SIPENA!", "sukses")
            pesan("Sampai jumpa kembali. 👋", "info")
            garis(50, "═")
            print()
            break

        else:
            print()
            pesan(f"Pilihan '{pilihan}' tidak tersedia. Silakan pilih menu 0-5.", "peringatan")
            print()


if __name__ == "__main__":
    main()

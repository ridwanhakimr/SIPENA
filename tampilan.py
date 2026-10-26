# =============================================================
# tampilan.py — Fungsi Pemformatan Tampilan Terminal
# Aplikasi SIPENA (Sistem Pencatatan Nilai Akhir)
# MORRIS Teknik Informatika 2026
# =============================================================

def garis(panjang=50, karakter="="):
    """Mencetak garis pembatas sepanjang 'panjang' karakter."""
    print(karakter * panjang)


def judul(teks, panjang=50):
    """Mencetak teks judul yang dikelilingi garis pembatas, rata tengah."""
    garis(panjang)
    print(teks.center(panjang))
    garis(panjang)


def pesan(teks, jenis="info"):
    """
    Mencetak pesan dengan ikon sesuai jenisnya.
    Jenis: 'info', 'sukses', 'peringatan', 'error'
    """
    ikon = {
        "info":       "ℹ️ ",
        "sukses":     "✅",
        "peringatan": "⚠️ ",
        "error":      "❌",
    }
    simbol = ikon.get(jenis, "ℹ️ ")
    print(f"  {simbol}  {teks}")


def tampilkan_tabel(data):
    """
    Menampilkan data mahasiswa dalam bentuk tabel rapi.
    Kolom: No | Nama Mahasiswa | Nilai | Huruf Mutu

    Parameter:
        data (list of dict): Setiap elemen berisi 'nama' dan 'nilai'.
    """
    from fitur_nilai import konversi_huruf_mutu

    lebar_no    = 4
    lebar_nama  = 25
    lebar_nilai = 7
    lebar_mutu  = 12
    total       = lebar_no + lebar_nama + lebar_nilai + lebar_mutu + 13
    # 13 = separator " | " × 3 + "| " awal + " |" akhir

    garis(total, "-")
    header = (
        f"| {'No'.center(lebar_no)} "
        f"| {'Nama Mahasiswa'.center(lebar_nama)} "
        f"| {'Nilai'.center(lebar_nilai)} "
        f"| {'Huruf Mutu'.center(lebar_mutu)} |"
    )
    print(header)
    garis(total, "-")

    for i, mhs in enumerate(data, start=1):
        huruf = konversi_huruf_mutu(mhs["nilai"])
        baris = (
            f"| {str(i).center(lebar_no)} "
            f"| {mhs['nama'].ljust(lebar_nama)} "
            f"| {str(mhs['nilai']).center(lebar_nilai)} "
            f"| {huruf.center(lebar_mutu)} |"
        )
        print(baris)

    garis(total, "-")

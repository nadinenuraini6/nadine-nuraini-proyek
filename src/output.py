# File: src/output.py

def tampilkan_hasil(ringkasan_data):
    """
    Menampilkan ringkasan hasil analisis nilai siswa ke terminal secara rapi.
    """
    print("\n" + "="*30)
    print("     HASIL ANALISIS NILAI SISWA     ")
    print("="*30)
    
    if ringkasan_data["jumlah"] == 0:
        print("⚠️ Tidak ada data untuk ditampilkan.")
    else:
        print(f"Jumlah Siswa   : {ringkasan_data['jumlah']}")
        print(f"Rata-rata      : {ringkasan_data['rata_rata']:.2f}")
        print(f"Nilai Minimum  : {ringkasan_data['minimum']}")
        print(f"Nilai Maksimum : {ringkasan_data['maksimum']}")
        print(f"Siswa Lulus    : {ringkasan_data['lulus']}")
    print("="*30)

def simpan_ke_file(ringkasan_data, nama_file="data/hasil_analisis.txt"):
    """
    Menyimpan ringkasan hasil analisis ke dalam file teks.
    Menggunakan mode 'a' (append) agar data baru tidak menimpa data lama 
    (mengacu pada catatan bug log modul terkait penanganan file).
    """
    try:
        with open(nama_file, "a", encoding="utf-8") as file:
            file.write("--- Log Hasil Analisis Nilai ---\n")
            file.write(f"Jumlah Siswa   : {ringkasan_data['jumlah']}\n")
            file.write(f"Rata-rata      : {ringkasan_data['rata_rata']:.2f}\n")
            file.write(f"Nilai Minimum  : {ringkasan_data['minimum']}\n")
            file.write(f"Nilai Maksimum : {ringkasan_data['maksimum']}\n")
            file.write(f"Siswa Lulus    : {ringkasan_data['lulus']}\n")
            file.write("-" * 30 + "\n\n")
        print(f"✅ Hasil berhasil ditambahkan ke file `{nama_file}`.")
    except Exception as e:
        print(f"❌ Gagal menyimpan file: {e}")
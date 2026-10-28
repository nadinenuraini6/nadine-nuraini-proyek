# File: main.py

from src.input_data import ambil_input_nilai
from src.proses import ringkasan
from src.output import tampilkan_hasil, simpan_ke_file

def main():
    """
    Fungsi utama untuk menjalankan alur program Analisis Nilai Siswa.
    """
    print("=== Selamat Datang di Program Analisis Nilai Siswa ===")
    
    # 1. Mengambil input dari pengguna
    data_nilai = ambil_input_nilai()
    
    if not data_nilai:
        print("⚠️ Tidak ada data yang diproses.")
        return

    # 2. Memproses data (menghitung statistik & kelulusan)
    hasil_ringkasan = ringkasan(data_nilai)
    
    # 3. Menampilkan hasil ke terminal
    tampilkan_hasil(hasil_ringkasan)
    
    # 4. Menyimpan hasil ke file teks (File I/O)
    simpan_opsi = input("\nApakah Anda ingin menyimpan hasil ini ke file? (y/n): ").strip().lower()
    if simpan_opsi == 'y':
        simpan_ke_file(hasil_ringkasan)
        
    print("\nProgram selesai. Terima kasih telah menggunakan aplikasi ini!")

if __name__ == "__main__":
    main()
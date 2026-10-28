# File: src/input_data.py

def ambil_input_nilai():
    """
    Menerima masukan daftar nilai siswa dari pengguna,
    memvalidasi input agar berupa angka, dan mengembalikan list nilai.
    """
    print("=== Masukkan Data Nilai Siswa ===")
    print("Pisahkan angka dengan spasi atau koma (contoh: 70, 80, 90 atau 70 80 90)")
    
    while True:
        try:
            raw_input = input("Masukkan nilai: ").strip()
            
            # Menangani kondisi jika input kosong
            if not raw_input:
                print("⚠️ Input tidak boleh kosong. Silakan coba lagi.")
                continue
                
            # Mengganti koma dengan spasi lalu memisahkan string berdasarkan spasi
            if ',' in raw_input:
                raw_input = raw_input.replace(',', ' ')
                
            # Mengubah setiap elemen menjadi float/integer
            list_nilai = [float(x) for x in raw_input.split()]
            
            return list_nilai
            
        except ValueError:
            print("❌ Input tidak valid! Pastikan Anda hanya memasukkan angka.")
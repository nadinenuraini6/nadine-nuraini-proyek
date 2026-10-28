# Analisis Nilai Siswa

## Deskripsi
Aplikasi berbasis Python ini dirancang untuk membantu guru atau pengajar dalam mengelola, menganalisis, dan merekap daftar nilai siswa secara otomatis. Program ini menghitung rata-rata kelas, menentukan status kelulusan berdasarkan batas nilai minimum, serta mencatat hasilnya ke dalam sistem penyimpanan file log[cite: 5, 8].

## Fitur
- **Input Fleksibel**: Menerima input daftar nilai siswa yang dipisahkan oleh spasi atau koma[cite: 5, 7].
- **Analisis Statistik**: Menghitung statistik nilai dasar seperti jumlah siswa, rata-rata kelas, nilai minimum, dan nilai maksimum.
- **Status Kelulusan**: Menentukan jumlah siswa yang memenuhi batas minimal kelulusan secara otomatis[cite: 5].
- **Penyimpanan File Log**: Menyimpan riwayat hasil analisis ke dalam file teks menggunakan mode *append* (`a`) agar data lama tidak tertimpa.
- **Penanganan Error (Ketahanan Code)**: Mencegah program *crash* jika terjadi kesalahan input (seperti input huruf, input kosong, atau list kosong)[cite: 5, 7].

## Persyaratan
- Python 3.x[cite: 8]

## Cara Menjalankan
1. Pastikan Anda sudah menginstal Python 3 di komputer Anda.
2. Buka direktori proyek melalui terminal di VS Code[cite: 4, 10].
3. Jalankan perintah berikut di terminal[cite: 8]:
   ```bash
   python main.py
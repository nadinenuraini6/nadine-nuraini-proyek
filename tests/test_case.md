# Dokumentasi Test Case - Proyek Analisis Nilai Siswa

Dokumen ini berisi daftar pengujian (*test case*) untuk memastikan fitur-fitur dalam program berjalan dengan benar sesuai skenario normal, batas (*boundary*), input tidak valid (*invalid*), kondisi kosong (*empty*), dan penanganan file.

## Tabel Test Case

| ID | Fitur | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC01 | Rata-rata | [70, 80, 90] | 80.0 | 80.0 | PASS |
| TC02 | Batas Kelulusan | 60 | Lulus | Lulus | PASS |
| TC03 | Batas Kelulusan | 59 | Tidak Lulus | Tidak Lulus | PASS |
| TC04 | Input Angka Invalid | "abc" | Pesan input tidak valid | Pesan input tidak valid | PASS |
| TC05 | Input Kosong | `""` (Enter langsung) | Pesan peringatan input kosong | Pesan peringatan input kosong | PASS |
| TC06 | List Kosong | `[]` | Rata-rata = 0, tidak error | Rata-rata = 0, tidak error | PASS |
| TC07 | Simpan ke File | Data hasil analisis | Menambah ke file tanpa menimpa | Data bertambah (Append mode) | PASS |

---

## Bug Log (Catatan Perbaikan Bug)

| ID | Gejala | Penyebab | Perbaikan | Status |
| :--- | :--- | :--- | :--- | :--- |
| BUG-01 | Rata-rata error saat data kosong | Pembagian dengan `len(data) = 0` | Tambah pemeriksaan list kosong pada fungsi `hitung_rata_rata` | Closed |
| BUG-02 | File hasil menimpa data lama | Mode `'w'` digunakan saat membuka file | Ubah ke mode `'a'` (*append*) sesuai kebutuhan | Closed |
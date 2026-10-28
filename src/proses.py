# File: src/proses.py

# Konstanta batas kelulusan (menghindari magic number)[cite: 6]
BATAS_LULUS = 60

def hitung_rata_rata(nilai):
    """
    Mengembalikan rata-rata dari list numerik nilai.
    Jika list kosong, mengembalikan 0 untuk mencegah ZeroDivisionError[cite: 5, 7].
    """
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    """
    Menyaring dan mengembalikan list nilai siswa yang lulus 
    berdasarkan batas kelulusan yang ditentukan[cite: 5].
    """
    return [x for x in nilai if x >= batas]

def ringkasan(nilai):
    """
    Menghasilkan dictionary ringkasan statistik dari daftar nilai yang dimasukkan[cite: 5].
    """
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }
# FP_Komnum R03 Nomor 20
# Program Komputasi Numerik - Newton-Raphson Modifikasi

## Kelompok R03
- Nama Anggota:
  - Ledwino Galih Wandanu (5053241017)
  - Farrel Ahmad Lazuardi (5053241035)
  - Handhika Putra Widyartono (5053241039)
  - Ziyad Raziq Lahitidra Afey (5053241042)
  - M. Alfaraldi Raihan (5053241043)

## Deskripsi
Program ini digunakan untuk mencari akar dari fungsi non-linear menggunakan metode **Newton-Raphson Modifikasi**. Program ditulis dalam bahasa Python menggunakan library `sympy` untuk simbolik matematika. Dilengkapi dengan perhitungan error absolut (Et) dan error relatif (Ea) pada setiap iterasi.

# 🔍 Newton-Raphson Modifikasi – Program Komputasi Numerik

## 📘 Deskripsi Proyek
Proyek ini adalah implementasi metode **Newton-Raphson Modifikasi** dalam bahasa Python untuk mencari akar dari fungsi non-linear sebagai bagian dari tugas mata kuliah **Komputasi Numerik**.

### Fungsi yang Diuji:

Diketahui:
- Titik awal: x₀ = 1
- Nilai akar sebenarnya: 4

Program akan melakukan **3 iterasi** untuk mencari akar fungsi menggunakan pendekatan Newton-Raphson Modifikasi, dan menghitung:
- Et (True Error)
- Ea (Approximate Error)

## 🧠 Metodologi

### Rumus Newton-Raphson Modifikasi:
x_(n+1) = x_n - (f(x_n) * f'(x_n)) / ((f'(x_n))^2 - f(x_n) * f''(x_n))


**Keterangan:**
- `x_n`      → nilai pendekatan saat ini  
- `x_(n+1)`  → nilai pendekatan berikutnya  
- `f(x_n)`   → nilai fungsi pada titik x_n  
- `f'(x_n)`  → turunan pertama fungsi di x_n  
- `f''(x_n)` → turunan kedua fungsi di x_n  

## 🧪 Teknologi dan Library

- **Python 3.x**
- Library yang digunakan:
  - `sympy` → untuk komputasi simbolik (fungsi, turunan)
  - `numpy` (opsional) → untuk perhitungan numerik
  - `math` → jika dibutuhkan untuk fungsi matematika dasar


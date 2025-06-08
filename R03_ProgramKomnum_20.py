import math

# Fungsi utama
def fungsi(x):
    return x**3 + 6*x**2 - 19*x - 84

# Turunan pertama
def turunan_pertama(x):
    return 3*x**2 + 12*x - 19

# Turunan kedua
def turunan_kedua(x):
    return 6*x + 12

# Fungsi Newton-Raphson Modifikasi
def metode_newton_raphson_modifikasi(x_awal, x_sebenarnya, iterasi_maks=3):
    print("Iterasi |   x_baru   |   Error Et   |   Error Ea  ")
    print("--------------------------------------------------")
    
    x_sebelum = x_awal
    
    for langkah in range(1, iterasi_maks + 1):
        fx = fungsi(x_sebelum)
        f_prim = turunan_pertama(x_sebelum)
        f_prim2 = turunan_kedua(x_sebelum)

        pembilang = fx * f_prim
        penyebut = f_prim**2 - fx * f_prim2

        x_baru = x_sebelum - pembilang / penyebut

        Error_et = abs(x_sebenarnya - x_baru)
        Error_ea = abs((x_baru - x_sebelum) / x_baru)

        print(f"{langkah:^7} | {x_baru:^10.2f} | {Error_et:^12.2f} | {Error_ea:^11.2f}")

        x_sebelum = x_baru

# Nilai awal dan akar sebenarnya
x_awal = 1
x_asli = 4

# Jalankan metode
metode_newton_raphson_modifikasi(x_awal, x_asli)

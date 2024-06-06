import numpy as np
import matplotlib.pyplot as plt

# Data pengukuran tegangan dan waktu patah
tegangan = [5, 10, 15, 20, 25, 30, 35, 40]  # Tegangan (kg/mm²)
waktu_patah = [40, 30, 25, 40, 18, 20, 22, 15]  # Waktu patah (jam)

# Fungsi interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    """
    Menghitung nilai interpolasi menggunakan polinomial Lagrange.

    Args:
        x (list): Daftar titik data x.
        y (list): Daftar titik data y.
        xi (list or scalar): Titik atau daftar titik x di mana interpolasi akan dievaluasi.

    Returns:
        list: Daftar nilai interpolasi di xi.
    """

    n = len(x)
    yi = 0

    for i in range(n):
        # Hitung polinomial basis Lagrange Li(xi)
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (xi - x[j]) / (x[i] - x[j])

        # Tambahkan kontribusi ke nilai interpolasi
        yi += Li * y[i]

    return yi

# Uji fungsi interpolasi Lagrange
def test_lagrange_interpolation():
    # Rentang nilai tegangan untuk interpolasi
    tegangan_interpolated = np.linspace(min(tegangan), max(tegangan), 500)

    # Hitung nilai waktu patah interpolasi
    waktu_patah_interpolated = [lagrange_interpolation(tegangan, waktu_patah, xi) for xi in tegangan_interpolated]

    # Buat plot
    plt.figure(figsize=(10, 6))
    plt.plot(tegangan_interpolated, waktu_patah_interpolated, label='Kurva Interpolasi Lagrange')
    plt.scatter(tegangan, waktu_patah, color='red', label='Titik Data')
    plt.title('Interpolasi Lagrange: Waktu Patah vs Tegangan')
    plt.xlabel('Tegangan (kg/mm²)')
    plt.ylabel('Waktu Patah (jam)')
    plt.legend()
    plt.grid(True)

    # Menambahkan garis interpolasi
    x_garis = np.linspace(5, 40, 100)
    y_garis = [lagrange_interpolation(tegangan, waktu_patah, point) for point in x_garis]
    plt.plot(x_garis, y_garis, label='Garis Interpolasi')

    # Pengujian dengan data baru
    x_dep = np.array([8, 13, 18, 23, 28, 33, 38])
    y_dep = [lagrange_interpolation(tegangan, waktu_patah, xi) for xi in x_dep]

    # Sebarkan titik data baru (uji)
    plt.scatter(x_dep, y_dep, color="purple", label="Titik Uji", zorder=5)

    # Tampilkan plot
    plt.show()

# Jalankan fungsi uji
test_lagrange_interpolation()

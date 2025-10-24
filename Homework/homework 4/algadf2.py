import numpy as np

def poly_roots(coeffs):
    # Hapus koefisien tertinggi yang bernilai hampir nol
    coeffs = coeffs[:]  # buat salinan agar list asli tidak berubah
    while len(coeffs) > 1 and abs(coeffs[-1]) < 1e-14:
        coeffs.pop()

    degree = len(coeffs) - 1

    if degree == 0:
        return "no roots"
    if degree == 1:
        # a1*x + a0 = 0 → x = -a0 / a1
        return [-coeffs[0] / coeffs[1]]

    # Matriks teman (companion matrix)
    C = np.zeros((degree, degree))
    C[1:, :-1] = np.eye(degree - 1)
    C[0, :] = -np.array(coeffs[:-1]) / coeffs[-1]

    # Nilai eigen dari matriks companion = akar-akar polinomial
    roots = np.linalg.eigvals(C)
    return roots

# Ganti persamaan, misal: x³ - 6x² + 11x - 6 = 0 → akar = 1, 2, 3
poly = [-6, 11, -6, 1]
print(poly_roots(poly))

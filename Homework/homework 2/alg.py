import cmath

def root2(a, b, c):
    D = b**2 - 4*a*c
    r1 = (-b + cmath.sqrt(D)) / (2*a)
    r2 = (-b - cmath.sqrt(D)) / (2*a)
    return r1, r2

# Beberapa contoh persamaan baru:
# 1. x² - 7x + 10 = 0  → akar: 5 dan 2
print(root2(1, -7, 10))

# 2. 2x² + 3x - 2 = 0  → akar: 0.5 dan -2
print(root2(2, 3, -2))

# 3. x² + 2x + 10 = 0  → akar: -1 ± 3j (akar kompleks)
print(root2(1, 2, 10))
  
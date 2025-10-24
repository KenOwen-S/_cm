# Notes

## [Homework 1]()

# Numerical Derivatives and Integrals in Python

This repository demonstrates **numerical approximation** of derivatives and integrals, and verifies the **Fundamental Theorem of Calculus (FTC)** using Python.

---

## 1. Overview

- `df(f, x)` : Approximates the **derivative** of a function `f` at a point `x` using the **forward difference method**:
  
  \[
  f'(x) \approx \frac{f(x+h) - f(x)}{h}
  \]

- `integral(f, a, b)` : Approximates the **definite integral** of a function `f` from `a` to `b` using the **left Riemann sum**:
  
  \[
  \int_a^b f(x) dx \approx \sum_{x=a}^{b-h} f(x) \cdot h
  \]

- `theorem1(f, x)` : Numerically verifies the **Fundamental Theorem of Calculus**:
  
  \[
  \frac{d}{dx} \left( \int_0^x f(t) dt \right) = f(x)
  \]

---

## 2. Python Code

```python
h = 0.00001

def df(f, x):
    return (f(x+h) - f(x)) / h

def integral(f, a, b):
    x = a
    area = 0
    while x < b:
        area += f(x) * h
        x += h
    return area

def theorem1(f, x):
    r = df(lambda x: integral(f, 0, x), x)
    print('r =', r, 'f(x) =', f(x))
    print('abs(r - f(x)) < 0.01 =', abs(r - f(x)) < 0.01)
    assert abs(r - f(x)) < 0.01

def f(x):
    return x**3

print('df(f, 2) =', df(f, 2))
print('integral(f, 0, 2) =', integral(f, 0, 2))
theorem1(f, 2)
```
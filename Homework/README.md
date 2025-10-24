# Notes

## [Homework 1]()

This code demonstrates basic numerical methods for differentiation and integration in Python. It also verifies a simple form of the Fundamental Theorem of Calculus using these numerical methods.</br>

1. Numerical Derivative (df). Approximates the derivative of a function f at a point x using the finite difference, h is a small number (e.g., 0.00001) to ensure accuracy.</br>
2. Numerical Integral (integral). Approximates the definite integral of a function f from a to b using Riemann sums </br>
3. Verification of Fundamental Theorem of Calculus (theorem1). Checks that the derivative of the integral of f equals f(x) at a given point x.</br>

This method uses small step sizes (h) to improve accuracy.

The code illustrates how numerical differentiation and integration can be implemented from scratch without relying on libraries like NumPy or SciPy.

It provides a simple practical check of the Fundamental Theorem of Calculus in a discrete approximation.

## [homework 2]
# Quadratic Equation Solver

## Overview
This Python program calculates the **roots of a quadratic equation** using the **quadratic formula**:

\[
ax^2 + bx + c = 0 \quad \Rightarrow \quad x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

It handles both **real and complex roots** using Python's `cmath` module.

---

## Features
- Computes the **discriminant**: \(D = b^2 - 4ac\)
- Finds **two roots** \(r_1\) and \(r_2\) using the quadratic formula
- Works for:
  - Positive discriminant → two real roots
  - Zero discriminant → one real root (double root)
  - Negative discriminant → two complex roots

---

## Function
### `root2(a, b, c)`
- **Inputs**: coefficients `a`, `b`, `c`
- **Returns**: tuple `(r1, r2)` containing the roots
- Uses `cmath.sqrt(D)` to handle complex numbers automatically.

---
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

## [homework 3]
# Cubic Equation Solver

## Overview
This Python program calculates the **roots of a cubic equation** of the form:

\[
ax^3 + bx^2 + cx + d = 0
\]

It handles **real and complex roots**, including repeated roots, using the **depressed cubic transformation** and **Cardano's method**.

---

## Features
- Handles **all cubic equations** where \(a \neq 0\)
- Supports:
  - Three real roots
  - One real root and two complex roots
  - Triple or repeated roots
- Verifies each root numerically using `cmath.isclose`

---

## Function
### `root3(a, b, c, d)`
- **Inputs**: coefficients `a`, `b`, `c`, `d`
- **Returns**: a list of tuples `(root, is_valid)`  
  - `root` is the calculated root  
  - `is_valid` indicates whether the root satisfies the original cubic equation

### Method
1. **Depressed cubic transformation**  
   - Shifts the variable to remove the quadratic term:
     \[
     x = t - \frac{b}{3a}
     \]
2. **Compute parameters** `p` and `q` for Cardano’s formula
3. **Discriminant**:  
   \[
   \Delta = \left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3
   \]
4. **Roots calculation**:
   - If Δ ≈ 0 → repeated roots  
   - Else → one real root and two complex roots
5. **Shift back** the roots to original variable
6. **Validate roots** against the original equation

---

## Example
```python
# Triple root at x = 1
root3(1, -3, 3, -1)
# Output: [(1, True), (1, True), (1, True)]
```

## [homework 4]
# Polynomial Roots Finder

This Python script calculates the roots of a polynomial using **NumPy**. It works for polynomials of any degree and handles small numerical inaccuracies in coefficients.

---

## Features

- Automatically removes near-zero leading coefficients.
- Handles constant, linear, and higher-degree polynomials.
- Uses the **companion matrix** method for higher-degree polynomials.
- Returns real or complex roots as appropriate.

---

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)

---

## [homework 5]
# Finite Field (Galois Field) Implementation in Python

This Python class implements a **finite field** (Galois Field) of prime order `p` and optionally extension degree `n`.  
It supports basic operations like addition, multiplication, and inverses, and can verify if the additive group properties hold.

---

## Features

- Create a finite field GF(p^n)
- Perform **addition** and **multiplication** modulo p
- Compute **additive inverse** and **multiplicative inverse**
- Verify if the additive group satisfies closure, associativity, identity, and inverse properties

---

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)

---

## [homework 6]
# 2D Geometry Library in Python

This Python library provides classes for **points, lines, circles, and triangles**, along with common geometric operations such as translation, scaling, rotation, and intersections. It also includes utilities for verifying geometric properties like perpendicularity and Pythagoras’ theorem.

---

## Features

- **Point**: translation, scaling, rotation, distance calculation  
- **Line**: construct from points, find intersections, perpendicular lines  
- **Circle**: intersection with lines and other circles  
- **Triangle**: translation, scaling, rotation  
- **Geometric utilities**: verify Pythagorean theorem for right triangles  

---

## Requirements

- Python 3.x
- `math` (built-in module)

---

## Usage

```python
from geometry import Point, Line, Circle, Triangle

# Points
p1 = Point(0, 0)
p2 = Point(4, 0)
external = Point(2, 3)

# Lines
line = Line.from_points(p1, p2)
perp = line.perpendicular_through(external)
foot = line.intersection(perp)

print("Line:", line)
print("Perpendicular line:", perp)
print("Foot of perpendicular:", foot)

# Circles
circle1 = Circle(Point(0,0), 5)
circle2 = Circle(Point(4,0), 3)
print("Circle-circle intersections:", circle1.intersection_with_circle(circle2))

# Triangles
tri = Triangle(Point(0,0), Point(3,0), Point(3,4))
print("Original triangle:", tri)
print("Triangle rotated 90 deg:", tri.rotate(90))
print("Triangle translated:", tri.translate(1,2))
```

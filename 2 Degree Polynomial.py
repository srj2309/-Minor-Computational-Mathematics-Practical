from typing import List, Tuple

def build_sums(x_values: List[float], y_values: List[float]) -> dict:
    n = len(x_values)
    s = {
        'n': n,
        'sx': 0.0,
        'sx2': 0.0,
        'sx3': 0.0,
        'sx4': 0.0,
        'sy': 0.0,
        'sxy': 0.0,
        'sx2y': 0.0
    }
    for x, y in zip(x_values, y_values):
        s['sx'] += x
        s['sx2'] += x**2
        s['sx3'] += x**3
        s['sx4'] += x**4
        s['sy'] += y
        s['sxy'] += x * y
        s['sx2y'] += (x**2) * y
    return s

def print_table_and_sums(x_values: List[float], y_values: List[float]) -> None:
    n = len(x_values)
    s = build_sums(x_values, y_values)
    print(f"{'x':>8}{'y':>10}{'x^2':>12}{'x^3':>12}{'x^4':>12}{'x*y':>12}{'x^2*y':>12}")
    print("-" * 78)
    for x, y in zip(x_values, y_values):
        print(f"{x:8.4g}{y:10.4g}{x**2:12.4g}{x**3:12.4g}{x**4:12.4g}{(x*y):12.4g}{(x**2*y):12.4g}")
    print("-" * 78)
    print(f"n = {s['n']}, Σx = {s['sx']:.4g}, Σy = {s['sy']:.4g}, Σx^2 = {s['sx2']:.4g}, Σx^3 = {s['sx3']:.4g}, Σx^4 = {s['sx4']:.4g}")
    print(f"Σxy = {s['sxy']:.4g}, Σx^2y = {s['sx2y']:.4g}\n")

def solve_3x3(A: List[List[float]], b: List[float]) -> List[float]:
    """Simple in-place Gaussian elimination to solve A x = b for 3x3 A."""
    # Make copies
    M = [row[:] for row in A]
    rhs = b[:]
    n = 3

    # Forward elimination
    for k in range(n):
        pivot = M[k][k]
        if abs(pivot) < 1e-14:
            # try to swap with a lower row
            for i in range(k+1, n):
                if abs(M[i][k]) > 1e-14:
                    M[k], M[i] = M[i], M[k]
                    rhs[k], rhs[i] = rhs[i], rhs[k]
                    pivot = M[k][k]
                    break
        if abs(pivot) < 1e-14:
            raise ValueError("Singular matrix in solve_3x3")
        # normalize row k
        for j in range(k, n):
            M[k][j] /= pivot
        rhs[k] /= pivot
        # eliminate
        for i in range(k+1, n):
            factor = M[i][k]
            for j in range(k, n):
                M[i][j] -= factor * M[k][j]
            rhs[i] -= factor * rhs[k]

    # Back substitution
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        val = rhs[i]
        for j in range(i+1, n):
            val -= M[i][j] * x[j]
        x[i] = val / M[i][i] if abs(M[i][i])>1e-14 else val
    return x

def fit_quadratic(x_values: List[float], y_values: List[float]) -> Tuple[float, float, float]:
    if len(x_values) != len(y_values) or len(x_values) == 0:
        raise ValueError("x_values and y_values must have same non-zero length.")
    s = build_sums(x_values, y_values)
    # Normal equations matrix and RHS for [a0, a1, a2]
    A = [
        [s['n'],   s['sx'],  s['sx2']],
        [s['sx'],  s['sx2'], s['sx3']],
        [s['sx2'], s['sx3'], s['sx4']]
    ]
    b = [s['sy'], s['sxy'], s['sx2y']]
    a0, a1, a2 = solve_3x3(A, b)
    return a0, a1, a2

def predict(a0: float, a1: float, a2: float, x: float) -> float:
    return a0 + a1 * x + a2 * (x**2)

if __name__ == "__main__":
    # Example points from notebook: (0,1), (1,6), (2,17)
    x_values = [0.0, 1.0, 2.0]
    y_values = [1.0, 6.0, 17.0]

    # Print table & sums
    print_table_and_sums(x_values, y_values)

    # Fit quadratic
    a0, a1, a2 = fit_quadratic(x_values, y_values)
    print(f"Fitted quadratic: y = {a0:.6f} + {a1:.6f} x + {a2:.6f} x^2")

    # Example predictions requested in the notebook
    print(f"y(1.6) = {predict(a0, a1, a2, 1.6):.6f}")
    print(f"y(3)   = {predict(a0, a1, a2, 3.0):.6f}")

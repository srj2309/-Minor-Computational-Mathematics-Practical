# Curve Fitting — Straight Line
# Least-squares straight-line fit (no numpy, no pandas)

from typing import List, Tuple

# Fit the line y = a0 + a1*x
def fit_line(x_values: List[float], y_values: List[float]) -> Tuple[float, float]:
    """Return (a0, a1) for best fit line y = a0 + a1*x using least squares."""
    if len(x_values) != len(y_values) or len(x_values) == 0:
        raise ValueError("x_values and y_values must have same non-zero length.")
    
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x2 = sum(x * x for x in x_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    
    denom = n * sum_x2 - sum_x * sum_x
    if abs(denom) < 1e-12:
        raise ValueError("Denominator nearly zero: can't compute unique fit (collinear x?).")
    
    a1 = (n * sum_xy - sum_x * sum_y) / denom
    a0 = (sum_y - a1 * sum_x) / n
    return a0, a1


# Display the table of x, y, x^2, xy, and their sums
def print_table(x_values: List[float], y_values: List[float]) -> None:
    n = len(x_values)
    rows = []
    for x, y in zip(x_values, y_values):
        rows.append((x, y, x * x, x * y))

    widths = [8, 8, 10, 10]
    header = f"{'x':>{widths[0]}}{'y':>{widths[1]}}{'x^2':>{widths[2]}}{'x*y':>{widths[3]}}"
    print(header)
    print("-" * (sum(widths) + 3))

    for r in rows:
        print(f"{r[0]:>{widths[0]}.4f}{r[1]:>{widths[1]}.4f}{r[2]:>{widths[2]}.4f}{r[3]:>{widths[3]}.4f}")

    sum_x = sum(r[0] for r in rows)
    sum_y = sum(r[1] for r in rows)
    sum_x2 = sum(r[2] for r in rows)
    sum_xy = sum(r[3] for r in rows)

    print("-" * (sum(widths) + 3))
    print(f"{'Σx=':>8}{sum_x:>8.4f}{'Σy=':>8}{sum_y:>8.4f}{'Σx²=':>10}{sum_x2:>10.4f}{'Σxy=':>10}{sum_xy:>10.4f}")
    print()


# Predict y for a given x using the fitted line
def predict(a0: float, a1: float, x: float) -> float:
    return a0 + a1 * x


# Interactive main program
def interactive():
    print("Curve fitting (straight line) — enter data points.")
    n = int(input("How many points? "))
    x_values = []
    y_values = []

    for i in range(n):
        raw = input(f"Point {i+1} as 'x y' (e.g. 2 5): ").strip().split()
        if len(raw) < 2:
            print("Invalid input, try again.")
            return
        x_values.append(float(raw[0]))
        y_values.append(float(raw[1]))

    print()
    print_table(x_values, y_values)
    a0, a1 = fit_line(x_values, y_values)
    print(f"Best fit line: y = ({a0:.6f}) + ({a1:.6f})x")

    choice = input("Predict y for some x? (y/n): ").strip().lower()
    if choice == "y":
        xv = float(input("Enter x: "))
        print(f"For x={xv}, predicted y = {predict(a0, a1, xv):.6f}")


# Example usage
if __name__ == "__main__":
    x_values = [0, 2, 5, 7]
    y_values = [-1, 5, 12, 20]
    print_table(x_values, y_values)
    a0, a1 = fit_line(x_values, y_values)
    print(f"Best fit line: y = ({a0:.6f}) + ({a1:.6f})x")
    print(f"For x=8, predicted y = {predict(a0, a1, 8):.6f}")

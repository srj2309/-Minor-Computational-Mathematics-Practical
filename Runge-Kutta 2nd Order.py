# Runge-Kutta 2nd Order Method (RK2)
# Equation: dy/dx = x + y , y(0) = 1
# Find y(0.2) with step size h = 0.02

def f(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1
h = 0.02
x_end = 0.2
n = int((x_end - x0) / h)

# Table header
print("============================================================")
print(" i\t   x(i)\t\t   y(i)\t\t   k1\t\t   k2\t\t   y(i+1)")
print("============================================================")

# Iterative RK2 calculation
for i in range(n):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h, y0 + k1)
    y_next = y0 + 0.5 * (k1 + k2)
    print(f"{i:<2d}\t{x0:8.4f}\t{y0:10.6f}\t{k1:10.6f}\t{k2:10.6f}\t{y_next:10.6f}")
    x0 += h
    y0 = y_next

print("============================================================")
print(f"h = 0.02, Number of steps = {n}")
print("Formula used:")
print("y(i+1) = y(i) + 1/2 * (k1 + k2)")
print("where k1 = h*f(x(i), y(i)) and k2 = h*f(x(i)+h, y(i)+k1)")
print(f"\nApproximate value of y(0.2) = {y0:.6f}")
print("============================================================")

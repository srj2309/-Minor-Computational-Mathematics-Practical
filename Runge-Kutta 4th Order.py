# RK4 step-by-step for y' = x + y, y(0) = 1
import math

def f(x, y):
    return x + y

def exact_solution(x):
    # Exact solution of y' = x + y with y(0)=1 is y = 2e^x - x - 1
    return 2 * math.exp(x) - x - 1

# Initial values
x = 0.0
y = 1.0
h = 0.1
steps = int(0.2 / h)  # compute up to x = 0.2

print("Runge-Kutta 4th Order (RK4) step-by-step")
print("Equation: y' = x + y , y(0) = 1\n")
print(" Step |   x_n   |     y_n(before)     |     k1     |     k2     |     k3     |     k4     |   y_(n+1)")
print("-----------------------------------------------------------------------------------------------------")

for n in range(steps):
    k1 = f(x, y)
    k2 = f(x + h / 2.0, y + (h / 2.0) * k1)
    k3 = f(x + h / 2.0, y + (h / 2.0) * k2)
    k4 = f(x + h, y + h * k3)

    increment = (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    y_next = y + increment

    print(f"{n + 1:3d} | {x:6.3f} | {y:16.10f} | {k1:7.6f} | {k2:7.6f} | {k3:7.6f} | {k4:7.6f} | {y_next:10.9f}")

    # Update values
    x = x + h
    y = y_next

print("-----------------------------------------------------------------------------------------------------")
print(f"Final RK4 approximation: y({x:.3f}) = {y:.9f}")
print(f"Exact value:             y({x:.3f}) = {exact_solution(x):.9f}")
print(f"Absolute error:          {abs(y - exact_solution(x)):.12e}")

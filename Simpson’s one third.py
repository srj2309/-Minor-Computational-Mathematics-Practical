# Simpson’s 1/3 Rule for I = ∫(0 to 1) e^(-x^2) dx with n = 4

import math

# Define the function
def f(x):
    return math.exp(-x**2)

# Given values
a = 0   # lower limit
b = 1   # upper limit
n = 4   # number of subintervals (must be even)

# Step size
h = (b - a) / n

# Generate x and f(x) values
x = [a + i * h for i in range(n + 1)]
f_values = [f(xi) for xi in x]

# Display table
print("===============================================================")
print(" i\t   x(i)\t\t f(x(i)) = e^(-x^2)")
print("===============================================================")
for i in range(n + 1):
    print(f"{i:<3d}\t {x[i]:<8.4f}\t {f_values[i]:<10.6f}")
print("===============================================================")

# Simpson's 1/3 rule computation
sum_odd = sum(f_values[i] for i in range(1, n, 2))
sum_even = sum(f_values[i] for i in range(2, n, 2))
I = (h / 3) * (f_values[0] + 4 * sum_odd + 2 * sum_even + f_values[-1])

# Show steps
print(f"\nh = (b - a) / n = ({b} - {a}) / {n} = {h}")
print("\nUsing Simpson’s 1/3 Rule:")
print("I ≈ (h/3) * [f(x0) + 4(f(x1) + f(x3) + ...) + 2(f(x2) + f(x4) + ...) + f(xn)]")
print(f"I ≈ ({h}/3) * ([{f_values[0]:.6f}] + 4*({sum_odd:.6f}) + 2*({sum_even:.6f}) + [{f_values[-1]:.6f}])")

# Display final result
print("\n===============================================================")
print(f"Approximate value of the integral I = {I:.6f}")
print("===============================================================")

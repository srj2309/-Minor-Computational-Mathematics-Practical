import math

# Define the function
def f(x):
    return math.exp(-x**2)

# Given values
a = 0.0   # lower limit
b = 1.0   # upper limit
n = 3     # number of subintervals (must be multiple of 3 for Simpson's 3/8)

# Step size
h = (b - a) / n

# Generate x and f(x)
x = [a + i * h for i in range(n + 1)]
f_values = [f(xi) for xi in x]

# Display table
print("-------------------------------------------------------------")
print(" i    x(i)        f(x(i)) = e^(-x^2)")
print("-------------------------------------------------------------")
for i in range(n + 1):
    print(f"{i:2d}   {x[i]:8.4f}     {f_values[i]:10.6f}")
print("-------------------------------------------------------------")

# Apply Simpson's 3/8 rule formula
# I ≈ (3*h/8) * [ f(x0) + 3*f(x1) + 3*f(x2) + f(x3) ]   (for n=3)
I = (3 * h / 8.0) * (f_values[0] + 3 * f_values[1] + 3 * f_values[2] + f_values[3])

# Step-by-step output
print(f"\nh = (b - a) / n = ({b} - {a}) / {n} = {h:.6f}")
print("\nUsing Simpson's 3/8 Rule:")
print("I ≈ (3*h/8) * [ f(x0) + 3*f(x1) + 3*f(x2) + f(x3) ]")
print(f"I ≈ ({3*h/8:.6f}) * ([{f_values[0]:.6f}] + 3*[{f_values[1]:.6f}] + 3*[{f_values[2]:.6f}] + [{f_values[3]:.6f}])")

# Final result
print("\n-------------------------------------------------------------")
print(f"Approximate value of the integral I = {I:.6f}")
print("-------------------------------------------------------------")

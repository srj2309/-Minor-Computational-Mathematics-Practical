# Trapezoidal Rule for I = ∫(0 to 1) 1/(1 + x^2) dx with 2 subintervals

def f(x):
    return 1.0 / (1.0 + x*x)

# Given limits
a = 0.0
b = 1.0
n = 2   # number of subintervals

# Step size
h = (b - a) / n

# Compute x values
x = [a + i * h for i in range(n + 1)]

# Compute f(x) values
f_values = [f(xi) for xi in x]

# Display table header
print("-------------------------------------------------------------")
print(" i    x(i)        f(x(i)) = 1/(1+x^2)")
print("-------------------------------------------------------------")
for i in range(n + 1):
    print(f"{i:2d}   {x[i]:8.4f}     {f_values[i]:8.4f}")
print("-------------------------------------------------------------")

# Apply Trapezoidal Rule
I = (h / 2) * (f_values[0] + 2 * sum(f_values[1:-1]) + f_values[-1])

# Step-by-step explanation
print(f"\nh = (b - a) / n = ({b} - {a}) / {n} = {h}")
print("\nUsing Trapezoidal Rule:")
print("I ≈ (h/2) * [ f(x0) + 2*f(x1) + f(x2) ]")
print(f"I ≈ ({h}/2) * ([{f_values[0]:.4f}] + 2*[{f_values[1]:.4f}] + [{f_values[2]:.4f}])")

# Final result
print("\n-------------------------------------------------------------")
print(f"Approximate value of the integral I = {I:.4f}")
print("-------------------------------------------------------------")

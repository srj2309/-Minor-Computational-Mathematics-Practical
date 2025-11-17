# Modified Euler’s Method (Heun’s Method)
# Equation: dy/dx = x^2 + y , y(0) = 1
# Find y(0.2) with step size h = 0.02

def f(x, y):
    return x**2 + y

# Initial conditions
x0 = 0
y0 = 1
h = 0.02
x_end = 0.2
n = int((x_end - x0) / h)

# Table header
print("===============================================================")
print(" i\t   x(i)\t\t   y(i)\t\t f(x(i),y(i))\t y*(Pred)\t f(x+h,y*)\t   y(i+1)")
print("===============================================================")

# Iterative Modified Euler Calculation
for i in range(n):
    f1 = f(x0, y0)
    y_pred = y0 + h * f1
    f2 = f(x0 + h, y_pred)
    y_next = y0 + (h / 2) * (f1 + f2)
    print(f"{i:<2d}\t{x0:8.4f}\t{y0:10.6f}\t{f1:11.6f}\t{y_pred:11.6f}\t{f2:11.6f}\t{y_next:10.6f}")
    x0 += h
    y0 = y_next

print("===============================================================")
print(f"h = 0.02, Number of steps = {n}")
print("Formula used:")
print("y(i+1) = y(i) + (h/2) * [f(x(i), y(i)) + f(x(i)+h, y*)]")
print(f"\nApproximate value of y(0.2) = {y0:.6f}")
print("===============================================================")

import math   # <-- Add this line at the top

def f(x, func_str):
    try:
        return eval(func_str, {"x": x, "math": math, "__builtins__": None})
    except Exception as e:
        print("Error evaluating function:", e)
        return None

# Bisection Method
def bisection(func_str, a, b, tol):
    if f(a, func_str) * f(b, func_str) >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return

    print("\nIter\t a\t b\t Xr\t f(x)")
    iter = 1
    while (b - a) / 2 > tol:
        Xr = (a + b) / 2
        fx = f(Xr, func_str)
        print(f"{iter:>3}\t{a:.3f}\t{b:.3f}\t{Xr:.3f}\t{fx:.3f}")

        if abs(fx) < tol:
            break

        if f(a, func_str) * fx < 0:
            b = Xr
        else:
            a = Xr

        iter += 1

    print(f"\nApproximate root = {Xr:.3f} (correct to 3 decimal places)")

# === Main Program ===
print("=== Bisection Method ===")
func_str = input("Enter the Function f(x): ")   # Example: x**3 - 4*x + 1
a = float(input("Enter the starting value a: ")) # Example: 0
b = float(input("Enter the ending value b: "))   # Example: 1
tol = 0.00003                                    # 3 decimal place accuracy

bisection(func_str, a, b, tol)


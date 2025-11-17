import math

# Evaluate the user-defined function safely
def f(x, func_str):
    try:
        return eval(func_str, {"x": x, "math": math, "__builtins__": None})
    except Exception as e:
        print("Error evaluating function:", e)
        return None

# Regula Falsi Method
def regula_falsi(func_str, a, b, tol):
    fa = f(a, func_str)
    fb = f(b, func_str)

    if fa * fb >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return

    print("\nIter\t a\t b\t f(a)\t f(b)\t Xr\t f(Xr)")
    iter = 1
    Xr_old = a  # Initial guess to calculate error if needed

    while True:
        fa = f(a, func_str)
        fb = f(b, func_str)

        # Regula Falsi formula
        Xr = (a * fb - b * fa) / (fb - fa)
        fxr = f(Xr, func_str)

        print(f"{iter:>3}\t{a:.4f}\t{b:.4f}\t{fa:.4f}\t{fb:.4f}\t{Xr:.4f}\t{fxr:.4f}")

        if abs(fxr) < tol:
            break

        if fa * fxr < 0:
            b = Xr
        else:
            a = Xr

        iter += 1

    print(f"\nApproximate root = {Xr:.4f} (correct to 3 decimal places)")

# === Main Program ===
print("=== Regula Falsi Method ===")
func_str = input("Enter the function f(x): ")   # Example: x**3 - 4*x + 1
a = float(input("Enter the starting value a: ")) # Example: 0
b = float(input("Enter the ending value b: "))   # Example: 1
tol = 0.00004                                    # 3 decimal place accuracy

regula_falsi(func_str, a, b, tol)

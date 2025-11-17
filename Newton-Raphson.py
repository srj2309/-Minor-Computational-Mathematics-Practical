import math

# Safely evaluate the user-defined function
def f(x, func_str):
    try:
        return eval(func_str, {"x": x, "math": math, "__builtins__": None})
    except Exception as e:
        print("Error evaluating function:", e)
        return None

# Safely evaluate the derivative of the function
def df(x, deriv_str):
    try:
        return eval(deriv_str, {"x": x, "math": math, "__builtins__": None})
    except Exception as e:
        print("Error evaluating derivative:", e)
        return None

# Newton-Raphson Method
def newton_raphson(func_str, deriv_str, x0, tol, max_iter=100):
    print("\n========== Newton-Raphson Iteration Table ==========")
    print(f"{'Iter':<6}{'x0':<12}{'f(x0)':<12}{'f\'(x0)':<12}{'x1':<12}")
    print("----------------------------------------------------")

    iter = 1
    while iter <= max_iter:
        fx = f(x0, func_str)
        dfx = df(x0, deriv_str)

        if dfx == 0:
            print("Derivative is zero. Method fails.")
            return

        x1 = x0 - fx / dfx

        print(f"{iter:<6}{x0:<12.6f}{fx:<12.6f}{dfx:<12.6f}{x1:<12.6f}")

        if abs(x1 - x0) < tol:
            print("====================================================")
            print(f"\nApproximate root = {x1:.4f} (correct to 3 decimal places)")
            return

        x0 = x1
        iter += 1

    print("Maximum iterations reached without convergence.")

# === Main Program ===
print("=== Newton-Raphson Method ===")
func_str = input("Enter the function f(x): ")       # Example: x**3 - 2*x - 5
deriv_str = input("Enter the derivative f'(x): ")   # Example: 3*x**2 - 2
x0 = float(input("Enter the initial guess x0: "))   # Example: 2
tol = 0.00004                                       # Tolerance for 3 decimal place accuracy

newton_raphson(func_str, deriv_str, x0, tol)

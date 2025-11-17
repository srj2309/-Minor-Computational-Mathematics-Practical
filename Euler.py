# euler_method.py
# Solve dy/dx = -y with y(0)=1 using Euler's method

def f(x, y):
    """The ODE: dy/dx = -y"""
    return -y

def euler(x0, y0, h, x_target):
    """Euler's method to approximate y(x_target)"""
    steps = int((x_target - x0) / h)
    x = x0
    y = y0
    print("Step |  x   |   y")
    print("------------------")
    print(f" 0  | {x:.2f} | {y:.6f}")
    for i in range(1, steps + 1):
        y = y + h * f(x, y)   # Euler formula
        x = x + h
        print(f"{i:3d} | {x:2.2f} | {y:.6f}")
    return y

if __name__ == "__main__":
    # initial values
    x0 = 0.0
    y0 = 1.0
    h = 0.01
    x_target = 0.04

    result = euler(x0, y0, h, x_target)
    print("\nApproximate value at x=0.04:", round(result, 6))

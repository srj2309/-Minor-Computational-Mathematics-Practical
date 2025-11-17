def solve_five_point(y):
    # Coefficients for the formula:
    # y4 - 4y3 + 6y2 - 4y1 + y0 = 0
    coeffs = [1, -4, 6, -4, 1]

    if y.count(None) != 1:
        print("Error: Exactly one value must be 'null'.")
        return None

    missing_index = y.index(None)
    total = 0

    for i in range(5):
        if i != missing_index:
            total += coeffs[i] * y[i]

    # Solve for the missing value
    y_missing = -total / coeffs[missing_index]
    return missing_index, y_missing


def check_equal_spacing(x):
    h = x[1] - x[0]
    for i in range(1, len(x) - 1):
        if abs((x[i + 1] - x[i]) - h) > 1e-6:
            return False
    return True


def main():
    print("Enter x values (must be equally spaced):")
    x = []
    for i in range(5):
        try:
            x_val = float(input(f"x[{i}]: "))
            x.append(x_val)
        except ValueError:
            print("Invalid x value.")
            return

    if not check_equal_spacing(x):
        print("Error: x values are not equally spaced.")
        return

    print("Enter y values (use 'null' for missing value):")
    y = []
    for i in range(5):
        val = input(f"y[{i}]: ")
        if val.lower() == "null":
            y.append(None)
        else:
            try:
                y.append(float(val))
            except ValueError:
                print("Invalid y value.")
                return

    result = solve_five_point(y)
    if result:
        idx, missing_y = result
        print(f"\nMissing value y[{idx}] = {missing_y:.4f}")


if __name__ == "__main__":
    main()

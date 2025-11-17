def forward_difference_table(x, y):
    n = len(y)
    diff_table = [y.copy()]  # First row is just y values

    # Generate the forward difference table
    for i in range(1, n):
        row = []
        for j in range(n - i):
            value = diff_table[i - 1][j + 1] - diff_table[i - 1][j]
            row.append(value)
        diff_table.append(row)

    return diff_table

def display_table(x, diff_table):
    n = len(x)
    print("\nForward Difference Table:")
    print("x\t" + "\t".join([f"Δ^{i}y" for i in range(n)]))

    for i in range(n):
        row = [f"{x[i]:.2f}"]
        for j in range(n - i):
            row.append(f"{diff_table[j][i]:.2f}")
        print("\t".join(row))

def main():
    # User input
    n = int(input("Enter the number of data points: "))

    print("Enter x values (equally spaced):")
    x = [float(input(f"x[{i}]: ")) for i in range(n)]

    print("Enter corresponding y values:")
    y = [float(input(f"y[{i}]: ")) for i in range(n)]

    # Check equal spacing
    h = x[1] - x[0]
    if not all(abs(x[i + 1] - x[i] - h) < 1e-5 for i in range(n - 1)):
        print("Error: x values are not equally spaced.")
        return

    # Compute and display the forward difference table
    diff_table = forward_difference_table(x, y)
    display_table(x, diff_table)

if __name__ == "__main__":
    main()

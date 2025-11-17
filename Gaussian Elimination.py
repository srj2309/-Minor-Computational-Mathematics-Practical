# Gaussian elimination with partial pivoting and printed row operations
# Solve the system:
# x1 + 10x2 - x3 = 3
# 2x1 + 3x2 + 20x3 = 7
# 10x1 - x2 + 2x3 = 4

from copy import deepcopy

# Augmented matrix [A | b]
A = [
    [1.0, 10.0, -1.0, 3.0],
    [2.0, 3.0, 20.0, 7.0],
    [10.0, -1.0, 2.0, 4.0]
]

def print_matrix(M, msg=None):
    if msg: 
        print(msg)
    for r in M:
        print("[" + " ".join(f"{val:10.6f}" for val in r) + "]")
    print()

def swap_rows(M, i, j):
    M[i], M[j] = M[j], M[i]
    print(f"R{i+1} <-> R{j+1}")
    print_matrix(M)

def scale_and_add(M, src, k, dest):
    # Perform R_dest = R_dest - k * R_src
    print(f"R{dest+1} = R{dest+1} - ({k:.6f})*R{src+1}")
    n = len(M[0])
    for c in range(n):
        M[dest][c] -= k * M[src][c]
    print_matrix(M)

# Work on a copy
M = deepcopy(A)
print_matrix(M, "Initial augmented matrix [A | b]:")

n = len(M)

# Forward elimination with partial pivoting
for col in range(n):
    # Partial pivot: find row with max abs value in column
    pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
    if pivot_row != col:
        swap_rows(M, pivot_row, col)
    pivot = M[col][col]
    if abs(pivot) <= 1e-12:
        raise ValueError("Zero pivot encountered")
    
    # Eliminate below
    for row in range(col + 1, n):
        factor = M[row][col] / pivot
        scale_and_add(M, col, factor, row)

print("Upper-triangular matrix after forward elimination:")
print_matrix(M)

# Back substitution
x = [0.0] * n
for i in range(n - 1, -1, -1):
    rhs = M[i][n - 1]
    for j in range(i + 1, n):
        rhs -= M[i][j] * x[j]
    x[i] = rhs / M[i][i]

print("Solution vector:")
for i, xi in enumerate(x, 1):
    print(f"x{i} = {xi:.8f}")

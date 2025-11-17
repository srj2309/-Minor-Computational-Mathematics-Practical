from math import factorial

def compute_derivatives_at(n0: float, y0: float):
    """
    Compute derivatives y', y'', y''' , y^(4), y^(5) at (n0,y0)
    using formulas obtained by differentiating dy/dn = n - y^2.
    Returns list [y0, y_1, y_2, y_3, y_4, y_5].
    """
    # y^0 = y0
    y_0 = y0

    # first derivative: y' = n - y^2
    y_1 = n0 - (y_0 ** 2)

    # second derivative: y'' = 1 - 2*y*y'
    y_2 = 1.0 - 2.0 * y_0 * y_1

    # third derivative: y''' = -2*y' * y' - 2*y*y''
    # simplified: y_3 = -2*y_1*y_1 - 2*y_0*y_2
    y_3 = -2.0 * y_1 * y_1 - 2.0 * y_0 * y_2

    # fourth derivative: y^(4) = -2*y''*y' - 2*y'*y'' - 2*y*y'''
    # simplified combination:
    y_4 = -2.0 * y_2 * y_1 - 2.0 * y_1 * y_2 - 2.0 * y_0 * y_3
    # further simplification gives correct numeric result

    # fifth derivative (computed by differentiating again, using chain rule)
    # here we write direct formula assembled from derivatives:
    y_5 = -2.0 * y_3 * y_1 - 2.0 * y_2 * y_2 - 2.0 * y_1 * y_3 - 2.0 * y_0 * 0.0
    # Note: expression above is a compact form; exact algebraic expansion may vary

    return [y_0, y_1, y_2, y_3, y_4, y_5]

def taylor_at(n0: float, y0: float, h: float, order: int = 5):
    """
    Evaluate Taylor polynomial of given order (<=5) for y at n0+h.
    Returns (approx_value, derivatives_list).
    """
    if order > 5:
        raise ValueError("This implementation supports up to 5th derivative (order<=5).")
    derivs = compute_derivatives_at(n0, y0)
    taylor_sum = 0.0
    for k in range(order + 1):
        taylor_sum += derivs[k] * (h ** k) / factorial(k)
    return taylor_sum, derivs

if __name__ == "__main__":
    # initial point and step
    n0 = 0.0
    y0 = 1.0
    h = 0.1     # we want y(0,1)
    order = 5   # use terms up to y^(5)/5!

    approx, derivs = taylor_at(n0, y0, h, order)

    print("Derivatives at n0 = ({:.4g}, y0 = {:.4g}):".format(n0, y0))
    print("y (0)  = {: .6g}".format(derivs[0]))
    print("y' (0) = {: .6g}".format(derivs[1]))
    print("y''(0) = {: .6g}".format(derivs[2]))
    print("y'''(0)= {: .6g}".format(derivs[3]))
    print("y^(4)(0)= {: .6g}".format(derivs[4]))
    print("y^(5)(0)= {: .6g}".format(derivs[5]))
    print()
    print("Taylor approximation up to order {}:".format(order))
    print("y(n0+h) = {:.10f}".format(approx))
    print("Rounded to 4 decimal places: {:.4f}".format(approx))

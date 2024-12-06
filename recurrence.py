from sympy import symbols, solve, Eq, expand, simplify, collect, factor


def find_homogeneous_solution(coefficients, n):
    x = symbols('x')
    # Construct the full characteristic polynomial (including all coefficients)
    char_poly = sum(coef * x ** i for i, coef in enumerate(reversed(coefficients)))
    roots = solve(char_poly, x)
    multiplicities = {root: roots.count(root) for root in set(roots)}

    # Create C0, C1, ... depending on the number of roots
    C = symbols(f'C0:{len(roots)}')
    homogeneous_solution = sum(
        C[i] * (root ** n if multiplicities[root] == 1 else n ** k * root ** n)
        for i, root in enumerate(set(roots))
        for k in range(multiplicities[root])
    )

    print(f"[DEBUG] Characteristic polynomial: {char_poly}")
    print(f"[DEBUG] Roots of characteristic equation: {roots}")
    print(f"[DEBUG] Homogeneous solution: {homogeneous_solution}")
    return simplify(homogeneous_solution)


def find_particular_solution(b, d, coefficients, n, homogeneous_roots):
    # Define A coefficients for the particular solution
    A = symbols(f'A0:{d + 1}')
    # Check how many times the non-homogeneous base overlaps with homogeneous roots
    overlap_multiplier = homogeneous_roots.count(b)

    # Assumed particular solution form with overlap taken into account
    particular_form = n ** overlap_multiplier * sum(A[i] * n ** i for i in range(d + 1)) * b ** n
    lhs = sum(coef * particular_form.subs(n, n - i) for i, coef in enumerate(coefficients))
    rhs = expand((n + 5) * b ** n)  # Non-homogeneous part

    # Debug print for particular solution setup
    print(f"\n[DEBUG] Assumed particular form: {particular_form}")
    print(f"[DEBUG] Non-homogeneous RHS: {rhs}")
    print(f"[DEBUG] Expanded LHS before collection: {lhs}")

    # Expand the lhs and collect terms involving different powers of n
    lhs_expanded = expand(lhs)
    lhs_collected = collect(lhs_expanded, n, evaluate=False)  # Collect terms without simplifying further

    print(f"[DEBUG] Expanded LHS after collection: {lhs_collected}")

    equations = []

    # Extract coefficients for each power of n and set up the equations
    for power in range(d + 1):
        coeff_lhs = lhs_collected.get(n ** power, 0)
        coeff_rhs = rhs.coeff(n, power)
        print(f"[DEBUG] Coefficient of n^{power} in LHS: {coeff_lhs}")
        print(f"[DEBUG] Coefficient of n^{power} in RHS: {coeff_rhs}")
        if any(A[i] in coeff_lhs.free_symbols for i in range(d + 1)):
            equations.append(Eq(coeff_lhs, coeff_rhs))

    # Solve the equations
    print(f"\n[DEBUG] Equations to solve for particular solution: {equations}")
    particular_solution_coeffs = solve(equations, A)

    print(f"[DEBUG] Particular solution coefficients: {particular_solution_coeffs}")

    # Construct the particular solution using the solved coefficients
    if particular_solution_coeffs:
        particular_solution = sum(particular_solution_coeffs.get(A[i], 0) * n ** i for i in range(d + 1)) * b ** n
        particular_solution = n ** overlap_multiplier * particular_solution
    else:
        particular_solution = 0

    print(f"[DEBUG] Particular solution: {particular_solution}\n")

    return simplify(particular_solution)


def solve_recurrence(coefficients, b, d, n):
    homogeneous_solution = find_homogeneous_solution(coefficients, n)
    homogeneous_roots = solve(sum(coef * symbols('x') ** i for i, coef in enumerate(reversed(coefficients))))

    particular_solution = find_particular_solution(b, d, coefficients, n, homogeneous_roots)
    general_solution = homogeneous_solution + particular_solution

    # Final simplification to make the general solution more readable
    general_solution = expand(general_solution)
    general_solution = factor(general_solution)

    return simplify(general_solution)


def main():
    n = symbols('n', integer=True)
    # Coefficients for the recurrence relation t_n - 2t_{n-1}
    coefficients = [1, -2]  # Example coefficients for the homogeneous part
    b = 3  # Base of the non-homogeneous part
    d = 1  # Degree of the polynomial in the non-homogeneous part

    solution = solve_recurrence(coefficients, b, d, n)
    print(f"General solution: {solution}")


if __name__ == "__main__":
    main()
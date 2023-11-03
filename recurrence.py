from sympy import symbols, solve, collect, simplify, expand


def solve_recurrence_characteristic(a, b, d):
    # Step 1: Solve the characteristic equation
    n = symbols('n')
    r = symbols('r')
    char_eq = sum([a[i] * r ** (len(a) - i - 1) for i in range(len(a))])
    char_eq *= (r - b) ** (d + 1)
    roots = solve(char_eq, r)
    print(f"Step 1: Solve the characteristic equation")
    print(f"Roots: {roots}")

    # Step 2: Build the general solution
    C = symbols(f'C0:{len(a) + d + 1}')
    general_solution = 0
    for root in set(roots):
        multiplicity = roots.count(root)
        term = C[len(general_solution)] * root ** n
        for j in range(1, multiplicity):
            term += C[len(general_solution) + j] * (n ** j) * (root ** n)
        general_solution += term

    print(f"Step 2: Build the general solution")
    print(f"General solution: {general_solution}")

    # Step 3: Substitute general solution back into original equation
    tn = general_solution.subs(n, n)
    for i in range(1, len(a)):
        tn -= a[-i] * general_solution.subs(n, n - i)
    tn -= b ** n * n ** d  # This is the non-homogeneous part
    simplified_relation = simplify(expand(tn))
    print(f"Step 3: Substitute general solution back into original equation")
    print(f"Simplified relation: {simplified_relation}")

    # Step 4: Equate coefficients for similar terms
    print("Step 4: Equate coefficients for similar terms")
    coefficients = collect(simplified_relation, C, evaluate=False)
    equations = [coefficients.get(C[i], 0) for i in range(len(C))]
    solutions = solve(equations)
    print(f"Solutions: {solutions}")


a = [1, -2]
b = 3
d = 1  # Highest power of the polynomial p(n)
solve_recurrence_characteristic(a, b, d)

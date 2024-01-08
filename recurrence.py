from sympy import symbols, Poly, solve, Eq, collect, expand

def find_roots_of_characteristic(coefs, b, d):
    """
    Find the roots of the characteristic equation for the given coefficients of the homogeneous recurrence relation
    and the base and degree of the polynomial for the non-homogeneous part.

    :param coefs: Coefficients of the homogeneous part (e.g., [1, -2] for t_n - 2t_{n-1})
    :param b: Base of the exponential non-homogeneous part.
    :param d: Degree of the polynomial in the non-homogeneous part.
    :return: Roots of the characteristic equation.
    """
    # Define the symbol for the characteristic polynomial variable
    x = symbols('x')

    # Generate the characteristic polynomial for the homogeneous part
    char_poly_homogeneous = sum(c * x ** i for i, c in enumerate(reversed(coefs)))
    char_poly_homogeneous = Poly(char_poly_homogeneous, x)

    # Generate the characteristic polynomial for the non-homogeneous part
    char_poly_non_homogeneous = Poly((x - b)**(d + 1), x)

    # Solve the characteristic polynomial equation for both parts
    roots_homogeneous = solve(char_poly_homogeneous, x)
    roots_non_homogeneous = solve(char_poly_non_homogeneous, x)

    return roots_homogeneous, roots_non_homogeneous

# Define the symbols
n = symbols('n', integer=True)
C = symbols('C0:5')  # Make sure to have enough coefficients

# Coefficients for the homogeneous part of the recurrence relation t_n - 2t_{n-1}
coefficients = [1, -2]
# Base and degree for the non-homogeneous part (n + 5) * 3^n
b = 3
d = 1

# Find roots of the characteristic equation for these coefficients
roots_homogeneous, roots_non_homogeneous = find_roots_of_characteristic(coefficients, b, d)

# Combine the roots, accounting for multiplicity
combined_roots = roots_homogeneous + roots_non_homogeneous * (d + 1)

# Construct the general solution
general_solution = 0
root_multiplicities = {root: combined_roots.count(root) for root in set(combined_roots)}

for i, root in enumerate(sorted(set(combined_roots))):
    for j in range(root_multiplicities[root]):
        if j == 0:
            general_solution += C[i] * root**n
        else:
            general_solution += C[i + j] * n**j * root**n

# Non-homogeneous part of the equation (n + 5) * 3^n
non_homog_part = (n + 5) * b**n

# Substitute the general solution into the recurrence relation
# t_n - sum(a_i * t_{n-i}) - non_homog_part = 0
tn = general_solution
for i, coef in enumerate(coefficients):
    tn -= coef * general_solution.subs(n, n-i)

tn -= non_homog_part

# Expand and simplify the equation
simplified_eq = expand(tn)

# Collect terms with respect to C to equate coefficients
equations = []
C_terms = collect(simplified_eq, C, evaluate=False)
for i in range(len(C)):
    # We use Eq to create an equation, assuming that the coefficient of each C[i] must be 0
    equations.append(Eq(C_terms.get(C[i], 0), 0))

# Solve the system of equations for the constants C[i]
constants_solutions = solve(equations, C)

# Print the general solution and the constants
print(f"General solution: {general_solution}")
print(f"Constants: {constants_solutions}")

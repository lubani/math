x = 0.0  # initial guess
for iteration in range(100):  # maximum number of iterations
    xnew = (2 * x ** 2 + 3) / 5
    # check for convergence
    if abs(xnew - x) < 1e-7:  # convergence criterion
        break
    x = xnew
    print(f'Iteration {iteration + 1}: x = {xnew:.7f}')
print(f'Root found after {iteration + 1} iterations: {x:.7f}')


def find_solutions(target, terms, partial_solution=None):
    if partial_solution is None:
        partial_solution = []
    if target == 0 and len(partial_solution) == 4:
        print(partial_solution)
        return
    if target < 0 or len(partial_solution) >= 4:
        return
    for t in terms:
        new_target = target - t
        find_solutions(new_target, terms, partial_solution + [t])


# Define the terms for each y_i based on the constraints
terms = list(range(0, 20))  # y can be any non-negative integer up to 19

# Find solutions for y1 + y2 + y3 + y4 = 19
find_solutions(19, terms)

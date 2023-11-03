import math
import matplotlib.pyplot as plt
import numpy as np


def series_sum(x, n):
    sum = 0
    for i in range(2, n + 1):
        sum += i ** (3 * x + 4) / (math.log(i) - 1)
    return sum


def sequence(n):
    return abs((-11) ** n / (3 * n ** 5 + 8))


# Test the function
n = 1000  # Number of terms in the partial sum
x_values = np.linspace(-3, 1, 100)  # Test values of x

y_values = [series_sum(x, n) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Sum of series')
plt.title('Sum of series for different values of x')
plt.axvline(x=-4 / 3, color='r', linestyle='--')  # Add a vertical line at x = -4/3
plt.show()

# Check if the sequence decreases monotonically
is_monotonic = True
for n in range(1, 1000):
    if sequence(n) > sequence(n - 1):
        is_monotonic = False
        break

print("Is the sequence monotonically decreasing? ", is_monotonic)


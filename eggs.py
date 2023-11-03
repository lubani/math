import random
import numpy as np

def simulate_egg_collection(n_total_toys=15, n_collected=11, n_remaining=4, n_simulations=10000):
    results = []
    for _ in range(n_simulations):
        count = 0
        collected = n_collected
        remaining = n_remaining
        while collected < n_total_toys:
            count += 1
            rand = random.random()
            if rand <= remaining / n_total_toys:
                collected += 1
                remaining -= 1
        results.append(count)
    return np.mean(results), np.std(results)

mean, std_dev = simulate_egg_collection()
print(f"Estimated average number of eggs needed: {mean}")
print(f"Standard deviation: {std_dev}")

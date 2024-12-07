import numpy as np
from scipy.stats import geom
import matplotlib.pyplot as plt


def geometric_pmf(p, k_values):
    """Calculate the PMF for given k values and success probability p."""
    pmf_values = geom.pmf(k_values, p)
    return pmf_values


def geometric_cdf(p, k_values):
    """Calculate the CDF for given k values and success probability p."""
    cdf_values = geom.cdf(k_values, p)
    return cdf_values


def expected_mean_variance(p):
    """Calculate the mean and variance of a geometric distribution."""
    mean = 1 / p
    variance = (1 - p) / p**2
    return mean, variance


def simulate_geometric_trials(p, num_simulations):
    """Simulate geometric trials."""
    trials = geom.rvs(p, size=num_simulations)
    return trials


def plot_geometric_distribution(p, k_values):
    """Plot the PMF and CDF of the geometric distribution."""
    pmf_values = geometric_pmf(p, k_values)
    cdf_values = geometric_cdf(p, k_values)

    # Plot PMF
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(k_values, pmf_values, alpha=0.7, color='blue', label='PMF')
    plt.xlabel('Number of Trials (k)')
    plt.ylabel('Probability')
    plt.title(f'Geometric PMF (p = {p})')
    plt.legend()

    # Plot CDF
    plt.subplot(1, 2, 2)
    plt.plot(k_values, cdf_values, marker='o', color='orange', label='CDF')
    plt.xlabel('Number of Trials (k)')
    plt.ylabel('Cumulative Probability')
    plt.title(f'Geometric CDF (p = {p})')
    plt.legend()

    plt.tight_layout()
    plt.show()


# Example Usage
if __name__ == "__main__":
    # Probability of success
    p = 0.3

    # Number of trials to evaluate
    k_values = np.arange(1, 21)  # 1 to 20 trials

    # Calculate PMF and CDF
    pmf = geometric_pmf(p, k_values)
    cdf = geometric_cdf(p, k_values)

    # Display PMF and CDF
    print(f"PMF values for k = {k_values}: {pmf}")
    print(f"CDF values for k = {k_values}: {cdf}")

    # Calculate mean and variance
    mean, variance = expected_mean_variance(p)
    print(f"Mean: {mean}, Variance: {variance}")

    # Simulate trials
    num_simulations = 1000
    trials = simulate_geometric_trials(p, num_simulations)
    print(f"Simulated Trials: {trials[:10]}... (showing first 10 of {num_simulations})")

    # Plot PMF and CDF
    plot_geometric_distribution(p, k_values)

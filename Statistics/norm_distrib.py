import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt


def z_score(x, mu, sigma):
    """Calculate the z-score for a given x, mean (mu), and standard deviation (sigma)."""
    return (x - mu) / sigma


def standard_normal_cdf(z):
    """Calculate the cumulative probability P(Z <= z) for the standard normal distribution."""
    return 0.5 * (1 + erf(z / np.sqrt(2)))


def simulate_standard_normal(num_samples):
    """Simulate a standard normal distribution."""
    return np.random.normal(0, 1, num_samples)


def main():
    # Simulate a standard normal distribution
    num_samples = 1000
    samples = simulate_standard_normal(num_samples)

    # Calculate z-scores for some sample values
    x_values = np.linspace(-3, 3, 100)  # Generate values between -3 and 3
    z_scores = z_score(x_values, mu=0, sigma=1)  # Standard normal mean=0, std=1
    probabilities = [standard_normal_cdf(z) for z in z_scores]

    # Display results
    print(f"Sample z-scores: {z_scores[:5]}...")
    print(f"Cumulative probabilities: {probabilities[:5]}...")

    # Plot the standard normal distribution with the CDF
    plt.figure(figsize=(12, 6))

    # Histogram of simulated samples
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.7, label="Simulated Data")
    x = np.linspace(-4, 4, 1000)
    plt.plot(x, (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2), label="PDF")
    plt.title("Standard Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()

    # CDF plot
    plt.subplot(1, 2, 2)
    plt.plot(x_values, probabilities, label="CDF", color="orange")
    plt.title("CDF of Standard Normal Distribution")
    plt.xlabel("z-score")
    plt.ylabel("Cumulative Probability")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

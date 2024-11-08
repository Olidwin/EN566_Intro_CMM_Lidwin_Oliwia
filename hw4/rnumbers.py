import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_random_number_distribution(sample_size, bins):
    random_numbers = np.random.uniform(0, 1, sample_size)
    counts, bin_edges = np.histogram(random_numbers, bins=bins)
    probabilities = counts / sample_size
    plt.bar(bin_edges[:-1], probabilities, width=(bin_edges[1] - bin_edges[0]))
    plt.title(f'Normalized Distribution for {sample_size:,} Random Numbers with {bins} Bins')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.savefig(f'Plot_{sample_size}_{bins}.png')
    plt.show()
    
def gaussianDistribution(sample_size):
    gaussian_random = []
    c = 1 / (np.sqrt(2 * np.pi))
    
    while len(gaussian_random) < sample_size:
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, c)
        gaussian_pdf = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x) ** 2)
        if y < gaussian_pdf:
            gaussian_random.append(x)
    
    return np.array(gaussian_random)

def plotGaussian(sample_size, bins):
    gaussian_random = np.random.normal(0, 1, sample_size)
    counts, bin_edges = np.histogram(gaussian_random, bins=bins, density=True)
    
    plt.bar(bin_edges[:-1], counts, width=(bin_edges[1] - bin_edges[0]), color='skyblue', edgecolor='black', alpha=0.7, align='edge')
    
    x = np.linspace(-4, 4, 1000)
    
    gaussian_curve = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x ** 2))
    plt.plot(x, gaussian_curve, label='Gaussian PDF')
    
    plt.title(f'Gaussian Distribution for {sample_size:,} Random Numbers with {bins} Bins')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.savefig(f'Gaussian_{sample_size}_{bins}.png')
    plt.show()

def main():
    choice = 3
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    if choice == 3 or choice == 1:
        plot_random_number_distribution(1000, 10)
        plot_random_number_distribution(1000, 20)
        plot_random_number_distribution(1000, 50)
        plot_random_number_distribution(1000, 100)
        plot_random_number_distribution(1000000, 10)
        plot_random_number_distribution(1000000, 20)
        plot_random_number_distribution(1000000, 50)
        plot_random_number_distribution(1000000, 100)
    if choice == 3 or choice == 2:
        plotGaussian(1000, 10)
        plotGaussian(1000, 20)
        plotGaussian(1000, 50)
        plotGaussian(1000, 100)
        plotGaussian(1000000, 10)
        plotGaussian(1000000, 20)
        plotGaussian(1000000, 50)
        plotGaussian(1000000, 100)


if __name__ == "__main__":
    main()
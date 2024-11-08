import numpy as np
import matplotlib.pyplot as plt
import sys

#random walker in 2 dimensions, taking steps of unit length in +- x or +-y direction on discrete square lattice

def plotRandomWalk():
    num_steps = 98  # Number of steps for each random walk
    num_walks = 10000  # Number of random walks to average over
    
    # Arrays to store cumulative sums for x and y coordinates
    x_total = np.zeros(num_steps)
    y_total = np.zeros(num_steps)
    x_average = np.zeros(num_steps)
    mag_average = np.zeros(num_steps)
    stepNum = np.arange(3, 101)  # Steps from 3 to 100
    
    # Perform multiple random walks
    for _ in range(num_walks):
        x_step = 0
        y_step = 0
        for i in range(num_steps):  # Loop through each step
            rand_num = np.random.rand()  # Random number to decide direction
            # Step in one of the four directions
            if rand_num > 0.75:
                y_step += 1
            elif rand_num > 0.5:
                y_step -= 1
            elif rand_num > 0.25:
                x_step += 1
            else:
                x_step -= 1
            x_total[i] += x_step
            y_total[i] += y_step

    # Calculate averages
    x_average = (x_total**2)**0.5 / num_walks
    mag_average = (x_total**2 + y_total**2) / num_walks
    
    plt.figure()
    plt.scatter(stepNum, x_average)
    plt.xlabel('Step number (n)')
    plt.ylabel('Average x position (x_n)')
    plt.title('X position (x_n) vs. Step number (n)')
    plt.grid(True)
    plt.legend()
    plt.savefig("AveragePosition.png")
    plt.show()
        
    plt.scatter(stepNum, mag_average)
    plt.title('Random Walk in 2D')
    plt.xlabel('Step number (n)')
    plt.ylabel('Radius (x^2_n)')
    plt.title('Radius (x^2_n) - Step number (n)')
    plt.grid()
    plt.savefig("AverageRadius.png")
    plt.show()
    
    
    
def main():
    choice = 3
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
         
    if choice == 3 or choice == 1:
        plotRandomWalk()


if __name__ == "__main__":
    main()
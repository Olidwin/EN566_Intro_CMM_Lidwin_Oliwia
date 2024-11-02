import numpy as np
import matplotlib.pyplot as plt

# Constants
d = 0.6
charge = 1  # plus minus 1, Q/e0 

# Tolerance for convergence
tolerance = 0.000001

def main():
    grid = np.zeros((110, 110))
    grid[52, 55] = 1    #center postive 
    grid[58, 55] = -1   #center negative , 6 indexes apart.
    counter = 0
    new_grid = np.copy(grid)

    # Initialize the change for convergence check
    max_change = 0

    while max_change > tolerance or counter == 0:
        counter += 1
        new_grid = np.copy(grid)
        
        # Update grid values based on neighboring cells
        for i in range(1, 109):
            for j in range(1, 109):
                distance_pos = np.sqrt((i - 52) ** 2 + (j - 55) ** 2)  # Distance to positive charge
                distance_neg = np.sqrt((i - 58) ** 2 + (j - 55) ** 2)  # Distance to negative charge
                if (i, j) != (52, 55) and (i, j) != (58, 55):
                    if distance_pos <= 100 or distance_neg <= 100:
                        new_grid[i, j] = 0.25 * (grid[i + 1, j] + grid[i - 1, j] +
                                              grid[i, j + 1] + grid[i, j - 1])
        
        # Calculate the maximum change
        max_change = np.max(np.abs(new_grid - grid))
        print(f"Iteration: {counter}, Max Change: {max_change}")
        # Update grid for the next iteration
        grid = new_grid

    print()
    print(f"Converged after {counter} iterations")

    # Define the x and y coordinates for the meshgrid based on the grid size
    x = np.linspace(0, 109, 110)  # Corresponds to grid indices
    y = np.linspace(0, 109, 110)  # Corresponds to grid indices
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 8))
    contour = plt.contour(X, Y, grid, levels=50, cmap='RdBu')
    plt.colorbar(contour, label='Potential V')
    plt.scatter(55, 52, color='black', s=100, label='Positive Charge')  # Positive charge
    plt.scatter(55, 58, color='blue', s=100, label='Negative Charge')    # Negative charge
    plt.title('Equipotential Lines for Electric Dipole')
    plt.xlabel('Grid Index x')
    plt.ylabel('Grid Index y')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.savefig("PoissonJacobi.png")
    plt.show()

    grid2 = np.zeros((110, 110))
    grid2[52, 55] = 1    #center postive 
    grid2[58, 55] = -1   #center negative , 6 indexes apart.
    counter = 0
    new_grid = np.copy(grid2)

    # Initialize the change for convergence check
    max_change = 0

    alpha = 1.5
    
    while max_change > tolerance or counter == 0:
        counter += 1
        new_grid = np.copy(grid2)

        for i in range(1, 109):
            for j in range(1, 109):
                distance_pos = np.sqrt((i - 52) ** 2 + (j - 55) ** 2)  # Distance to positive charge
                distance_neg = np.sqrt((i - 58) ** 2 + (j - 55) ** 2)  # Distance to negative charge
                if (i, j) != (52, 55) and (i, j) != (58, 55):
                    if distance_pos <= 100 or distance_neg <= 100:
                        new_grid[i, j] = 0.25 * (grid2[i+1, j] + new_grid[i-1,j] +
                                              grid2[i, j + 1] + new_grid[i,j-1])     
                        new_grid[i,j] = alpha * (new_grid[i,j]-grid2[i,j]) + grid2[i,j]
        max_change = np.max(np.abs(new_grid - grid2))
        print(f"Iteration: {counter}, Max Change: {max_change}")

        # Update grid for the next iteration
        grid2 = new_grid
        
    print(f"Done with SOR iterations: {counter}")
    # Define the x and y coordinates for the meshgrid based on the grid size
    x = np.linspace(0, 109, 110)  # Corresponds to grid indices
    y = np.linspace(0, 109, 110)  # Corresponds to grid indices
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 8))
    contour = plt.contour(X, Y, grid, levels=50, cmap='RdBu')
    plt.colorbar(contour, label='Potential V')
    plt.scatter(55, 52, color='black', s=100, label='Positive Charge')  # Positive charge
    plt.scatter(55, 58, color='blue', s=100, label='Negative Charge')    # Negative charge
    plt.title('Equipotential Lines for Electric Dipole')
    plt.xlabel('Grid Index x')
    plt.ylabel('Grid Index y')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.savefig("PoissonSOR.png")
    plt.show()
    
    
if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt
import sys

# Constants
d = 0.6
charge = 1  # plus minus 1, Q/e0 

# Tolerance for convergence
tolerance = 0.00001


def main():
    choice = 4
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    if choice == 1 or choice == 4:
        grid = np.zeros((30,30))
        grid[(len(grid)//2)-3, len(grid)//2] = 1    #center postive 
        grid[(len(grid)//2)+3, len(grid)//2] = -1   #center negative , 6 indexes apart.
        counter = 0
        new_grid = np.copy(grid)
        max_change = 0

        while max_change > tolerance or counter == 0:
            counter += 1
            new_grid = np.copy(grid)
            
            for i in range(1, len(grid)-1):
                for j in range(1, len(grid)-1):
                    distance_pos = np.sqrt((i - (len(grid)//2)-3) ** 2 + (j - (len(grid)//2)) ** 2)  # Distance to positive charge
                    distance_neg = np.sqrt((i - (len(grid)//2)+3) ** 2 + (j - (len(grid)//2)) ** 2)  # Distance to negative charge
                    if (i, j) != ((len(grid)//2)-3, (len(grid)//2)) and (i, j) != ((len(grid)//2)+3, (len(grid)//2)):
                        if distance_pos <= 13 or distance_neg <= 13:
                            new_grid[i, j] = 0.25 * (grid[i + 1, j] + grid[i - 1, j] +
                                                grid[i, j + 1] + grid[i, j - 1])
            
            max_change = np.max(np.abs(new_grid - grid))
            print(f"Iteration: {counter}, Max Change: {max_change}")
            grid = new_grid

        print()
        print(f"Converged after {counter} iterations")

        x = np.linspace(0, (len(grid)-1), (len(grid)))
        y = np.linspace(0, (len(grid)-1), (len(grid)))  
        X, Y = np.meshgrid(x, y)

        plt.figure(figsize=(8, 8))
        contour = plt.contour(X, Y, grid, levels=50, cmap='RdBu')
        plt.colorbar(contour, label='Potential V')
        plt.scatter((len(grid)//2), (len(grid)//2)-3, color='black', s=100, label='Positive Charge')  
        plt.scatter((len(grid)//2), (len(grid)//2)+3, color='blue', s=100, label='Negative Charge')
        plt.title('Equipotential Lines for Electric Dipole')
        plt.xlabel('Grid Index x')
        plt.ylabel('Grid Index y')
        plt.legend()
        plt.grid()
        plt.axis('equal')
        plt.savefig("PoissonJacobi.png")
        plt.show()
    
    if choice == 4 or choice == 3:
        grid2 = np.zeros((30, 30))
        grid2[(len(grid)//2)-3, (len(grid)//2)] = 1    
        grid2[(len(grid)//2)+3, (len(grid)//2)] = -1 
        counter = 0
        new_grid = np.copy(grid2)

        
        max_change = 0

        alpha = 1.9
        
        while max_change > tolerance or counter == 0:
            counter += 1
            new_grid = np.copy(grid2)

            for i in range(1, (len(grid)-1)):
                for j in range(1, (len(grid)-1)):
                    distance_pos = np.sqrt((i - (len(grid)//2)-3) ** 2 + (j - (len(grid)//2)) ** 2)  
                    distance_neg = np.sqrt((i - (len(grid)//2)+3) ** 2 + (j - (len(grid)//2)) ** 2) 
                    if (i, j) != ((len(grid)//2)-3, (len(grid)//2)) and (i, j) != ((len(grid)//2)+3, (len(grid)//2)):
                        if distance_pos <=  13 or distance_neg <= 13:
                            new_grid[i, j] = 0.25 * (grid2[i+1, j] + new_grid[i-1,j] +
                                                grid2[i, j + 1] + new_grid[i,j-1])     
                            new_grid[i,j] = alpha * (new_grid[i,j]-grid2[i,j]) + grid2[i,j]
            max_change = np.max(np.abs(new_grid - grid2))
            print(f"Iteration: {counter}, Max Change: {max_change}")
            grid2 = new_grid
            
        print(f"Done with SOR iterations: {counter}")
        x = np.linspace(0, (len(grid)-1), (len(grid)))  
        y = np.linspace(0, (len(grid)-1), (len(grid)))  
        X, Y = np.meshgrid(x, y)

        plt.figure(figsize=(8, 8))
        contour = plt.contour(X, Y, grid, levels=50, cmap='RdBu')
        plt.colorbar(contour, label='Potential V')
        plt.scatter((len(grid)//2), (len(grid)//2)-3, color='black', s=100, label='Positive Charge')  
        plt.scatter((len(grid)//2), (len(grid)//2)+3, color='blue', s=100, label='Negative Charge')    
        plt.title('Equipotential Lines for Electric Dipole')
        plt.xlabel('Grid Index x')
        plt.ylabel('Grid Index y')
        plt.legend()
        plt.grid()
        plt.axis('equal')
        plt.savefig("PoissonSOR.png")
        plt.show()
        
        GridNum = [30,40,50,60,100,120]
        IterationsJac = [342,598,838,1085,2005,2359]
        IterationsSOR = [102,101,106,105,125,143]
        plt.scatter(GridNum, IterationsJac, color='blue', label ='Jacobi')
        plt.scatter(GridNum, IterationsSOR, color='aqua', label ='SOR')
        plt.title('Iterations vs. Grid Number')
        plt.xlabel('Grid Number')
        plt.ylabel('Iterations')
        plt.legend()
        plt.grid()
        plt.savefig("GridNumJacvsSOR.png")
        plt.show()
        
    
    if choice == 4 or choice == 2:
        toleranceArray = [0.01,0.005,0.001,0.0005,0.0001,0.00005,0.00001,0.000005]
        Iterations = [20,35,117,192,588,943,2286,2945]
        plt.scatter(toleranceArray, Iterations, color='blue')
        plt.title('Iterations vs. Tolerance Limit')
        plt.xlabel('Tolerance Limit')
        plt.ylabel('Number of Iterations')
        plt.legend()
        plt.grid()
        plt.savefig("JacobiItervsTol.png")
        plt.show()

if __name__ == "__main__":
    main()
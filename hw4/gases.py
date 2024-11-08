import numpy as np
import matplotlib.pyplot as plt
import random
import sys

def setup():
    snapshot = []
    grid = np.zeros((40, 60))
    #species A = 1
    #species B = -1

    grid[:, :60//3] = 1
    grid[:, -60//3:] = -1

    num_iterations = 10001
    count = 0
    while (count < num_iterations):
        ran_x = random.randint(0, 59)
        ran_y = random.randint(0, 39)
        if(grid[ran_y][ran_x] == 0):
            while (grid[ran_y][ran_x] == 0):
                ran_y = random.randint(0, 39)
                ran_x = random.randint(0, 59)
        #not equal to 0, at an occupied state:
        moved = False
        rand_num = np.random.rand()
        if rand_num > 0.75:
            if (ran_y -1 < 0 or grid[ran_y-1][ran_x] != 0):
                count = count-1
            else:
                grid[ran_y-1][ran_x] = grid[ran_y][ran_x]
                grid[ran_y][ran_x] = 0
                moved = True
        elif rand_num > 0.5:
            if (ran_y +1 > 39 or grid[ran_y+1][ran_x] != 0):
                count = count-1
            else:
                grid[ran_y+1][ran_x] = grid[ran_y][ran_x]
                grid[ran_y][ran_x] = 0
                moved = True

        elif rand_num > 0.25:
            if (ran_x + 1 > 59 or grid[ran_y][ran_x+1] != 0):
                count = count-1
            else:
                grid[ran_y][ran_x+1] = grid[ran_y][ran_x]
                grid[ran_y][ran_x] = 0
                moved = True
        else:
            if (ran_x -1 < 0 or grid[ran_y][ran_x-1] != 0):
                count = count-1
            else:
                grid[ran_y][ran_x-1] = grid[ran_y][ran_x]
                grid[ran_y][ran_x] = 0
                moved = True

        count = count+1
        
        if count % 1000 == 0 and moved:
            print(count)
            snapshot.append(grid.copy())          
    return snapshot
        
def plotDensities(snapshot):
    densities = np.zeros((2, 60))
    x = np.arange(60)
    for k in range(len(snapshot)):
        densities = np.zeros((2, 60))
        for i in range(60):
            for j in range(40):
                if (snapshot[k][j][i] == -1):
                    densities[1][i] = densities[1][i] + 1
                elif (snapshot[k][j][i] == 1):
                    densities[0][i] = densities[0][i] + 1
        plt.plot(x, densities[0], label=f'Density A')
        plt.plot(x, densities[1], label=f'Density B')
        plt.xlabel("Position (x)")
        plt.ylabel("Population Density")
        plt.title(f"Population Densities of A and B at {k*1000}")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"Density{k*1000}moves.png")
        plt.close()
        # plt.show()
        # Plot snapshots of the grid at each time interval
        plt.figure() 
        im = plt.imshow(snapshot[k], cmap="bwr", vmin=-1, vmax=1)
        cbar = plt.colorbar(im)
        cbar.set_label("Species")
        
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.title(f"Grid Configuration at {k*1000}")
        plt.savefig(f"Grid{k*1000}.png")
        plt.close()
        # plt.show()
    return densities
            
            
def repeat100():
    averageDensities= []
    counter = 0
    for i in range(100):
        snapshots = setup()
        averageDensities.append(plotDensities(snapshots))
    print(len(averageDensities))
    print(len(averageDensities[0]))
    print(len(averageDensities[0][0]))
    print(counter)

    averageArray = np.zeros(2,60)
    for j in range(60):
        for i in range(100):
            averageArray[0][j] = averageDensities[i][0][j]
            averageArray[1][j] = averageDensities[i][1][j]
            
    #     averageArray[0][j] = averageArray[0][j] / 100
    #     averageArray[1][j] = averageArray[1][j] / 100
    # return averageArray

    averageDensities = np.array(averageDensities)
    averageArray = np.mean(averageDensities, axis=0)
    return averageArray

def averageDensityPlot(averageDensities):
    x = np.arange(60)
    plt.plot(x, averageDensities[0], label='Average Density A')
    plt.plot(x, averageDensities[1], label='Average Density B')
    plt.xlabel("Position (x)")
    plt.ylabel("Average Population Density")
    plt.title(f"Average Population Densities of A and B")
    plt.legend()
    plt.grid(True)
    plt.savefig("AvgDensityMoves.png")
    plt.show()

def main():
    choice = 4
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    snapshots = setup()
    if choice != 1:
        plotDensities(snapshots)
    if choice != 1 and choice != 2:
        averageDensityPlot(repeat100())

    
if __name__ == "__main__":
    main()

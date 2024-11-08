import numpy as np
import matplotlib.pyplot as plt
import sys

D = 2.0
L = 1000
dt = 0.05
dx = 1
numSteps = 1001

def densityDispersion():
    density = np.zeros(L)
    density[(L//2-5):(L//2+5)] = 1
    density /= np.sum(density)
    density2 = np.copy(density)
    snapshots = []
    for j in range(numSteps):
        for i in range(1, 999):
            density2[i] = density[i] + (D*dt/(dx**2)) * (density[i+1]-2 *density[i] + density[i-1])
        density2 /= np.sum(density2)
        density = density2
        if j % 200 == 0 :
            snapshots.append(density)
            
    print(len(snapshots))
    for index in range(len(snapshots)):
        x = np.linspace(-500, 500,1000)
        snapshot = snapshots[index]
        sigma = np.sqrt(2*D*index*dt*200)
        if index != 0:
            gaussianCurve = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-(x**2) / (2 * sigma**2))
            plt.plot(x, gaussianCurve, label = f"Gaussian Curve (Sigma = {sigma})")
        plt.plot(x, snapshot, label = f"t = {index*dt*200}")
        plt.xlabel('Position (x)')
        plt.ylabel('Density p(x)')
        plt.title(f'Density profile of 1D diffusion equation at time = {index*dt*200}')
        plt.grid(True)
        plt.legend()
        plt.savefig(f"Gaussian{index}.png")
        plt.show()

            
def main():
    choice = 3
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    if choice ==2 or choice == 3:
        densityDispersion()


if __name__ == "__main__":
    main()
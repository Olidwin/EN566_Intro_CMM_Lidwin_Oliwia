import numpy as np
import matplotlib.pyplot as plt
import sys

J = 1.5
k = 1.38 * 10**-23
temperatures = np.arange(0.1, 10.1, 0.1)



def originalLattice(n):
    return np.random.choice([1,-1], size=(n,n))
    
def energy(lattice):
    energy = 0
    n = len(lattice)
    for i in range(n):
        for j in range(n):
            nneighbors = lattice[i][(j - 1) % n] + lattice[i][(j + 1) % n] + lattice[(i - 1) % n][j] + lattice[(i + 1) % n][j]
            energy +=nneighbors*lattice[i][j]
    return energy/4 #The energy is divided by four because each square affects 4 nearest neighbors and is affected by it's four nearest neighbors

def magnitization(lattice):
    mag = 0
    n = len(lattice)
    for i in range(n):
        for j in range(n):
            mag += lattice[i][j]
    return mag

def step(lattice, temp):
    n = len(lattice)
    i = np.random.randint(0, n)
    j = np.random.randint(0, n)
    location = lattice[i][j]
    nneighbors = lattice[i][(j - 1) % n] + lattice[i][(j + 1) % n] + lattice[(i - 1) % n][j] + lattice[(i + 1) % n][j]
    d_E = 2*J*nneighbors*location
    if d_E <= 0 or np.random.uniform(0,1) <= np.exp((-d_E)/(k*temp)):
        lattice[i][j] *= -1
    return lattice, d_E  

def partOne():
    lattice = originalLattice(50)
    mag = np.zeros(len(temperatures))
    index = 0
    for temp in temperatures:
        for i in range(1000*len(lattice)** 2):
            lattice, e = step(lattice, temp)
        mag[index] = magnitization(lattice)
        index += 1
        print(f"temp: {temp}")
    plt.figure(figsize=(8, 6))
    plt.plot(temperatures, mag, marker='o', linestyle='-', color='b')
    plt.title("Magnetization vs Temperature")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Magnetization (M)")
    plt.grid()
    plt.show()
    plt.savefig("magtemp.png")
    
def partTwo():
    sizes = [5, 10, 20, 30]
    c_max = np.zeros(len(sizes))
    index_c_max = 0
    for size in sizes:
        lattice = originalLattice(size)
        index = 0
        c = np.zeros(len(temperatures))
        c_n = np.zeros(len(temperatures))
        index_c = 0
        for temp in temperatures:
            for i in range(100*size** 2):
                lattice,d_E = step(lattice, temp)
            print(f"size {size} temp ", temp)
            energies = np.zeros(101)
            energies[0] = energy(lattice)
            index = 1
            for i in range(100):
                lattice, d_E = step(lattice, temp)
                energies[index] = energies[index-1] + d_E
                index +=1
            average_E = 0
            average_E_2 = 0
            for j in range(len(energies)):
                average_E += energies[j]
                average_E_2 += energies[j]**2
            E = (average_E_2 - average_E)/(len(lattice)**2)
            c[index_c] = E/(k*(temp**2))
            c_n[index_c] = (E/(k*(temp**2)))/(len(lattice)**2)
            index_c +=1
        plt.figure(figsize=(8, 6))
        plt.plot(temperatures, c, label=f'Lattice size: {len(lattice)}x{len(lattice)}')
        plt.title(f"Specific Heat vs Temperature for n = {len(lattice)}")
        plt.xlabel("Temperature (T)")
        plt.ylabel("Specific Heat (C)")
        plt.grid()
        plt.savefig(f"ct{size}.png")
        c_max[index_c_max] = np.max(c_n)
        index_c_max += 1
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, c_max, marker='o', linestyle='-', color='b')
    plt.title("Specific Heat/N vs size")
    plt.xlabel("size (n)")
    plt.ylabel("Specific Heat/N (C)")
    plt.grid()
    plt.savefig("cmaxn.png")
    log_n = np.log(sizes)
    plt.plot(log_n, c_max, marker='o', linestyle='-', color='b')
    plt.title("Specific Heat/N vs log(size)")
    plt.xlabel("log(size) ")
    plt.ylabel("Specific Heat/N (C)")
    plt.grid()
    plt.savefig("cmaxln(n).png")

        

def main():
    partTwo()
    

if __name__ == "__main__":
    main()
    
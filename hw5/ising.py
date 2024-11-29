import numpy as np
import matplotlib.pyplot as plt
import sys

J = 1.5
temperatures = np.arange(0.1, 10.1, 0.1)

def originalLattice(n): #initializes a lattice of nxn size
    return np.random.choice([1,-1], size=(n,n))
    
def energy(lattice): #sum of the energy of a configuration
    energy = 0
    n = len(lattice)
    for i in range(n):
        for j in range(n):
            nneighbors = lattice[i][(j - 1) % n] + lattice[i][(j + 1) % n] + lattice[(i - 1) % n][j] + lattice[(i + 1) % n][j]
            energy += -nneighbors*lattice[i][j]
    return energy/4 #The energy is divided by four because each square affects 4 nearest neighbors and is affected by it's four nearest neighbors

def magnitization(lattice): #sum of the magnetization of a configuration
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
    if d_E <= 0 or np.random.uniform(0,1) <= np.exp((-d_E)/(temp)):
        lattice[i][j] *= -1
    else:
        d_E = 0
    return lattice, d_E  

def partOne():
    lattice = originalLattice(50) #lattice of size 50 x 50
    mag = np.zeros(len(temperatures)) #mag of same dimension as the amount of temperatures being sampled
    index = 0
    for temp in temperatures:
        for i in range(10000*len(lattice)** 2):
            lattice, e = step(lattice, temp)
        for j in range(10000):
            lattice, e = step(lattice, temp)
            mag[index] += magnitization(lattice)
        mag[index] = np.abs((mag[index]/(10000 * len(lattice)**2)))
        index += 1
        print(f"temp: {temp}")
    plt.figure(figsize=(8, 6))
    plt.plot(temperatures, mag, marker='o', linestyle='-', color='b')
    plt.title("Magnetization vs Temperature")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Magnetization (M)")
    plt.grid()
    plt.show()
    plt.savefig("magtemp_10000.png")
    
def partTwo():
    sizes = [100, 200, 500] #practice sizes
    log_n = np.log(sizes)
    print(log_n)
    c_max = np.zeros(len(sizes)) #array to store the maximum C/N values to compare with N and log(N)
    index_c_max = 0 #index for the maximum C/N value
    for size in sizes:
        lattice = originalLattice(size) #create a lattice
        index = 0 #used for the energy, initialize to 0 for every new size
        c = np.zeros(len(temperatures)) #new c values for each size
        c_n = np.zeros(len(temperatures)) #new C/N value for each size
        index_c = 0  #new c and C/N indexing
        for temp in temperatures:
            for i in range(10000*size** 2): #iterate till equilibrium basically
                lattice, d_E = step(lattice, temp)
            print(f"size {size} temp ", temp)
            energies = np.zeros(10001) #initialize an array of energies
            energies[0] = energy(lattice) #set the first energy to the current lattice
            index = 1 #then the index of energies would be 1
            for i in range(10000): #run 100 Monte-Carlos to get the change in energy from the previous microstate, and add the change to the previous microstate value.
                lattice, d_E = step(lattice, temp)
                energies[index] = energies[index-1] + d_E #calculate the energy of the new configuration
                index +=1
            average_E = np.mean(energies)
            average_E_2 = np.mean(energies**2)
            E = (average_E_2 - average_E**2)/((len(lattice)**2)) #calculate E for the specific heat equation
            c[index_c] = E/((temp**2)) #calculate the specific heat
            c_n[index_c] = c[index_c]/(len(lattice)**2) #specific heat divided by N
            index_c +=1
        plt.figure(figsize=(8, 6))
        plt.scatter(temperatures, c, label=f'Lattice size: {len(lattice)}x{len(lattice)}')
        plt.title(f"Specific Heat vs Temperature for n = {len(lattice)}")
        plt.xlabel("Temperature (T)")
        plt.ylabel("Specific Heat (C)")
        plt.grid()
        plt.savefig(f"ct{size}_100.png")
        plt.close()
        c_max[index_c_max] = np.max(c_n)
        index_c_max += 1
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, c_max, marker='o', linestyle='-', color='b')
    plt.title("Specific Heat/N vs size")
    plt.xlabel("size (n)")
    plt.ylabel("Specific Heat/N (C)")
    plt.grid()
    plt.savefig("cmaxn.png")
    plt.close()
    log_n = np.log(sizes)
    print(log_n)
    plt.plot(log_n, c_max, marker='o', linestyle='-', color='b')
    plt.title("Specific Heat/N vs log(size)")
    plt.xlabel("log(size) ")
    plt.ylabel("Specific Heat/N (C)")
    plt.grid()
    plt.savefig("cmaxln(n).png")
    plt.close()

def main():
    choice = 1
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    if choice == 1:
        partOne()
    if choice == 2:
        partTwo()
    
if __name__ == "__main__":
    main()
    
#Carbon 14_2 is used for carbon dating.
#It undergoes Beta- decay with a half-life of 5700 years.
#Originally 10**-12 kg of C14_2. 

import sys
import numpy as np
import matplotlib.pyplot as plt

particleNum = (4.3) * (10**13) #default number of particles
halfLife = 5700 #half-life of carbon (rate)


def euler(step_size, total_time): #Euler approximation method calculation values. Total time is considered to be 20000 years
    N = np.zeros(int(total_time/step_size)+1)
    N[0] = particleNum #originally start with the amount of 14C2
    
    for i in range(1,int(total_time/step_size)+1): #works similarly to a recursive method.
        N[i] = N[i-1] - 0.00012*N[i-1]*step_size #decrease each amount of particles by the rate multiplied by the amount multiplied by the change in time.
        #N(t) = N_o - lambda*N_o*t
    return N

def plot(width): #method was used to show figueres found in LaTex doc.
    x1 = np.arange(0,20001,10) #these define the time-steps
    x2 = np.arange(0,20001,100)
    x3 = np.arange(0,20001,1)
    y1 = euler(10, 20000) #these use approximations
    y2 = euler(100, 20000)
    y3 = particleNum*np.exp(-0.00012*x3) #this is the exact method.

    plt.plot(x1, y1, label='Numerical (10-year intervals)', color='blue')
    plt.plot(x2, y2, label='Numerical (100-year intervals)', color='green')
    plt.plot(x3, y3, label='Exact Solution (yearly)', color='purple')
    plt.title('Radioactive Decay of 14C2 over Time')
    plt.xlabel('Time (years)')
    plt.ylabel('Number of Particles Remaining')
    plt.legend()
    plt.grid()
    plt.xlim(0, 20000)
    plt.savefig("PlotDefault.png")
    plt.show()
    plt.close()
    
    #Plot of Figure 2 in Latex - same as Figure 1 but with a step width of 1000 for comparison
    x4 = np.arange(0,20001,width) #Width = 1000
    y4 = euler(width,20000)
    print("Euler 2nd half life (11400 years ~12000 years): ", y4[12])
    print("Exact 2nd half life (11400 years ~12000 years): ", y3[12000])

    plt.plot(x1, y1, label='Numerical (10-year intervals)', color='blue')
    plt.plot(x2, y2, label='Numerical (100-year intervals)', color='green')
    plt.plot(x3, y3, label='Exact Solution (yearly)', color='purple')
    plt.plot(x4, y4, label=f'Numerical ({width}-year intervals)', color='red')
    plt.title('Radioactive Decay of 14C2 over Time')
    plt.xlabel('Time (years)')
    plt.ylabel('Number of Particles Remaining')
    plt.legend()
    plt.grid()
    plt.xlim(0, 20000)
    plt.savefig("PlotExact101001000.png")
    plt.show()
    plt.close()

def plotByRequest(width): #Plotting only the requested graph
    x4 = np.arange(0,20001,width)
    y4 = euler(width,20000)
    #y1 = 0.00012*(particleNum*np.exp(-0.00012*x1))
    plt.plot(x4, y4, label=f'Numerical ({width}-year intervals)', color='red')
    plt.title('Radioactive Decay of 14C2 over Time')
    plt.xlabel('Time (years)')
    plt.ylabel('Number of Particles Remaining')
    plt.legend()
    plt.grid()
    plt.xlim(0, 20000)
    plt.savefig(f"PlotChosenWidth{width}.png")
    plt.show()
    plt.close()
    

def main():  
    if len(sys.argv) == 1: #gets you Figures 1 and 2 from the Latex Doc
        plot(1000) 
        
    elif len(sys.argv) == 2:
        width_arg = sys.argv[1]
        if width_arg.startswith('--plot='):
            width = int(width_arg[len('--plot='):])
            print(width)
            plotByRequest(width)
    else:
        print("Usage: python carbon.py --plot=<width>")
        sys.exit(1)
            


if __name__ == "__main__":
    main()
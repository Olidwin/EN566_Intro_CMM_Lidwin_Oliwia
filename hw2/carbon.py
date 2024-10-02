#Carbon 14_2 is used for carbon dating.
#It undergoes Beta- decay with a half-life of 5700 years.
#Originally 10**-12 kg of C14_2. 

import sys
import numpy as np
import matplotlib.pyplot as plt

particleNum = (4.3) * (10**13)
halfLife = 5700


def euler(step_size, total_time):
    N = np.zeros(int(total_time/step_size)+1)
    N[0] = particleNum
    
    for i in range(1,int(total_time/step_size)+1):
        N[i] = N[i-1] - 0.00012*N[i-1]*step_size
        
    return N

def plot():
    x1 = np.arange(0,20001,10)
    x2 = np.arange(0,20001,100)
    x3 = np.arange(0,20001,1)
    y1 = euler(10, 20000)
    y2 = euler(100, 20000)
    y3 = particleNum*np.exp(-0.00012*x3)

    plt.plot(x1, y1, label='Numerical (10-year intervals)', color='blue')
    plt.plot(x2, y2, label='Numerical (100-year intervals)', color='green')
    plt.plot(x3, y3, label='Exact Solution (yearly)', color='purple')
    plt.title('Radioactive Decay of 14C2 over Time')
    plt.xlabel('Time (years)')
    plt.ylabel('Number of Particles Remaining')
    plt.legend()
    plt.grid()
    plt.xlim(0, 20000)
    plt.savefig("PlotExact10100.png")
    plt.show()
    plt.close()

def plotByRequest(width):
    x1 = np.arange(0,20001,10)
    x2 = np.arange(0,20001,100)
    x3 = np.arange(0,20001,1)
    y1 = euler(10, 20000)
    y2 = euler(100, 20000)
    y3 = particleNum*np.exp(-0.00012*x3)
    plt.plot(x1, y1, label='Numerical (10-year intervals)', color='blue')
    plt.plot(x2, y2, label='Numerical (100-year intervals)', color='green')
    plt.plot(x3, y3, label='Exact Solution (yearly)', color='purple')
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
    if len(sys.argv) < 1:
        print("Usage: python carbon.py (Optional)WIDTH=<width>")
        sys.exit(1)
        
    width = 0   
    
    plot() 
    
    if len(sys.argv) == 2:
        width_arg = sys.argv[1]
        if width_arg.startswith('WIDTH='):
            width = int(width_arg[len('WIDTH='):])
            print(width)
            plotByRequest(width)
            print(width)


if __name__ == "__main__":
    main()
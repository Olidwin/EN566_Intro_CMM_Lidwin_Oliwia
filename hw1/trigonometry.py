import sys
import numpy as np
import matplotlib.pyplot as plt

def create_plot(function, FMT=None):
    x = np.arange(-10, 10, 0.05)
    for func in function: #iterates through the function array of strings
        if func == 'cos':
            y = np.cos(x)
            plt.plot(x, y, color='green', label='Cos(x)')
        elif func == 'sin':
            y = np.sin(x)
            plt.plot(x, y, color='blue', label='Sin(x)')
        elif func == 'sinc':
            y = np.sinc(x / np.pi)
            plt.plot(x, y, color='red', label='Sinc(x)')
    plt.legend()      
    plt.xlabel('Radians')
    plt.ylabel(f'Trigonometic function (radians)')
    if len(function) == 1:
        plt.title(f'Trigonometic Function: {", ".join(function)}')
    else:
        plt.title(f'Trigonometic Functions: {", ".join(function)}')
    if FMT:
        plt.savefig(f'plot_Function.{FMT}')
        print(f"Plot saved in the format of {FMT} to plot_Function.{FMT}")
    plt.show()
    
def write_to_file(write, FXN):
    x = np.arange(-10, 10, 0.05)
    with open(write, 'w') as file: #creates and open the file to be writeable.
        file.write("X(radians) "+ " ".join(FXN) + "\n") #creates the first line of the file to define the x and y axis.
        for i in range(len(x)):
            value = f"{x[i]}"
            for func in FXN:
                if func == 'cos':
                    value = value + f" {np.cos(x[i])}"
                elif func == 'sin':
                    value = value + f" {np.sin(x[i])}"
                elif func == 'sinc':
                    value = value + f" {np.sin(x[i]/np.pi)}"
            file.write(value + "\n")
    print(f"Done adding table to {write}")

def read_from_file(read, FMT="None"):
    try:
        with open(read, 'r') as file:
            file.readline()  # Skip the header line
            data = []
            for line in file:
                data.append(line.strip().split())

            if len(data) < 1 or len(data[0]) < 2:  # Ensure there's enough data
                print("Not enough data in file to create a plot")
                sys.exit(1)

            # Extract x-values from the first column
            x = [float(data[i][0]) for i in range(len(data))]  

            # Loop through each series of y-values
            for i in range(1, len(data[0])):  # Start from 1 to skip the x column
                y = [float(data[j][i]) for j in range(len(data))]  # Convert y values to float
                plt.plot(x, y, label=f"series {i}")

            plt.xlabel('X values')
            plt.ylabel('Y values')
            plt.title(f'Data plot of {read}')
            plt.legend()
            if FMT:
                plt.savefig(f"plot_from_file.{FMT}")
                print(f"Plot saved in the format of {FMT} to plot_from_file.{FMT}")
            plt.show()
                
    except FileNotFoundError:
        print("Invalid file input: The specified file does not exist.")

def main():
    
    if len(sys.argv) < 2:
        print("Not enough arguments")
        print("Usage: python3 trigonometry.py --function=<trig functions> [optional: --write=<filename>, --read=<filename>, --print=<format>]")
        sys.exit(1)
        
    
    FXN = []
    write = None
    read = None
    FMT = None

    for argument in sys.argv[1:]:
        if argument.startswith('--function='):
            FXN = argument[len('--function='):].split(',')
        elif argument.startswith('--write='):
            write = argument[len('--write='):]
        elif argument.startswith('--read_from_file'):
            read = argument[len('--read_from_file='):]
        elif argument.startswith('--print='):
            FMT = argument[len('--print='):]

    if len(FXN) == 0 and not read: #if running directly from the terminal as opposed to using the Makefile
        print("Usage: python3 trigonometry.py --function=<trig functions> [optional: --write=<filename>, --read=<filename>, --print=<format>]")
        sys.exit(1)

    if read:
        read_from_file(read, FMT)
    elif write:
        write_to_file(write, FXN)
    create_plot(FXN, FMT)
    
if __name__ == "__main__":
    main()
    

    
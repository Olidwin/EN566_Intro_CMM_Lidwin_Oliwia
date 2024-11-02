import sys
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8 # m/s^2
l = 9.8 # m
y = 0.25 # s^-1
a = 0.2 #rad/s^2
t = 0.05 #timestep

 
def plot(Et, Eo, Rt, Ro):
    x1 = np.arange(0,100.01,0.01)
    plt.plot(x1, Et, label='Euler theta', color='blue')
    plt.plot(x1, Rt, label='Runge theta', color='purple')
    plt.title('Theta Calculations using Euler and Runge')
    plt.xlabel('time (s)')
    plt.ylabel('Theta')
    plt.legend()
    plt.grid()
    plt.savefig("PlotTheta.png")
    plt.show()
    plt.close()
    plt.plot(x1, Eo, label='Euler omega', color='green')
    plt.plot(x1, Ro, label='Runge omega', color='aqua')
    plt.title('Omega Calculations using Euler and Runge')
    plt.xlabel('time (s)')
    plt.ylabel('Omega')
    plt.legend()
    plt.grid()
    plt.savefig("PlotOmega.png")
    plt.show()
    plt.close()
    
def plotPart4(R0t, R0o, R1t, R1o):
    x1 = np.arange(0,100.01,0.01)
    plt.plot(x1, R0t, label='Runge theta a = 0.2 rad/s^2', color='blue')
    plt.plot(x1, R1t, label='Runge theta a = 1.2 rad/s^2', color='purple')
    plt.title('Theta Calculations using Runge')
    plt.xlabel('time (s)')
    plt.ylabel('Theta')
    plt.legend()
    plt.grid()
    plt.savefig("PlotTheta2.png")
    plt.show()
    plt.close()
    plt.plot(x1, R0o, label='Runge omega a = 0.2 rad/s^2', color='green')
    plt.plot(x1, R1o, label='Runge omega a = 1.2 rad/s^2', color='aqua')
    plt.title('Omega Calculations Runge')
    plt.xlabel('time (s)')
    plt.ylabel('Omega')
    plt.legend()
    plt.grid()
    plt.savefig("PlotOmega2.png")
    plt.show()
    plt.close()
    
def plotEnergies(theta, omega):
    x1 = np.arange(0, 1000.01, 0.01)
    m = 1
    kinetic = np.zeros(len(theta))
    potential = np.zeros(len(theta))
    total = np.zeros(len(theta))

    for i in range(len(theta)):
        velocity = l * omega[i] 
        kinetic[i] = 0.5 * m * (velocity ** 2)
        height = l * (1 - np.cos(theta[i])) 
        potential[i] = m * g * height  
        
        # Total energy
        total[i] = kinetic[i] + potential[i]

    plt.plot(x1, kinetic, label='Kinetic Energy', color='green')
    plt.plot(x1, potential, label='Potential Energy', color='aqua')
    plt.plot(x1, total, label='Total Energy', color='blue')

    plt.title('Energy calculation based on position')
    plt.xlabel('time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.grid()
    plt.savefig("PlotEnergies.png")
    plt.show()
    plt.close()

    
def plotRungeTheta(Ro):
    omega = np.array([0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.85,0.9,1.0,1.5,2.0])
    phase_shift = np.array([9501, 831, 33, 9, 3, 6, 13, 15, 2081, 880, 1543,35,1000,668,9,2203])
    amp = np.array([0.20187, 0.24001, 0.24063, 0.24262, 0.25088, 0.26611, 0.29149, 0.32739, 0.37649, 0.44611, 0.52086, 0.54054, 0.52091,0.44627, 0.129,0.061])

    plt.figure(figsize=(8, 5))
    plt.scatter(omega, phase_shift, color='blue', label='Phase Shift Data')
    plt.plot(omega, phase_shift, linestyle='-', color='blue')

    plt.title('Phase Shift vs. Omega')
    plt.xlabel('Omega (ω)')
    plt.ylabel('Phase Shift (radians)')
    plt.legend()
    plt.grid()
    plt.savefig("PhaseShift_vs_Omega.png")
    plt.show()

    # Plot 2: Phase Shift vs Omega
    plt.plot(omega, amp, marker='s', linestyle='-', color='red')
    plt.title('Amplitude vs. Omega')
    plt.xlabel('Omega (ω)')
    plt.ylabel('Amplitude (m)')
    plt.legend()
    plt.grid()
    plt.savefig("Amplitude_vs_Omega.png")
    plt.show()
    
def Euler(step_size, total_time, frequency):
    time = 0 
    theta = np.zeros(int(total_time/step_size)+1)
    omega = np.zeros(int(total_time/step_size)+1)
    theta[0] = 0
    omega[0] = 1
    time = time
    for i in range(1,int(total_time/step_size)+1): 
        time = time + step_size
        omega[i] = omega[i-1] + ( -(1)* theta[i-1] - 2 * y * omega[i-1] + a*math.sin(frequency*time))*step_size
        theta[i] = theta[i-1] + omega[i] * step_size

    return theta, omega


def Runge(step_size, total_time, frequency):
    time = 0
    theta = np.zeros(int(total_time/step_size)+1)
    omega = np.zeros(int(total_time/step_size)+1)
    theta[0] = 0
    omega[0] = 1
    for i in range(1,int(total_time/step_size)+1):
        o1 = omega[i-1]
        t1 = theta[i-1]
        o2 = omega[i-1] + 0.5 * (-(1) * theta[i-1] - 2 * y * omega[i-1] + a * math.sin(frequency * time)) * step_size
        t2 = theta[i-1]+0.5*(o2)*step_size
        o3 = omega[i-1] + 0.5 * ((-(1) * (t2) - 2 * y * o2 + a * math.sin(frequency * (time+0.5*step_size))))*step_size
        t3 = theta[i-1]+0.5*(o3)*step_size
        o4 = omega[i-1] + 0.5 * ((-(1) * (t3) -2 * y * o3 + a * math.sin(frequency * (time+0.5*step_size))))*step_size
        t4 = theta[i-1]+0.5*(o4)*step_size
        
        omega[i] = omega[i-1] + (1/6) * ((2 * (o2-o1)) + 2 *(2 *(o3-o1)) + 2*(2*(o4-o1)) + (-(1)*t4*-2*y*o4+a*math.sin(frequency*(time+0.5*step_size)))*step_size)
        theta[i] = theta[i-1] + (1/6)*((2*(t2-t1)) + 2*(2*(t3-t1)) + 2*(2*(t4-t1)) + (o4)*step_size)

        time = time + step_size
    return theta, omega

def NonLinear02(step_size, total_time, frequency, alpha, theta1):
    time = 0
    theta = np.zeros(int(total_time/step_size)+1)
    omega = np.zeros(int(total_time/step_size)+1)
    theta[0] = theta1
    omega[0] = 1
    for i in range(1,int(total_time/step_size)+1): #works similarly to a recursive method.
        o1 = omega[i-1]
        t1 = theta[i-1]
        o2 = omega[i-1] + 0.5 * (-(1) * math.sin(theta[i-1]) - 2 * y * omega[i-1] + alpha * math.sin(frequency * time)) * step_size
        t2 = theta[i-1]+0.5*(o2)*step_size
        o3 = omega[i-1] + 0.5 * ((-(1) * math.sin((t2)) - 2 * y * o2 + alpha * math.sin(frequency * (time+0.5*step_size))))*step_size
        t3 = theta[i-1]+0.5*(o3)*step_size
        o4 = omega[i-1] + 0.5 * ((-(1) * math.sin((t3)) -2 * y * o3 + alpha * math.sin(frequency * (time+0.5*step_size))))*step_size
        t4 = theta[i-1]+0.5*(o4)*step_size
        
        omega[i] = omega[i-1] + (1/6) * ((2 * (o2-o1)) + 2 *(2 *(o3-o1)) + 2*(2*(o4-o1)) + (-(1)*math.sin(t4)*-2*y*o4+alpha*math.sin(frequency*(time+0.5*step_size)))*step_size)
        theta[i] = theta[i-1] + (1/6)*((2*(t2-t1)) + 2*(2*(t3-t1)) + 2*(2*(t4-t1)) + (o4)*step_size)

        time = time + step_size
    return theta, omega

def plotNonLinearForLyapunov(zero, one, two, three, four, num):
    curve1 = []
    curve1.append(np.abs(one-zero))
    curve2 = []
    curve2.append(np.abs(two-one))
    curve3 = []
    curve3.append(np.abs(three-two))
    curve4 = []
    curve4.append(np.abs(four-three))
    x1 = np.arange(0, 100.01, 0.01)
    
    findLyapunov(curve1)
    findLyapunov(curve2)
    findLyapunov(curve3)
    findLyapunov(curve4)


    plt.plot(x1, np.array(curve1).flatten(), label= f'theta from 0 to 0.001, Lyapunov = {findLyapunov(curve1)}')
    plt.plot(x1, np.array(curve2).flatten(), label= f'theta from 0.001 to 0.002, Lyapunov = {findLyapunov(curve2)}')
    plt.plot(x1, np.array(curve3).flatten(), label= f'theta from 0.002 to 0.003, Lyapunov = {findLyapunov(curve3)}')
    plt.plot(x1, np.array(curve4).flatten(), label= f'theta from 0.003 to 0.004, Lyapunov = {findLyapunov(curve4)}')
    plt.title('|Δθ(t)| for Various Initial Angles ')
    plt.xlabel('Time (s)')
    plt.ylabel('|Δθ(t)|')
    plt.legend()
    plt.grid()
    plt.savefig(f"Part_5_{num}.png")
    plt.show()
    
def findLyapunov(curve):
    log_curve = np.log(curve[curve > 0])
    time_valid = np.arange(len(log_curve)) * 0.01
    lyapunov_exponent, _ = np.polyfit(time_valid, log_curve, 1)
    return lyapunov_exponent
        
def main():
    choice = 6
    if (len(sys.argv) == 2): 
        part = sys.argv[1]
        if part.startswith('PART='):
            choice = int(part[len('PART='):])
    
    if choice == 2:
        Et, Eo = Euler(0.01, 100, 1.5)
        Rt, Ro = Runge(0.01, 100, 1.5)
        
        maxEt, maxRt, maxEo, maxRo = 0,0,0,0
        indexEo, indexRo, indexRt, indexEt = 0,0,0,0
        
        for i in range(6000,10001):

            if maxEo < Eo[i]:
                maxEo = Eo[i]
                indexEo = i
                
            if maxRt < Rt[i]:
                maxRt = Rt[i]
                indexRt = i

            if maxRo < Ro[i]:
                maxRo = Ro[i]
                indexRo = i
                
        print("Amp Runge-Kutta Theta: ", maxRt, " ", indexRt)
        print("PhaseShift Runge-Kutta Omega: ", (indexRo-indexEo))

        plot(Et, Eo, Rt, Ro)
        plotRungeTheta(Ro)
        
    if choice == 3:
        Rt1, Ro1 = Runge(0.01, 1000, 0.1)
        plotEnergies(Rt1, Ro1)
        
    if choice == 4:
        R0t,R0o = NonLinear02(0.01, 100, 0.1, 0.2, 0)
        R1t,R1o = NonLinear02(0.01, 100, 0.1, 1.2, 0)
        plotPart4(R0t,R0o,R1t,R1o)
    
    if choice == 5:
        R620t, R620o =  NonLinear02(0.01, 100, 0.666, 0.2, 0.000)
        R621t, R621o =  NonLinear02(0.01, 100, 0.666, 0.2, 0.001)
        R622t, R622o =  NonLinear02(0.01, 100, 0.666, 0.2, 0.002)
        R623t, R623o =  NonLinear02(0.01, 100, 0.666, 0.2, 0.003)
        R624t, R624o =  NonLinear02(0.01, 100, 0.666, 0.2, 0.004)
        
        plotNonLinearForLyapunov(R620t.flatten(),R621t.flatten(),R622t.flatten(),R623t.flatten(),R624t.flatten(), 0.2)

        R620t, R620o =  NonLinear02(0.01, 100, 0.666, 0.5, 0.000)
        R621t, R621o =  NonLinear02(0.01, 100, 0.666, 0.5, 0.001)
        R622t, R622o =  NonLinear02(0.01, 100, 0.666, 0.5, 0.002)
        R623t, R623o =  NonLinear02(0.01, 100, 0.666, 0.5, 0.003)
        R624t, R624o =  NonLinear02(0.01, 100, 0.666, 0.5, 0.004)
        
        plotNonLinearForLyapunov(R620t,R621t,R622t,R623t,R624t, 0.5)
        R620t, R620o =  NonLinear02(0.01, 100, 0.666, 1.2, 0.000)
        R621t, R621o =  NonLinear02(0.01, 100, 0.666, 1.2, 0.001)
        R622t, R622o =  NonLinear02(0.01, 100, 0.666, 1.2, 0.002)
        R623t, R623o =  NonLinear02(0.01, 100, 0.666, 1.2, 0.003)
        R624t, R624o =  NonLinear02(0.01, 100, 0.666, 1.2, 0.004)
        
        plotNonLinearForLyapunov(R620t,R621t,R622t,R623t,R624t, 1.2)
if __name__ == "__main__":
    main()
#This code will have four trajectories
#Angles: 45, 30, 15, 9
#Initial Velocity 70 m/s
#Drag F_drag = -CpA(v^2); C is coefficient, p is 1.29 kg/m^3, A = 0.0014 m^2, v is velocity (magnitude)
#F = ma;
#g = 9.8 m/s^2
#mass = 46 grams  = 0.046 kg
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

v = 70 #initial velocity
g = 9.8 #gravity
m = 0.046 #mass
p = 1.29 #air density
A = 0.0014 #golf ball surface area
time = 0.05 #time_steps

def idealTraj(angle): #only influence of gravity
    v_x = v*math.cos(angle) #split initial velocity into x and y components
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]] #starts at (0,0)
    velocities = [[v_x], [v_y]] #starts with initial velocity components
    index = 0 #this will be used to iterate through the list (could have alternatively used for each loop with a break when condition not met)
    print(coordinates[1][index]) #make sure the plot starts at y = 0.
    while coordinates[1][index] > 0 or coordinates[1][index] == 0: #while the y coordinate >=0
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time #x = x_o + v_x(t)
        coordinates[0].append(new_x)
        velocities[0].append(velocities[0][index]) # v_x = v_ox

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time #y = y_o + v_y(t)
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time #v_y = v_oy - gt
        velocities[1].append(velocity_y)

        index += 1 #go to next coordinate
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates #coordinates array is all the x, y positions
                
#Drag F_drag = -CpA(v^2); C is coefficient, p is 1.29 kg/m^3, A = 0.0014 m^2, v is velocity (magnitude)

def dragTraj(angle):
    C = 0.5
    v_x = v*math.cos(angle) #Split v into it's components
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]] #initially at (0,0)
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0: #while y >= 0
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time #x = x_o + v_x(t)
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time
        velocities[0].append(velocity_x) # v_x = v_ox - tCpA(v^2)/m

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time #y = y_oy + v_y(t)
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time
        velocities[1].append(velocity_y) #v_y = v_oy - gt - tCpA(v^2)/m
        index += 1
        
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates #coordinates array is all the x, y positions
        
def dimpledDragTraj(angle):
    v_x = v*math.cos(angle) #Split v into it's components
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]] #initially at (0,0)
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0: #while y >= 0
        if ((velocities[0][index]**2 + velocities[1][index]**2)**0.5) <= 14: #Change C of drag accoring to velocity
            C = 0.5
        else:
            C = 7.0/((velocities[0][index]**2 + velocities[1][index]**2)**0.5)
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time #x = x_o + v_x(t)
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time
        velocities[0].append(velocity_x) # v_x = v_ox - tCpA(v^2)/m

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time #y = y_oy + v_y(t)
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time
        velocities[1].append(velocity_y) #v_y = v_oy - gt - tCpA(v^2)/m
        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates #coordinates array is all the x, y positions
        
        
def spunDimpledDraggedTraj(angle):
    Sowm = 0.25
    v_x = v*math.cos(angle) #Split v into it's components
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]]#initially at (0,0)
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0: #while y >= 0
        if ((velocities[0][index]**2 + velocities[1][index]**2)**0.5) <= 14: #Change C of drag accoring to velocity
            C = 0.5
        else:
            C = 7.0/((velocities[0][index]**2 + velocities[1][index]**2)**0.5) 
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time #x = x_o + v_x(t)
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time - Sowm*velocities[1][index] * time
        velocities[0].append(velocity_x) # v_x = v_ox - tCpA(v^2)/m - Sowm *v_oy*t

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time #y = y_oy + v_y(t)
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time + Sowm*velocities[0][index] * time
        velocities[1].append(velocity_y) #v_y = v_oy - gt - tCpA(v^2)/m - Sown *v_ox*t
        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates  #coordinates array is all the x, y positions
    
def plotAllFourTraj(angle): #plot outputs from the methods above.
    angle_rad = math.radians(angle)
    ideal = idealTraj(angle_rad)
    drag = dragTraj(angle_rad)
    dimpledDrag = dimpledDragTraj(angle_rad)
    spunDimpledDrag = spunDimpledDraggedTraj(angle_rad)

    plt.plot(ideal[0], ideal[1], label='Ideal Trajectory', color='blue')
    plt.plot(drag[0], drag[1], label='Smooth Ball with Drag', color='green')
    plt.plot(dimpledDrag[0], dimpledDrag[1], label='Dimpled Ball with Drag', color='purple')
    plt.plot(spunDimpledDrag[0], spunDimpledDrag[1], label='Dimpled Ball with Drag and Spin', color='black')
    plt.title(f'Projectile Motion at Angle {angle}')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.grid()
    plt.legend()
    plt.savefig(f"ProjectileAngle{angle}.png") #save the figure 
    plt.show()


def main():
    if (len(sys.argv) == 1): #if no optional parameter input, display default 4 plots used for LaTex file
        plotAllFourTraj(45)
        plotAllFourTraj(30)
        plotAllFourTraj(15)
        plotAllFourTraj(9)

    elif (len(sys.argv) == 2): #if angle is provided, create it's plot.
        theta_arg = sys.argv[1]
        if theta_arg.startswith('--plot='):
            theta = int(theta_arg[len('--plot='):])
            print(theta)
            plotAllFourTraj(theta)
            
    else:
        print("Usage: python golf.py --plot=<theta>") #if wrong amount of parameters exit the code
        sys.exit(1)





if __name__ == "__main__":
    main()
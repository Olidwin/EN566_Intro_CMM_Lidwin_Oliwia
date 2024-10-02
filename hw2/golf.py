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

o1 = 45
o2 = 30
o3 = 15
o4 = 9
v = 70
g = 9.8
m = 0.046
p = 1.29
A = 0.0014
time = 0.05 #time_steps


def idealTraj(angle):
    v_x = v*math.cos(angle)
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]]
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0:
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time
        coordinates[0].append(new_x)
        velocities[0].append(velocities[0][index])

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time
        velocities[1].append(velocity_y)

        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates
                
#Drag F_drag = -CpA(v^2); C is coefficient, p is 1.29 kg/m^3, A = 0.0014 m^2, v is velocity (magnitude)

def dragTraj(angle):
    C = 0.5
    v_x = v*math.cos(angle)
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]]
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0:
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time
        velocities[0].append(velocity_x)

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time
        velocities[1].append(velocity_y)
        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates
        
def dimpledDragTraj(angle):
    v_x = v*math.cos(angle)
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]]
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0:
        if ((velocities[0][index]**2 + velocities[1][index]**2)**0.5) <= 14:
            C = 0.5
        else:
            C = 7.0/((velocities[0][index]**2 + velocities[1][index]**2)**0.5)
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time
        velocities[0].append(velocity_x)

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time
        velocities[1].append(velocity_y)
        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates
        
        
def spunDimpledDraggedTraj(angle):
    Sowm = 0.25
    v_x = v*math.cos(angle)
    v_y = v*math.sin(angle)
    coordinates = [[0], [0]]
    velocities = [[v_x], [v_y]]
    index = 0
    print(coordinates[1][index])
    while coordinates[1][index] > 0 or coordinates[1][index] == 0:
        if ((velocities[0][index]**2 + velocities[1][index]**2)**0.5) <= 14:
            C = 0.5
        else:
            C = 7.0/((velocities[0][index]**2 + velocities[1][index]**2)**0.5)
        # Changing X-coordinate
        new_x = coordinates[0][index] + velocities[0][index] * time
        coordinates[0].append(new_x)
        velocity_x = velocities[0][index] - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[0][index]) * time - Sowm*velocities[1][index] * time
        velocities[0].append(velocity_x)

        # Changing Y-coordinate
        new_y = coordinates[1][index] + velocities[1][index] * time
        coordinates[1].append(new_y)
        velocity_y = velocities[1][index] - g * time - (1/m)* (C*p*A) * (velocities[0][index]**2 + velocities[1][index]**2)**0.5 * (velocities[1][index]) * time + Sowm*velocities[0][index] * time
        velocities[1].append(velocity_y)
        index += 1
    print(f"Initial coordinates: x={coordinates[0][0]}, y={coordinates[1][0]}")
    return coordinates
    
def plotAllFourTraj(angle):
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
    plt.show()




def main():
    if len(sys.argv) < 1:
        print("Usage: python golf.py (Optional)THETA=<theta>")
        sys.exit(1)
        
    theta = 45 #set this as the default, then check if the argument exists and change it if it 
    
    if len(sys.argv) == 2:
        theta_arg = sys.argv[1]
        if theta_arg.startswith('THETA='):
            theta = int(theta_arg[len('THETA='):])
            print(theta)
            
    plotAllFourTraj(theta)




if __name__ == "__main__":
    main()
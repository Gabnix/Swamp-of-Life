
import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from swamp import Duck, Newt, Shrimp, Alga, Rock

if (len(sys.argv) < 7):
    print("argv too short, usage: python3 swampLife.py <Duck> <Newt> <Shrimp> <Algae> <Rock> <Timestep>")
    print('Using default values for <Duck=5> <Newt=5> <Shrimp=5> <Algae=5> <Rock=5> <Timestep=15> <Movement="von Neumann">')
    # Default values
    userDuck = 20
    userNewt = 20
    userShrimp = 20
    userAlga = 30
    userRock = 5
    userTime = 15
    moveType = "V"
else:
    # User definable values
    moveType = str(sys.argv[1].upper())
    userDuck = int(sys.argv[2])
    userNewt = int(sys.argv[3])
    userShrimp = int(sys.argv[4])
    userAlga = int(sys.argv[5])
    userRock = int(sys.argv[6])
    userTime = int(sys.argv[7])


def create_animal(number_of_animals, container, blueprint, bounding_value, num_of_terrain):
    for i in range(number_of_animals):
        randX = random.randint(0, XMAX-1)
        randY = random.randint(0, YMAX-1)
        
        if num_of_terrain == 1:
            while terrain[randY][randX] != bounding_value[0]:
                randX = random.randint(0, XMAX-1)
                randY = random.randint(0, YMAX-1)
        elif num_of_terrain == 2:
            while terrain[randY][randX] != bounding_value[0] and terrain[randY][randX] != bounding_value[1]:
                randX = random.randint(0, XMAX-1)
                randY = random.randint(0, YMAX-1)
        elif num_of_terrain == 4:
            while terrain[randY][randX] != bounding_value[0] and terrain[randY][randX] != bounding_value[1] and terrain[randY][randX] != bounding_value[2] and terrain[randY][randX] != bounding_value[3]:
                randX = random.randint(0, XMAX-1)
                randY = random.randint(0, YMAX-1)
        container.append(blueprint([randX, randY]))
        print(container[i])


def plot(container, col, bounding_value, num_of_terrain):
    xvalues = []
    yvalues = []
    sizes = []

    for c in container:
        if not c.is_dead():  # check if duck is not dead
            c.stepChange(terrain, (XMAX, YMAX), bounding_value, num_of_terrain, moveType)
        xvalues.append(c.pos[0])
        yvalues.append(c.pos[1])
        sizes.append(c.getSize())
    plt.scatter(xvalues, yvalues, s=sizes, color=col) 
    plt.xlim(0, XMAX)
    plt.ylim(0, YMAX)


def print_statement(container):
    for c in list(container):  # make a copy of the list
        if c.dead:
            container.remove(c)
        print(c)


def plotTerrain(filename):
    grid = np.loadtxt(filename, dtype=int, delimiter=",")
    grid = np.array(grid[::-1])
    plt.imshow(grid, cmap=plt.cm.terrain)
    return grid


def reprodution(container, blueprint, bounding_value, num_of_terrain):
    for i in range(len(container)):
        for j in range(i+1, len(container)):
            c = container[i] 
            c2 = container[j]
            if c.inRange_Repro(c2.getPos()):
                if c.getState() != c.states[0] and c.getState() != c.states[1]:
                    if c2.getState() != c2.states[0] and c2.getState() != c2.states[1]:
                        chance = random.randint(0, 100)
                        coordinate = c.getPos_Average(c2.getPos())
                        coordinate = list(coordinate)
                        if chance >= 50:
                            randX = random.randint(0, XMAX-1)
                            randY = random.randint(0, YMAX-1)

                            if num_of_terrain == 1:
                                while terrain[randY][randX] != bounding_value[0]:
                                    randX = random.randint(0, XMAX-1)
                                    randY = random.randint(0, YMAX-1)
                            elif num_of_terrain == 2:
                                while terrain[randY][randX] != bounding_value[0] and terrain[randY][randX] != bounding_value[1]:
                                    randX = random.randint(0, XMAX-1)
                                    randY = random.randint(0, YMAX-1)
                            elif num_of_terrain == 4:
                                while terrain[randY][randX] != bounding_value[0] and terrain[randY][randX] != bounding_value[1] and terrain[randY][randX] != bounding_value[2] and terrain[randY][randX] != bounding_value[3]:
                                    randX = random.randint(0, XMAX-1)
                                    randY = random.randint(0, YMAX-1)

                            # while terrain[randY][randX] != bounding_value:
                            #     randY = random.randint(0, YMAX-1)
                            #     randX = random.randint(0, XMAX-1)
                            ani = blueprint([randX, randY])
                            container.append(ani)
                            print(f'---> {c.getState()} met {c2.getState()}, lay an egg @ {str(coordinate)}')
                        else:
                            print(f'---> {c.getState()} met {c2.getState()}, had a fight @ {str(coordinate)}')


def hunting(containerA, containerZ):
    for contA in containerA:
        for contZ in containerZ:
            if contA.inRange(contZ.getPos()):
                if contA.getState() != contA.states[0]:
                    coordinate = contA.getPos_Average(contZ.getPos())
                    coordinate = list(coordinate)
                    if contZ.getState() != contZ.states[0] and contZ.getState() != contZ.states[3][1]:
                        containerZ.remove(contZ)
                        print(f"---> {contZ.getState()} was eaten by {contA.getState()} @ {str(coordinate)}")
                    elif contZ.getState() == contZ.states[3][1]:
                        chance = random.randint(0, 100)
                        if chance > 40:
                            print(f"---> {contA.getState()} poisoned by {contZ.getState()}, but survived! @ {list(contA.getPos())}")
                        else:
                            contA.dead = True
                            contZ.dead = True
                            print(f"---> {contA.getState()} eaten {contZ.getState()}, and died! @ {list(contA.getPos())}")


# Boundary limits = (XMAX, YMAX)
XMAX = 100
YMAX = 75
terrain = plotTerrain("terrain.csv")


def main():
    ducks = []
    newts = []
    shrimps = []
    algae = []
    rocks = []
    bounding_value = [15, 75, 25, 25]

    create_animal(userDuck, ducks, Duck, bounding_value, 4)
    create_animal(userNewt, newts, Newt, bounding_value, 2)
    create_animal(userShrimp, shrimps, Shrimp, bounding_value, 1)
    create_animal(userAlga, algae, Alga, bounding_value, 1)
    create_animal(userRock, rocks, Rock, bounding_value, 4)

    for i in range(userTime):
        print("\n==== TIMESTEP ", i+1, "====")

        print_statement(ducks)
        print_statement(newts)
        print_statement(shrimps)
        print_statement(algae)
        print_statement(rocks)

        print()
        reprodution(ducks, Duck, bounding_value, 4)
        reprodution(newts, Newt, bounding_value, 2)
        reprodution(shrimps, Shrimp, bounding_value, 1)
        # reprodution(algae, Alga, bounding_value, 1)
        print()

        hunting(ducks, newts)
        hunting(ducks, shrimps)
        hunting(ducks, algae)
        hunting(newts, shrimps)

        plot(ducks, "orange", bounding_value, 4)
        plot(newts, "black", bounding_value, 2)
        plot(shrimps, "red", bounding_value, 1)
        plot(algae, "green", bounding_value, 1)
        plot(rocks, "brown", bounding_value, 1)

        plotTerrain("terrain.csv")  # plotting the terrain
        plt.suptitle(f"Swamp of life: Timestep {i+1}/{userTime}", fontsize=10, fontweight='bold')
        title = f"Duck: {len(ducks)}   Newt: {len(newts)}   Shrimp: {len(shrimps)}   Alga: {len(algae)}   Rocks: {len(rocks)}"
        plt.title(title, fontsize=10)
        plt.savefig(f"Swap of life_Timestep[{i+1} of {userTime}].png", dpi=300)
        plt.pause(0.2)
        plt.clf()

    print(f"\nNumber of timesteps: {userTime}")
    if moveType == "M":
        print("Movement type      : Moore ")
    elif moveType == "V":
        print("Movement type      : von Neumann ")
    else:
        print(f"Movement type      : {moveType}")
        print(f"\n*** Invalid movement type {moveType} entered") 
        print('*** Next time, use "M" for Moore / "V" for von Neumann')
        print("*** Using default movement: von Neumann")

        
    print(f"Initial count      : {userDuck} Ducks, {userNewt} Newts, {userShrimp} Shrimps, {userAlga} Algae, {userRock} Rocks")
    print(f"Final count        : {len(ducks)} Ducks, {len(newts)} Newts, {len(shrimps)} Shrimps, {len(algae)} Algae, {len(rocks)} Rocks")



if __name__ == "__main__":
    t1 = time.perf_counter()
    print("\nProgram starts...\n")
    main()
    print("\nProgram terminated.")
    t2 = time.perf_counter()
    time_used = t2-t1
    print(f"\n[Finished in {time_used:.1f}s]\n")

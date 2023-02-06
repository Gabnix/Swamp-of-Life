#
# swampLife.py - Basic simulation of swamp life for assignment, S2 2022. 
#
# Revisions: 
#
# 01/09/2022 – Base version for assignment
#

# Cite: This python file is build on using COMP1005 Assignment sample file "swamp.py", Semester 2, 2022, provided on the blackboard
# Cite: COMP 1005. 2022. “test3.py” & “characters.py” Practical Test 3, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: COMP 1005. 2022. “Senior Tutoring Sessions”, COMP1005 Fundamentals of Programming, Semester 2, 2022.


import sys 
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from swamp import * #Duck, Newt, Shrimp, Rock, Terrain
#from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#import os

'''sys.stdout = open(os.path.join(__file__), "w")
print ("test sys.stdout")'''


######################################################
# Command line argument

# Cite: COMP 1005. 2022. “dosagebase.py” Practical 8, COMP1005 Fundamentals of Programming, Semester 2, 2022.

print(sys.argv) # print out the program's name

# Process command line arguments
if (len(sys.argv) < 7):
    print("argv too short, usage: python3 swampLife.py <Number of Ducks> <Number of Newts> <Number of Shrimps> <Number of Algae> <Number of Rocks> <Number of Timesteps>")
    print('Using default values for <Number of Ducks: 5> <Number of Newts: 5> <Number of Shrimps: 5> <Number of Algae: 5> <Number of Rocks: 5> <Number of Timesteps: 15> <Movement Type: von Neumann>')
    # Default values
    userDuck = 5
    userNewt = 5
    userShrimp = 5
    userAlga = 5
    userRock = 5
    userTime = 5
    moveType = "V"
else:
    # User definable values
    moveType = str(sys.argv[1].upper()) # user-definable movement type (M - Moore / V - von Neumann)
    userDuck = int(sys.argv[2]) # user-definable duck's numbers
    userNewt = int(sys.argv[3]) # user-definable newt's numbers
    userShrimp = int(sys.argv[4]) # user-definable shrimp's numbers
    userAlga = int(sys.argv[5]) # user-definable alga's numbers
    userRock = int(sys.argv[6]) # user-definable rock's numbers
    userTime = int(sys.argv[7]) # user-definable timeteps
    
    
    '''userDuck = int(input("Please enter numbers of duck: ")) # number of ducks user created
    userNewt = int(input("Please enter numbers of newt: ")) # number of newts user created
    userShrimp = int(input("Please enter numbers of shrimp: ")) # number of shrimps user created
    userAlga = int(input("Please enter numbers of Alga: ")) # number of algae user created
    userRock = int(input("Please enter numbers of Rock: ")) # number of rocks user created
    userTime = int(input("Please enter numbers of timestep: ")) # number of timesteps user created'''

    print("\nNumber of timesteps: " + str(userTime))
    if  moveType == "M" or moveType == "MOORE":
        print("Movement type      : Moore ")
    elif  moveType != "V" or moveType != "VON NEUMANN":
        print("Movement type      : von Neumann ")
    print("Initial count      : " + str(userDuck) + " Ducks, " + str(userNewt) + " Newts, " + str(userShrimp) + " Shrimps, " + str(userAlga) + " Algae, " + str(userRock) + " Rocks")

    #print("Movement type (M)oore / (V)on Neumann: " + str(moveType))

######################################################
# Boundary limits = (XMAX, YMAX)

XMAX = 100
YMAX = 75

######################################################
# Plot's Functions

# Cite: COMP 1005. 2022. “test3.py” & “characters.py” Practical Test 3, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: Matplotlib 3.6.0 documentation. (n.d.) “matplotlib.markers”
# URL: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

def plotDuck(dList):
    # plot for ducks
    xvalues = []
    yvalues = []
    sizes = []
    for d in dList:
        #d.stepChange((XMAX, YMAX))
        xvalues.append(d.pos[0])
        yvalues.append(d.pos[1])
        sizes.append(d.getSize())
        # Annotate
        #for i in range(len(xvalues)):
            #plt.annotate("D", (xvalues[i], yvalues[i]))
    plt.scatter(xvalues, yvalues, s=sizes, marker="P", color="yellow")   # Note plt origin is bottom left 
    plt.xlim(0,XMAX)
    plt.ylim(0,YMAX)

def plotNewt(nList):
    # plot for newts
    xvalues = []
    yvalues = []
    sizes = []
    for n in nList:
        #d.stepChange((XMAX, YMAX))
        xvalues.append(n.pos[0])
        yvalues.append(n.pos[1])
        sizes.append(n.getSize())
        # Annotate
        #for i in range(len(xvalues)):
            #plt.annotate("D", (xvalues[i], yvalues[i]))
    plt.scatter(xvalues, yvalues, s=sizes, marker="2", color="black")   # Note plt origin is bottom left 
    plt.xlim(0,XMAX)
    plt.ylim(0,YMAX)

def plotShrimp(sList):
    # plot for shrimps
    xvalues = []
    yvalues = []
    sizes = []
    for s in sList:
        #d.stepChange((XMAX, YMAX))
        xvalues.append(s.pos[0])
        yvalues.append(s.pos[1])
        sizes.append(s.getSize())
        # Annotate
        #for i in range(len(xvalues)):
            #plt.annotate("D", (xvalues[i], yvalues[i]))
    plt.scatter(xvalues, yvalues, s=sizes, marker="d", color="lightcoral")   # Note plt origin is bottom left 
    plt.xlim(0,XMAX)
    plt.ylim(0,YMAX)

def plotAlga(aList):
    # plot for algae
    xvalues = []
    yvalues = []
    sizes = []
    for a in aList:
        #d.stepChange((XMAX, YMAX))
        xvalues.append(a.pos[0])
        yvalues.append(a.pos[1])
        sizes.append(a.getSize())
        # Annotate
        #for i in range(len(xvalues)):
            #plt.annotate("D", (xvalues[i], yvalues[i]))
    plt.scatter(xvalues, yvalues, s=sizes, marker="X", color="green")   # Note plt origin is bottom left 
    plt.xlim(0,XMAX)
    plt.ylim(0,YMAX)

def plotRock(rList):
    # plot for rocks
    xvalues = []
    yvalues = []
    sizes = []
    for r in rList:
        #d.stepChange((XMAX, YMAX))
        xvalues.append(r.pos[0])
        yvalues.append(r.pos[1])
        sizes.append(r.getSize())
        # Annotate
        #for i in range(len(xvalues)):
            #plt.annotate("D", (xvalues[i], yvalues[i]))
    plt.scatter(xvalues, yvalues, s=sizes, marker="p", color="brown")   # Note plt origin is bottom left 
    plt.xlim(0,XMAX)
    plt.ylim(0,YMAX)

######################################################
# Plot terrain

# Cite: COMP 1005. 2022. “colourmap” Lecture 4 slides, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: COMP 1005. 2022. “heatsource.py” Practical 5 worksheet, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: Senior Tutoring Sessions

def plotTerrain(filename):
    grid = np.loadtxt(filename, dtype = int, delimiter = ',')
    grid = np.array(grid[::-1])
    plt.imshow(grid, cmap=plt.cm.terrain)
    return grid

terrain = plotTerrain("terrain.csv") # plotting the terrain

# Colour codes:
# 15 = Water (Blue)
# 25 = Grassland (Light green)
# 35 = Bush (Dark green)
# 75 = Mud (Brown)

########################################################
# Creating ducks, newts, shrimps, algae, rocks variables 

def main():
    ducks = [] # variable for ducks
    newts = [] # variable for newts
    shrimps = [] # variable for shrimps
    algae = [] # variable for shrimps
    rocks = [] # variable for rocks

    '''userDuck = int(input("Please enter numbers of duck: ")) # number of ducks user created
    userNewt = int(input("Please enter numbers of newt: ")) # number of newts user created
    userShrimp = int(input("Please enter numbers of shrimp: ")) # number of shrimps user created
    userAlga = int(input("Please enter numbers of Alga: ")) # number of algae user created
    userRock = int(input("Please enter numbers of Rock: ")) # number of rocks user created
    userTime = int(input("Please enter numbers of timestep: ")) # number of timesteps user created'''

    '''######################################################
    # Movement type's prompt (moore / von Neumann)
    
    print("Please choose moore / von Neumann movement ( M / V ): ") # user-definable movement types
    moveType = str(input().upper())
    while moveType != "M" and moveType != "MOORE" and moveType != "V" and moveType != "VON NEUMANN":
        print("Error! Re-enter 'M' or 'V' only (M - moore / V - von Neumann): ")
        moveType = str(input().upper())
    print(moveType, type(moveType))'''
    
    ######################################################
    # Generating animals objects

    for i in range(userDuck): # create duck in a loop (user defined numbers)
        randX = random.randint(0,XMAX-1) # generating X_position
        randY = random.randint(0,YMAX-1) # generating Y_position
        '''while terrain[randY][randX] != 15 and terrain[randY][randX] != 75:
            randY = random.randint(0,YMAX-1) # generating X_position
            randX = random.randint(0,XMAX-1) # generating Y_position'''
        duck = Duck([randX, randY]) # define the position of duck by passing the (X, Y) values into class Duck
        ducks.append(duck) # append each "duck" into the "ducks" variable
        print(ducks[i]) # in a loop, print out each individual duck from "ducks" variable
     
    for i in range(userNewt): # create newt in a loop (user defined numbers)
        randX = random.randint(0,XMAX-1) # generating X_position
        randY = random.randint(0,YMAX-1) # generating Y_position
        while terrain[randY][randX] != 15 and terrain[randY][randX] != 75 and terrain[randY][randX] != 25: # Loop for generating (X,Y) coordinate until conditions are met (in "water" and "mud")
            randY = random.randint(0,YMAX-1) # generating X_position
            randX = random.randint(0,XMAX-1) # generating Y_position
        newt = Newt([randX, randY]) # define the position of newt by passing the (X, Y) values into class Newt
        newts.append(newt) # append each "newt" into the "newts" variable
        print(newts[i]) # in a loop, print out each individual newt from "newts" variable
        
    for i in range(userShrimp): # create shrimp in a loop (user defined numbers)
        randX = random.randint(0,XMAX-1) # generating X_position
        randY = random.randint(0,YMAX-1) # generating Y_position
        while terrain[randY][randX] != 15:
            randY = random.randint(0,YMAX-1) # generating X_position
            randX = random.randint(0,XMAX-1) # generating Y_position
        shrimp = Shrimp([randX, randY]) # define the position of shrimp by passing the (X, Y) values into class shrimp
        shrimps.append(shrimp) # append each "shrimp" into the "shrimps" variable
        print(shrimps[i]) # in a loop, print out each individual shrimp from "shrimps" variable

    for i in range(userAlga): # create alga in a loop (user defined numbers)
        randX = random.randint(0,XMAX-1) # generating X_position
        randY = random.randint(0,YMAX-1) # generating Y_position
        while terrain[randY][randX] != 15:
            randY = random.randint(0,YMAX-1) # generating X_position
            randX = random.randint(0,XMAX-1) # generating Y_position
        alga = Alga([randX, randY]) # define the position of alga by passing the (X, Y) values into class alga
        algae.append(alga) # append each "alga" into the "algae" variable
        print(algae[i]) # in a loop, print out each individual alga from "algae" variable

    for i in range(userRock): # create rock in a loop (user defined numbers)
        randX = random.randint(0,XMAX-1) # generating X_position
        randY = random.randint(0,YMAX-1) # generating Y_position
        rock = Rock([randX, randY]) # define the position of rock by passing the (X, Y) values into class rock
        rocks.append(rock) # append each "rock" into the "rocks" variable
        print(rocks[i]) # in a loop, print out each individual rock from "rocks" variable


##################################################################
# Timesteps: Logs of animals' states & positions in each timesteps 

    for k in range(userTime): 
        print("\n ### TIMESTEP ",k, "###")
        
        #################################### duck timesteps ####################################
        for d in ducks:
            '''for d2 in ducks:
                if d2.getState() == d2.states[3]:
                    ducks.remove(d2) # Remove if dead'''
                
            '''if d.getState() == "Dead Duck":
                for d in ducks:
                    ducks.remove(d) # Remove if dead'''
                           
            # ducks eat newts      
            for n in newts: # for every newt
                if duck.inRange(n.getPos()): # if duck is inRange of newt
                    if d.getState() != d.states[0] and d.getState() != d.states[3]: # state of duck is not "Duck Egg" and "Dead Duck"
                        if n.getState() != n.states[2]: # state of newt is not "Dead Newt"
                            coordinate = d.getPos_Average(n.getPos()) # get the avarage coordinate between duck and newt
                            newts.remove(n) # remove newt from the list
                            print("### An " + n.getState() + " was eaten by an " + d.getState() + " @ " + str(coordinate))
                        elif n.getState() == n.states[2]: # state of newt is "Poisonous Newt"
                            chance = random.randint(0,100) # possibilities of survival
                            if chance > 40 :
                                print("### An " + d.getState() + " poisoned by a " + n.getState() +  " @ " + str(d.getPos()) + ", but survived !!!")
                            else:
                                newts.remove(n)
                                for d in ducks:
                                    ducks.remove(d) # Remove duck if dead
                                print("### An " + d.getState() + " poisoned by a " + n.getState() +  " @ " + str(d.getPos()) + ", and died !!!")
            
            # duck eat shrimps   
            for s in shrimps: # for every shrimp
                if duck.inRange(s.getPos()): # if duck is inRange of shrimp
                    if d.getState() != d.states[0] and d.getState() != d.states[3]: # state of duck is not "Duck Egg" and "Dead Duck"
                        if s.getState() != s.states[3]: # state of newt is not "Dead Newt"
                            coordinate = d.getPos_Average(s.getPos())
                            shrimps.remove(s)
                            print("### A " + s.getState() + " was eaten by a " + d.getState() + " @ " + str(coordinate))
            
            d.stepChange(terrain, (XMAX,YMAX), moveType) 
            print(d, d.getTerrain(terrain)) # print out duck's state, pos, and terrain

        # ducks reproduction
        # Cite: Senior tutor
        for i in range(len(ducks)): # for in the range of number of ducks
            for j in range(i+1, len(ducks)): # for in the range from, start: 2nd duck(i+1), stop: number of ducks
                d = ducks[i] 
                d2 = ducks[j]
                if d.inRange_Repro(d2.getPos()): # for every duck1, check if duck2 is in range
                    if d.getState() != d.states[0] and d.getState() != d.states[3]: # if duck1 is not "Duck Egg" and "Dead Duck"
                        if d2.getState() != d2.states[0] and d2.getState() != d2.states[3]: # if duck2 is not "Duck Egg" and "Dead Duck"
                            chance = random.randint(0,100) # the possibility of reproduction
                            if chance >= 50 :
                                coordinate = d.getPos_Average(d2.getPos())
                                randX = random.randint(0,XMAX-1) # generating X_position for new duck ("Duck Egg")
                                randY = random.randint(0,YMAX-1) # generating Y_position for new duck ("Duck Egg")
                                '''while terrain[randY][randX] != 15 and terrain[randY][randX] != 75:
                                    randY = random.randint(0,YMAX-1) # generating X_position
                                    randX = random.randint(0,XMAX-1) # generating Y_position'''
                                duck = Duck([randX, randY]) # define the position of new duck by passing the (X, Y) values into class Duck
                                ducks.append(duck) # append each new "duck" into the "ducks" variable (list)
                                print("### A " + d.getState() + " met a " + d2.getState() + " @ " + str(coordinate) + ", lay an egg")
                            else:
                                print("### A " + d.getState() + " met a " + d2.getState() + ", no egg!!!")
        
        #################################### newt timesteps ####################################
        for n in newts:
            '''n.stepChange(terrain, (XMAX,YMAX))
            for n2 in newts:
                if n2.getState() == n2.states[4]:
                    newts.remove(n2) # Remove if dead
            print(n)'''

            # newts eat shrimps
            for s in shrimps:
                if newt.inRange(s.getPos()):
                    if n.getState() != n.states[0] and n.getState() != n.states[4]:
                        if s.getState() != s.states[0]:
                            shrimps.remove(s)
                            print("### A " + s.getState() + " was eaten by a " + n.getState() + " @ " + str(s.getPos()))
            
            n.stepChange(terrain, (XMAX,YMAX), moveType)
            print(n, n.getTerrain(terrain))

        # newt reproduction
        for i in range(len(newts)):
            for j in range(i+1, len(newts)):
                n = newts[i]
                n2 = newts[j]
                if n.inRange_Repro(n2.getPos()):
                    if n.getState() != n.states[0] and n.getState() != n.states[4]:
                        if n2.getState() != n2.states[0] and n2.getState() != n.states[4]:
                            chance = random.randint(0,100) 
                            if chance >= 50 : # possibilities of producing offspring
                                coordinate = n.getPos_Average(n2.getPos()) 
                                randX = random.randint(0,XMAX-1) # generating X_position
                                randY = random.randint(0,YMAX-1) # generating Y_position
                                while terrain[randY][randX] != 15 and terrain[randY][randX] != 75  and terrain[randY][randX] != 25:
                                    randY = random.randint(0,YMAX-1) # generating X_position
                                    randX = random.randint(0,XMAX-1) # generating Y_position'''
                                newt = Newt([randX, randY]) # define the position of newt by passing the (X, Y) value into class Newt
                                newts.append(newt) # append each "newt" into the "newts" variable
                                print("### A " + n.getState() + " met a " + n2.getState() + ", lay an egg" + " @ " + str(coordinate))
                                #print(newts)
                            else:
                                print("### A " + n.getState() + " met a " + n2.getState() + ", no egg !!!")
                        
        #################################### shrimp timesteps ####################################
        for s in shrimps:
            #s.stepChange(terrain, (XMAX,YMAX))
            '''for s2 in shrimps:
                if s2.getState() == s2.states[3]:
                    shrimps.remove(s2) # Remove if dead
            print(s)'''

            # shrimps eat algae
            for a in algae:
                if shrimp.inRange(a.getPos()):
                    if s.getState() != s.states[0] and s.getState() != s.states[3]:
                        if a.getState() == a.states[0]:
                            algae.remove(a)
                            print("### An " + a.getState() + " eaten by a " + s.getState() + " @ " + str(s.getPos()))
                        if a.getState() == a.states[1]:
                            chance = random.randint(0,100) # possibilities of survival
                            if chance > 50 :
                                print("### An " + s.getState() + " poisoned by a " + a.getState() +  " @ " + str(s.getPos()) + ", but survived !!!")
                            else:
                                algae.remove(a)
                                for s in shrimps:
                                    shrimps.remove(s) # Remove if dead
                                print("### An " + s.getState() + " poisoned by a " + a.getState() +  " @ " + str(s.getPos()) + ", and died !!!")

            s.stepChange(terrain, (XMAX,YMAX), moveType)
            print(s, s.getTerrain(terrain))

        # shrimps reproduction
        for i in range(len(shrimps)):
            for j in range(i+1, len(shrimps)):
                s = shrimps[i]
                s2 = shrimps[j]
                if s.inRange_Repro(s2.getPos()):
                    if s.getState() != s.states[0] and s.getState() != s.states[3]:
                        if s2.getState() != s2.states[0] and s2.getState() != s2.states[3]:
                            chance = random.randint(0,100) # possibilities of producing offspring
                            if chance > 30 :
                                coordinate = s.getPos_Average(s2.getPos())
                                randX = random.randint(0,XMAX-1) # generating X_position
                                randY = random.randint(0,YMAX-1) # generating Y_position
                                while terrain[randY][randX] != 15:
                                    randY = random.randint(0,YMAX-1) # generating X_position
                                    randX = random.randint(0,XMAX-1) # generating Y_position
                                shrimp = Shrimp([randX, randY]) # define the position of shrimp by passing the (X, Y) value into class Shrimp
                                shrimps.append(shrimp) # append each "shrimp" into the "shrimps" variable
                                print("### A " + s.getState() + " met a " + s2.getState() + ", lay an egg" + " @ " + str(coordinate))
                                #print(shrimps)
                            else:
                                print("### A " + s.getState() + " met a " + s2.getState() + ", no egg !!!")
            
        #################################### alga timesteps ####################################
        for a in algae:
            #a.stepChange(terrain, (XMAX,YMAX))
            '''if a.getState() == a.states[2]: 
                algae.remove(a) # Remove if dead'''
            
            # algae reproduction
            if a.getState() != a.states[2]: 
                chance = random.randint(0,100) # possibilities of producing offspring (can alter for lower or highr chance)
                if chance >= 95 :
                    randX = random.randint(0,XMAX-1) # generating X_position
                    randY = random.randint(0,YMAX-1) # generating Y_position
                    while terrain[randY][randX] != 15:
                        randY = random.randint(0,YMAX-1) # generating X_position
                        randX = random.randint(0,XMAX-1) # generating Y_position'''
                    alga = Alga([randX, randY]) # define the position of new creature by passing the (X, Y) value into class Alga
                    algae.append(alga) # append each new "alga" into the "algae" variable (list)
                    print("### An " + a.getState() + " self-reproduced !!!") # + " @ " + str(a.getPos()) + ", " + str(chance) + "%" + " chance")

            a.stepChange(terrain, (XMAX,YMAX), moveType)
            print(a, a.getTerrain(terrain))
            
        
        #################################### rock timesteps ####################################
        for r in rocks:
            '''r.stepChange(terrain, (XMAX,YMAX))
            print(r)'''

            # ducks hit the rocks
            for d in ducks:
                if rock.inRange(d.getPos()):
                    if d.getState() != d.states[0] and d.getState() != d.states[3]:
                        chance = random.randint(0,100) 
                        if chance <= 90 : # possibilities of survival (can alter for lower or highr chance)
                            ducks.remove(d)
                            print("### A " + d.getState() + " hit a " + r.getState() + " @ " + str(r.getPos()) + ", and died !!!")
                        else:
                            print("### A " + d.getState() + " hit a " + r.getState() + " @ " + str(r.getPos()) + ", and survived !!!")

            r.stepChange(terrain, (XMAX,YMAX))
            print(r, r.getTerrain(terrain))

    ######################################################
    # Plots of animals' positions on screen/ Visualisation
        
        # Calling plot fuctions at the top, plot the scatter plots
        plotDuck(ducks)
        plotNewt(newts)
        plotShrimp(shrimps)
        plotAlga(algae)
        plotRock(rocks)
        terr = plotTerrain("terrain.csv") # plotting the terrain
        
        ######################################################
        # Change background colour
        
        # Cite: Matplotlib change background color.(2021).Retrived from https://pythonguides.com/matplotlib-change-background-color/

        plt.rcdefaults() # Reset the plot configurations to default
        plt.rcParams.update({'axes.facecolor':'lightblue'}) # Set the axes color globally for all plots
        
        ######################################################
        # Titles of the plot (in each timesteps)

        Title ="#Timesteps "+ str(k) + " " + " Ducks: " + str(len(ducks)) + " Newts: " + str(len(newts)) + " Shrimps: " + str(len(shrimps)) + " Algae: " + str(len(algae)) + " Rocks: " + str(len(rocks))
        plt.title(Title)

        ######################################################
        # Save the plots into local directory

        #plt.savefig("Swamp of Life_Timestep" + str([k]) + ".png")
        #plt.pause(0.5)
        #plt.clf()

    #################################################################################################
    # Final counts shown at the end of program: Number of timesteps, Initial counts, and Final counts

    print("\nNumber of timesteps: " + str(userTime))
    if  moveType == "M" or moveType == "MOORE":
        print("Movement type      : Moore ")
    elif  moveType != "V" or moveType != "VON NEUMANN":
        print("Movement type      : von Neumann ")
    #print("Movement type (M - moore / V - von Neumann): ", moveType)
    print("Initial count      : " + str(userDuck) + " Ducks, " + str(userNewt) + " Newts, " + str(userShrimp) + " Shrimps, " + str(userAlga) + " Algae, " + str(userRock) + " Rocks")
    print("Final count        : " + str(len(ducks)) + " Ducks, " + str(len(newts)) + " Newts, " + str(len(shrimps)) + " Shrimps, " + str(len(algae)) + " Algae, " + str(len(rocks)) + " Rocks")
    
if __name__ == "__main__":
    print("\n===== Swamp of Life =====\n")
    main()

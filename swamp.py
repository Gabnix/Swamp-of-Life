#
# swamp.py - Class definitions for simulation of swamp life
#
# Revisions: 
#
# 01/09/2022 – Base version for assignment
#

# Cite: This python file is build on using COMP1005 Assignment sample file "swamp.py", Semester 2, 2022, provided on the blackboard
# Cite: COMP 1005. 2022. “test3.py” & “characters.py” Practical Test 3, COMP1005 Fundamentals of Programming, Semester 2, 2022.
# Cite: COMP 1005. 2022. “Senior Tutoring Sessions”, COMP1005 Fundamentals of Programming, Semester 2, 2022.

import random
import pandas as pd

# Duck
class Duck():
    time2hatch = 3
    states = ["Duck Egg", "Adult Duck", "Old Duck", "Dead Duck"]
    #eat = ["eaten"]

    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)

    '''# Cite: senior tutor
    def __eq__(self, other):
        equals = False

        if isinstance(other, Newt):
            if self.pos == other.pos:
                if self.state == other.state:
                    if self.age == other.age:
                        equals = True
        return equals'''

    '''def stepChange(self, grid, limits, userMov):
        #print(self.pos[1], type(grid))
        #print(type(grid[self.pos[1]]))
        self.age += 1
        if self.state == self.states[0]: # for when it's "duck egg"
            if self.age == self.time2hatch: # when the age reach/equal the "time2hatch", the state change to "Adult Duck"
                self.state = self.states[1]
        if self.state != self.states[0]: # for when it's not "Duck Egg", then it could be "Adult Duck", "Old Duck" or "Dead Duck"
            if self.age > 8 and self.age < 12: # when the age is between 9 to 11, self.state turns into "Old Duck"
                self.state = self.states[2]
                
                # Moore
                if userMov == "M":
                    xmov = random.randint(-2,2) # Movement of the "Old Duck" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                            self.pos[1] += ymov
                            self.pos[0] += xmov

                # von Neumann
                if userMov == "V":
                    xmov = random.randint(-2,2) # Movement of the "Old Duck" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                            chance = random.randint(0,100)
                            if chance < 51:
                                self.pos[1] += ymov
                            else:    
                                self.pos[0] += xmov'''

    def stepChange(self, grid, limits, userMov):
        #print(self.pos[1], type(grid))
        #print(type(grid[self.pos[1]]))
        self.age += 1
        if self.state == self.states[0]: # for when it's "duck egg"
            if self.age == self.time2hatch: # when the age reach/equal the "time2hatch", the state change to "Adult Duck"
                self.state = self.states[1]
        elif self.state != self.states[0]: # for when it's not "Duck Egg", then it could be "Adult Duck", "Old Duck" or "Dead Duck"
            if self.age > 8 and self.age < 12: # when the age is between 9 to 11, self.state turns into "Old Duck"
                self.state = self.states[2]
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Duck" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                            self.pos[1] += ymov
                            self.pos[0] += xmov

                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Duck" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                            chance = random.randint(0,100)
                            if chance < 51:
                                self.pos[1] += ymov
                            else:    
                                self.pos[0] += xmov

            elif self.age >= 12: # when the age is 12 or greater, self.state turns into "Dead Duck" - no movement
                self.state = self.states[3]
                # von Neumann
                xmov = 0 # Zero movement for "Dead Duck"
                ymov = 0
                '''if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                        chance = random.randint(0,100)
                        if chance < 51:
                            self.pos[1] += ymov
                        else:
                            self.pos[0] += xmov'''

            else: # for when it's "Adult Duck"
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-5,5) # Movement of the "Adult Duck" defined here - faster
                    ymov = random.randint(-5,5)
                    #print(self.pos[1], type(grid))
                    #print(type(grid[self.pos[1]]))
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                            self.pos[1] += ymov
                            self.pos[0] += xmov
                
                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-5,5) # Movement of the "Adult Duck" defined here - slower
                    ymov = random.randint(-5,5)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                            chance = random.randint(0,100)
                            if chance < 51:
                                self.pos[1] += ymov
                            else:    
                                self.pos[0] += xmov

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 10 and abs(self.pos[1] - pos[1]) < 10 # check if a duck is near another animals

    def inRange_Repro(self, pos):
        return abs(self.pos[0] - pos[0]) < 10 and abs(self.pos[1] - pos[1]) < 10 # check if a duck is near another duck, for reproduction

    def getSize(self): # return "duck" size on the scatter plot
        if self.state == self.states[0]:
            size = 15
        else:
            size = 30
        return size

    def getPos(self): # return the position of duck (x,y)
        return (self.pos[0], self.pos[1])
    
    def getPos_Average(self, pos): # return the avarage positioni coordinate (X,Y) where duck meet with another animal
        abs((self.pos[0] + pos[0]) / 2) and abs((self.pos[1] + pos[1]) / 2)
        return pos


    def getState(self): # return the state of duck
        return self.state

    def getTerrain(self, grid): # return the terrain type
        if grid[self.pos[1]][self.pos[0]] == 15:
            location = "Water"
            return location
        if grid[self.pos[1]][self.pos[0]] == 75:
            location = "Mud"
            return location
        if grid[self.pos[1]][self.pos[0]] == 35:
            location = "Bush"
            return location
        if grid[self.pos[1]][self.pos[0]] == 25:
            location = "Grassland"
            return location


# Newt
class Newt():

    time2hatch = 2
    states = ["Newt Egg", "Adult Newt", "Poisonous Newt", "Old Newt", "Dead Newt"]

    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0

    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    # Cite: senior tutor
    '''def __eq__(self, other):
        equals = False

        if isinstance(other, Newt):
            if self.pos == other.pos:
                if self.state == other.state:
                    if self.age == other.age:
                        equals = True
        return equals'''

    def stepChange(self, grid, limits, userMov):
        self.age += 1
        if self.state == self.states[0]:
            if self.age == self.time2hatch:
                chance = random.randint(0,100)
                if chance <= 80:
                    self.state = self.states[1]
                else:
                    self.state = self.states[2]
        elif self.state != self.states[0]: # for when it's not "Newt Egg", then it could be "Adult Newt", "Old Newt" or "Dead Newt"
            if self.age > 9 and self.age < 13: # when the age is between 10 to 12, self.state turns into "Old Newt"
                self.state = self.states[3] # "Old Newt"
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Newt" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 25:
                                self.pos[1] += ymov
                                self.pos[0] += xmov

                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Newt" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 25:
                                chance = random.randint(0,100)
                                if chance < 51:
                                    self.pos[1] += ymov
                                else:    
                                    self.pos[0] += xmov

            elif self.age >= 13: # when the age is 13, self.state turns into "Dead Newt" - no movement
                self.state = self.states[4]
                # von Neumann
                xmov = 0 # Movement of the "Adult Newt"
                ymov = 0
                '''if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                        chance = random.randint(0,100)
                        if chance < 51:
                            self.pos[1] += ymov
                        else:
                            self.pos[0] += xmov'''

            else: # for when it's "Adult Newt" or "Poisonius Newt"
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-5,5) # Movement - faster
                    ymov = random.randint(-5,5)
                    #print(self.pos[1], type(grid))
                    #print(type(grid[self.pos[1]]))
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 25:
                                self.pos[1] += ymov
                                self.pos[0] += xmov
                
                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-5,5) # Movement - faster
                    ymov = random.randint(-5,5)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 25:
                                chance = random.randint(0,100)
                                if chance < 51:
                                    self.pos[1] += ymov
                                else:    
                                    self.pos[0] += xmov

        '''if self.state != self.states[0]: # for when it's not "Newt Egg", then it could be "Adult Newt", "Old Newt" or "Dead Newt"
            if self.age > 9 and self.age < 13 : # when the age is between 10 to 12, self.state turns into "Old Newt"
                self.state = self.states[3]
                xmov = random.randint(0,1) # Movement of the "Old Newt" defined here - slower
                ymov = random.randint(0,1)
                if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 35 and grid[self.pos[1] + ymov][self.pos[0] + xmov] != 25:
                            self.pos[1] += ymov
                            self.pos[0] += xmov
            elif self.age == 13: # when the age is 13, self.state turns into "Dead Newt"
                self.state = self.states[4]
                xmov = 0 # "Dead Newt" has zero X and Y movement
                ymov = 0
            else: # for when it's "Adult Newt"
                xmov = random.randint(-2,2)
                ymov = random.randint(-2,2)
                if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        if grid[self.pos[1] + ymov][self.pos[0] + xmov] != 35 and grid[self.pos[1] + ymov][self.pos[0] + xmov] != 25:
                            self.pos[1] += ymov
                            self.pos[0] += xmov'''

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 15 and abs(self.pos[1] - pos[1]) < 15

    def inRange_Repro(self, pos):
        return abs(self.pos[0] - pos[0]) < 5 and abs(self.pos[1] - pos[1]) < 5

    def getSize(self):
        if self.state == self.states[0]:
            size = 10
        else:
            size = 15
        return size
    
    def getPos(self):
        return (self.pos[0], self.pos[1])

    def getPos_Repro(self,pos):
        return (self.pos[0], self.pos[1])

    def getPos_Average(self, pos):
        abs((self.pos[0] + pos[0]) / 2) and abs((self.pos[1] + pos[1]) / 2)
        return pos

    def getState(self):
        return self.state

    def getTerrain(self, grid):
        if grid[self.pos[1]][self.pos[0]] == 15:
            location = "Water"
            return location
        if grid[self.pos[1]][self.pos[0]] == 75:
            location = "Mud"
            return location
        if grid[self.pos[1]][self.pos[0]] == 35:
            location = "Bush"
            return location
        if grid[self.pos[1]][self.pos[0]] == 25:
            location = "Grassland"
            return location

"""
n = Newt((3, 5))
n2 = Newt((5, 3))
print(n == n2)
"""

# Shrimp
class Shrimp():
    time2hatch = 2
    states = ["Shrimp Egg", "Adult Shrimp", "Old Shrimp", "Dead Shrimp"]
    
    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)

    # Cite: senior tutor
    def __eq__(self, other):
        equals = False

        '''if isinstance(other, Newt):
            if self.pos == other.pos:
                if self.state == other.state:
                    if self.age == other.age:
                        equals = True
        return equals'''
    
    def stepChange(self, grid, limits, userMov):
        self.age += 1
        if self.state == self.states[0]:
            if self.age == self.time2hatch:
                self.state = self.states[1]
        elif self.state != self.states[0]: # for when it's not "Shrimp Egg", then it could be "Adult Shrimp", "Old Shrimp" or "Dead Shrimp"
            if self.age > 4 and self.age < 6: # when the age is 5, self.state turns into "Old Shrimp"
                self.state = self.states[2]
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Shrimp" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                                self.pos[1] += ymov
                                self.pos[0] += xmov

                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-2,2) # Movement of the "Old Shrimp" defined here - slower
                    ymov = random.randint(-2,2)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                                chance = random.randint(0,100)
                                if chance < 51:
                                    self.pos[1] += ymov
                                else:    
                                    self.pos[0] += xmov

            elif self.age >= 6: # when the age is 6 or older, self.state turns into "Dead Shrimp" - no movement
                self.state = self.states[3]
                xmov = 0 
                ymov = 0
                '''if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        #if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15 or grid[self.pos[1] + ymov][self.pos[0] + xmov] == 75:
                        chance = random.randint(0,100)
                        if chance < 51:
                            self.pos[1] += ymov
                        else:
                            self.pos[0] += xmov'''

            else: # for when it's "Adult Shrimp"
                
                # Moore
                if userMov == "M" or userMov == "MOORE":
                    xmov = random.randint(-5,5) # Movement of the "Adult Shrimp" defined here - faster
                    ymov = random.randint(-5,5)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                                self.pos[1] += ymov
                                self.pos[0] += xmov
                
                # von Neumann (and anything else other than moore)
                elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                    xmov = random.randint(-5,5) # Movement of the "Adult Shrimp" defined here - faster
                    ymov = random.randint(-5,5)
                    if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                        if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                            if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                                chance = random.randint(0,100)
                                if chance < 51:
                                    self.pos[1] += ymov
                                else:    
                                    self.pos[0] += xmov

        '''if self.age > 4 and self.age < 6: # when the age is 5, self.state turns into "Old Shrimp"
            self.state = self.states[2]
            xmov = random.randint(-1,1) # Movement of the "Old Shrimp" defined here - slower
            ymov = random.randint(-1,1)
            if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                    if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                        self.pos[1] += ymov
                        self.pos[0] += xmov
        elif self.age == 6: # when the age is greater equal to 6, self.state turns into "Dead Shrimp"
            self.state = self.states[3]
            xmov = 0 # "Dead Shrimp" has zero X and Y movement
            ymov = 0
        else: # for when it's an "Adult Shrimp"
            xmov = random.randint(-2,2) # Movement of the "Adult Shrimp" defined here - faster
            ymov = random.randint(-2,2)
            if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                    if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                        self.pos[1] += ymov
                        self.pos[0] += xmov'''

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 10 and abs(self.pos[1] - pos[1]) < 10

    def inRange_Repro(self, pos):
        return abs(self.pos[0] - pos[0]) < 7 and abs(self.pos[1] - pos[1]) < 7
            
    def getSize(self):
        if self.state == "Shrimp Egg":
            size = 3
        else:
            size = 8
        return size

    def getPos(self):
        return (self.pos[0], self.pos[1])

    def getPos_Average(self, pos):
        abs((self.pos[0] + pos[0]) / 2) and abs((self.pos[1] + pos[1]) / 2)
        return pos

    def getState(self):
        return self.state

    def getTerrain(self, grid):
        if grid[self.pos[1]][self.pos[0]] == 15:
            location = "Water"
            return location
        if grid[self.pos[1]][self.pos[0]] == 75:
            location = "Mud"
            return location
        if grid[self.pos[1]][self.pos[0]] == 35:
            location = "Bush"
            return location
        if grid[self.pos[1]][self.pos[0]] == 25:
            location = "Grassland"
            return location

# Alga
class Alga():
    states = ["Alga", "Poisonous Alga", "Dead Alga"]
    #lifespan = 5
    
    def __init__(self, pos):
        self.pos = pos
        det = random.randint(0,100) # when an Alga spawn, it will have 2 possibilities
        if det > 80:
            self.state = self.states[1] # "Poisonous Alga"
        else:
            self.state = self.states[0] # regular "Alga"
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
        
    # Cite: senior tutor
    '''def __eq__(self, other):
        equals = False

        if isinstance(other, Newt):
            if self.pos == other.pos:
                if self.state == other.state:
                    if self.age == other.age:
                        equals = True
        return equals'''

    def stepChange(self, grid, limits, userMov):
        self.age += 1
        if self.age == 10: # when the age is 10, self.state turns into "Dead Alga"
            self.state = "Dead Alga"
            xmov = 0 # "Dead Alga" has zero X and Y movement
            ymov = 0
        else: # movements for when it's "Alga" or "Poisonous Alga"
            
            # Moore
            if userMov == "M" or userMov == "MOORE":
                xmov = random.randint(-1,1) # Movement of the "Alga" and "Poisonous Alga" defined here
                ymov = random.randint(-1,1)
                if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                            self.pos[1] += ymov
                            self.pos[0] += xmov
            
            # von Neumann (and anything else other than moore)
            elif userMov == "V" or userMov == "VON NEUMANN" or  userMov != "M" or userMov != "MOORE":
                xmov = random.randint(-1,1) # Movement of the "Alga" and "Poisonous Alga" defined here
                ymov = random.randint(-1,1)
                if (self.pos[0] + xmov) < limits[0] and (self.pos[1] + ymov) < limits[1]:
                    if (self.pos[0] + xmov) > 0 and (self.pos[1] + ymov) > 0:
                        if grid[self.pos[1] + ymov][self.pos[0] + xmov] == 15:
                            chance = random.randint(0,100)
                            if chance < 51:
                                self.pos[1] += ymov
                            else:    
                                self.pos[0] += xmov

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 5 and abs(self.pos[1] - pos[1]) < 5

    def getSize(self):
        return 5

    def getPos(self):
        return (self.pos[0], self.pos[1])

    def getState(self):
        return self.state

    def getTerrain(self, grid):
        if grid[self.pos[1]][self.pos[0]] == 15:
            location = "Water"
            return location
        if grid[self.pos[1]][self.pos[0]] == 75:
            location = "Mud"
            return location
        if grid[self.pos[1]][self.pos[0]] == 35:
            location = "Bush"
            return location
        if grid[self.pos[1]][self.pos[0]] == 25:
            location = "Grassland"
            return location

# Rock
class Rock():
    states = ["Stationary Rock"]
    
    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)

    # Cite: senior tutor
    '''def __eq__(self, other):
        equals = False

        if isinstance(other, Newt):
            if self.pos == other.pos:
                if self.state == other.state:
                    if self.age == other.age:
                        equals = True
        return equals'''
    
    def stepChange(self, grid, limits):
        ...

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 40 and abs(self.pos[1] - pos[1]) < 40

    def getSize(self):
        return 100

    def getPos(self):
        return (self.pos[0], self.pos[1])

    def getState(self):
        return self.state
    
    def getPos_Average(self, pos):
        abs((self.pos[0] + pos[0]) / 2) and abs((self.pos[1] + pos[1]) / 2)
        return pos

    def getTerrain(self, grid):
        if grid[self.pos[1]][self.pos[0]] == 15:
            location = "Water"
            return location
        if grid[self.pos[1]][self.pos[0]] == 75:
            location = "Mud"
            return location
        if grid[self.pos[1]][self.pos[0]] == 35:
            location = "Bush"
            return location
        if grid[self.pos[1]][self.pos[0]] == 25:
            location = "Grassland"
            return location

'''if __name__ == '__main__':
    print('test')
    T = Terrain()
    T.loadTerrain("D:\\FOP\\Assignment\\terrain2.csv")'''

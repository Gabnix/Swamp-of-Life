import random


def movement(posX, posY, limit, grid, bounding_value, num_of_terrain, moveType):
    xmov = random.randint(-1, 1)
    ymov = random.randint(-1, 1)
    if (posX + xmov) < limit[0] and (posY + ymov) < limit[1]:
        if (posX + xmov) > 0 and (posY + ymov) > 0:

            if num_of_terrain == 1:
                if grid[posY + ymov][posX + xmov] == bounding_value[0]:
                    chance = random.randint(0, 100)
                    if moveType == "M":
                        posY += ymov
                        posX += xmov
                    else:
                        if chance < 51:
                            posY += ymov
                        else:
                            posX += xmov
            elif num_of_terrain == 2:
                if grid[posY + ymov][posX + xmov] == bounding_value[0] or grid[posY + ymov][posX + xmov] == bounding_value[1]:
                    chance = random.randint(0, 100)
                    if moveType == "M":
                        posY += ymov
                        posX += xmov
                    else:
                        if chance < 51:
                            posY += ymov
                        else:
                            posX += xmov
            elif num_of_terrain == 4:
                if grid[posY + ymov][posX + xmov] == bounding_value[0] or grid[posY + ymov][posX + xmov] == bounding_value[1] or grid[posY + ymov][posX + xmov] == bounding_value[2] or grid[posY + ymov][posX + xmov] == bounding_value[3]:
                    chance = random.randint(0, 100)
                    if moveType == "M":
                        posY += ymov
                        posX += xmov
                    else:
                        if chance < 51:
                            posY += ymov
                        else:
                            posX += xmov
    return (posX, posY)


class Animal:

    states = ["Animal"]

    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        self.dead = False

    def inRange(self, pos):
        return abs(self.pos[0] - pos[0]) < 5 and abs(self.pos[1] - pos[1]) < 5

    def inRange_Repro(self, pos):
        return abs(self.pos[0] - pos[0]) < 5 and abs(self.pos[1] - pos[1]) < 5

    def getPos(self):
        return (self.pos[0], self.pos[1])

    def getPos_Repro(self, pos):
        return (self.pos[0], self.pos[1])

    def getPos_Average(self, pos):
        abs((self.pos[0] + pos[0]) / 2) and abs((self.pos[1] + pos[1]) / 2)
        return pos

    def getState(self):
        return self.state

    def is_dead(self):
        return self.dead

    def getSize(self):
        if self.state == self.states[0]:
            size = 2
        elif self.state == self.states[1]:
            size = 3
        elif self.state == self.states[2]:
            size = 4
        elif self.state == self.states[3]:
            size = 5
        else:
            size = 5  # or some other default value
        return size


class Duck(Animal):
    time2hatch = 2
    states = ["Duck egg", "Duckling", "Adult duck", "Dead duck"]

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def stepChange(self, grid, limit, bounding_value, num_of_terrain, moveType):
        if not self.dead:
            self.age += 1
        if self.state == "Duck egg":
            if self.age > self.time2hatch:
                self.state = "Duckling"
        elif self.state == "Duckling":
            if self.age > 4:
                self.state = "Adult duck"
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == "Adult duck":
            if self.age > 10:
                self.state = "Dead duck"
                self.dead = True
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)

    def inRange_Repro(self, pos):
        return abs(self.pos[0] - pos[0]) < 8 and abs(self.pos[1] - pos[1]) < 8

    def getSize(self):
        if self.state == "Duck egg":
            size = 5
        else:
            size = 15
        return size


class Newt(Animal):
    time2hatch = 2
    states = ["Newt egg", "Newt larva", "Juvenile newt", ["Regular newt", "Poisonous newt"], "Dead newt"]

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def stepChange(self, grid, limit, bounding_value, num_of_terrain, moveType):
        if not self.dead:
            self.age += 1
        if self.state == "Newt egg":
            if self.age > self.time2hatch:
                self.state = "Newt larva"
        elif self.state == "Newt larva":
            if self.age > 4:
                self.state = "Juvenile newt"
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == "Juvenile newt":
            if self.age > 6:
                chance = random.randint(0, 100)
                if chance > 80:
                    self.state = self.states[3][0]
                else:
                    self.state = self.states[3][1]
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            if self.age > 10:
                self.state = "Dead newt"
                self.dead = True
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)

    def getSize(self):
        if self.state == "Newt egg":
            size = 2
        elif self.state == "Newt larva":
            size = 3
        elif self.state == "Juvenile newt":
            size = 4
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            size = 5
        else:
            size = 5  # or some other default value
        return size


class Shrimp(Animal):
    time2hatch = 1
    states = [
        "Shrimp egg",
        "Larval shrimp",
        "Juvenile shrimp",
        ["Regular shrimp", "Poisonous shrimp"],
        "Dead shrimp",
    ]

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def stepChange(self, grid, limit, bounding_value, num_of_terrain, moveType):
        if not self.dead:
            self.age += 1
        if self.state == "Shrimp egg":
            if self.age > self.time2hatch:
                self.state = "Shrimp larva"
        elif self.state == "Shrimp larva":
            if self.age > 4:
                self.state = "Juvenile shrimp"
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == "Juvenile shrimp":
            if self.age > 6:
                chance = random.randint(0, 100)
                if chance > 80:
                    self.state = self.states[3][0]
                else:
                    self.state = self.states[3][1]
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            if self.age > 10:
                self.state = "Dead shrimp"
                self.dead = True
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)

    def getSize(self):
        if self.state == "Shrimp egg":
            size = 2
        elif self.state == "Shrimp larva":
            size = 3
        elif self.state == "Juvenile shrimp":
            size = 4
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            size = 5
        else:
            size = 5  # or some other default value
        return size


class Alga(Animal):
    time2hatch = 1
    states = ["Algal spore", "Algal cell", "Algal colony", ["Chlorella", "Red Tide"], "Dead alga"]

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def stepChange(self, grid, limit, bounding_value, num_of_terrain, moveType):
        if not self.dead:
            self.age += 1
        if self.state == "Algal spore":
            if self.age > self.time2hatch:
                self.state = "Algal cell"
        elif self.state == "Algal cell":
            if self.age > 4:
                self.state = "Algal colony"
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == "Algal colony":
            if self.age > 6:
                chance = random.randint(0, 100)
                if chance > 80:
                    self.state = self.states[3][0]
                else:
                    self.state = self.states[3][1]
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            if self.age > 20:
                self.state = "Dead alga"
                self.dead = True
            else:
                self.pos[0], self.pos[1] = movement(self.pos[0], self.pos[1], limit, grid, bounding_value, num_of_terrain, moveType)

    def getSize(self):
        if self.state == "Algal spore":
            size = 2
        elif self.state == "Algal cell":
            size = 3
        elif self.state == "Algal colony":
            size = 4
        elif self.state == self.states[3][0] or self.state == self.states[3][1]:
            size = 5
        else:
            size = 5  # or some other default value
        return size


class Rock(Animal):
    states = ["Stationary rock"]

    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        self.dead = False

    def __str__(self):
        return self.state + " @ " + str(self.pos)

    def stepChange(self, grid, limit, bounding_value, num_of_terrain, moveType):
        self.state = "Stationary rock"
        
    def getSize(self):
        size = 30
        return size

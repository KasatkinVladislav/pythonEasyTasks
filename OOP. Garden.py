import random

class Tomato:
    """
    this is a single tomato. it don't do anything,
    it can only grow and show its stage of maturity
    """
    def __init__(self, index, stage):
        self.index = index
        self.stage = stage

    def grow(self):
        self.stage.changeMaturity()

    def showStage(self):
        return self.stage.show()

class tomatoTree:
    """
    this is a tree of tomatoes. it has a list of tomatoes and when it's time to grow,
    it grows one single random tomato to next stage
    if someone needs to harvest a tomato, then he can harvest every red tomato on this tree
    """
    def __init__(self, tomatoCount):
        self.tomatoList = []
        for i in range (tomatoCount):
            self.tomatoList.append(Tomato(i, Maturity()))

    def showStage(self):
        for i in self.tomatoList:
            print(i.showStage())

    def growTomatoes(self):
        tomato = random.choice(self.tomatoList)
        tomato.grow()

    def giveHarvest(self):
        harvest = ""
        for i in self.tomatoList:
            if i.showStage() == "red":
                harvest = harvest + "we got tomato number " + str(self.tomatoList.index(i))
                self.tomatoList.remove(i)
        return harvest

class Gardener:
    """
    gardener is someone who takes care of a plant, he makes it grow and he harvest red tomatoes
    """
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def takeCare(self):
        self.plant.growTomatoes()

    def getHarvest(self):
        return self.plant.giveHarvest()

    def checkStage(self):
        return self.plant.showStage()

class Maturity:
    """
    learning exercise offered to describe stages of maturity through linked list
    i didn't saw it and implemented its functions in a brand new class
    """
    def __init__(self):
        self.states = ("disabled", "blooming", "green", "red")
        self.currentStage = 0

    def changeMaturity(self):
        self.currentStage = self.currentStage + 1

    def show(self):
        return self.states[self.currentStage]

if __name__ == '__main__':
    treeOfTomatoes = tomatoTree(4)
    tomas = Gardener("Tomas", treeOfTomatoes)
    tomas.takeCare()
    print(tomas.checkStage())
    tomas.takeCare()
    tomas.takeCare()
    print(tomas.checkStage())
    print(tomas.getHarvest())
    tomas.takeCare()
    tomas.takeCare()
    tomas.takeCare()
    print(tomas.checkStage())
    print(tomas.getHarvest())    

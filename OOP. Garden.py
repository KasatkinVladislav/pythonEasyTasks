
class Tomato:
    def __init__(self, index, stage):
        self.index = index
        self.stage = stage

    def grow(self):
        self.stage = self.stage + 1 #that's a plug

    def showStage(self):
        return self.stage

class tomatoTree:
    def __init__(self, tomatoCount):
        self.tomatoList = list()
        for i = 1 to tomatoCount:
            self.tomatoList.add(Tomato(i - 1, 0))

    def showStage(self):
        for i = 1 to len(self.tomatoList):
            print(self.tomatoList[i - 1].showStage())

    def growTomatoes(self):
        for i = 1 to len(self.tomatoList):
            self.tomatoList[i - 1].grow())

    def giveHarvest(self):
        self.tomatoList.clear() #plug

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def takeCare(self):
        self.plant.growTomatoes()


        

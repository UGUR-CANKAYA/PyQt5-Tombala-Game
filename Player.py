import random

class Player:
    def __init__(self,name):
        self.name=name

    def buildCard(self):
        bingo=list(random.sample(range(1,91),15))
        # random.shuffle(bingo)
        set1 = bingo[0:5]
        set1.sort()
        set2 = bingo[5:10]
        set2.sort()
        set3 = bingo[10:15]
        set3.sort()

        self.set=[set1,set2,set3]
        return self.set



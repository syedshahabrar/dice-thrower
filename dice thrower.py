import random

class Dice:
    def __init__(self):
        self.throws = None

    def throwDice(self):
        throw1 = random.randint(1,6)
        throw2 = random.randint(1,6)
        self.throws = (throw1, throw2)
        return self.throws

    def checkDouble(self):
        return self.throws[0] == self.throws[1]

    def generateThrees(self):
        count = 0
        flag = True

        while (flag):
            self.throwDice()
            count += 1
            if self.throws[0] == 3 and self.throws[1] == 3:
                flag = False
                break
        return count

    def getDice (self):
        return self.throws

    def __str__(self):
        return "{0}".format(self.throws)

d = Dice()
result = d.throwDice()
print(result)
print(d.checkDouble())
print(d.generateThrees())
print(d.getDice())
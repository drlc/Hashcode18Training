from Pizza import *

class Parser(object):

    def readFile(self, filePath):
        with open(filePath) as f:
            content = f.readlines()

        content = [x.strip() for x in content]

        firstlineList = content[0].split(' ')

        row = int(firstlineList[0])
        column = int(firstlineList[1])
        minIngredientPerSlice = int(firstlineList[2])
        maxCellsPerSlice = int(firstlineList[3])

        pizzaMatrix = [[val for val in list(line)] for line in content[1:]]

        pizza = Pizza(row, column, minIngredientPerSlice, maxCellsPerSlice, pizzaMatrix)

        return pizza


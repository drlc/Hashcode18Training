class Pattern(object):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def setPoint(self,x,y):
        self.coordinates = (x, y)

    def isFitting(self, pizza):
        if self.coordinates:
            minMashroom = pizza.minIngredientsInSlice
            minTomatoes = pizza.minIngredientsInSlice

            matrix = pizza.Matrix

            for row in range(self.h):
                for col in range(self.w):
                    if matrix[self.coordinates[1]+col][self.coordinates[0]+row] == 'M':
                        minMashroom = minMashroom - 1
                    else:
                        minTomatoes = minTomatoes - 1

            if minMashroom == 0 and minTomatoes == 0:
                return True
            else:
                return False
        else:
            False

    def isOverlapping(self, pattern, pizza):
        if self.coordinates and self.isInsidePizza(pizza):
            True
        else:
            False

    def isInsidePizza(self, pizza):
        if pizza.rows >= (self.coordinates[0] + self.h) and pizza.columns >= (self.coordinates[1] + self.w):
            return True
        print 'is out of Pizza'
        return False

    def getCoordinate(self):
        allCells = []
        for row in range(self.h):
            for col in range(self.w):
                tup = (self.coordinates[1]+col, self.coordinates[0]+row)
                allCells.append(tup)
        return allCells

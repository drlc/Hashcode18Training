class Parser(object):

    def readFile(self, filePath):
        with open(filePath) as f:
            content = f.readlines()

        content = [x.strip() for x in content]

        firstlineList = content[0].split(' ')

        row = int(firstlineList[0])
        column = int(firstlineList[1])
        minIngredientPerSlice = firstlineList[2]
        maxCellsPerSlice = firstlineList[3]

        Matrix = [[val for val in list(line)] for line in content[1:]]
        print Matrix

        return Matrix


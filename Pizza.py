class Pizza(object):

    def __init__(self, rows, columns, minIngredientsInSlice, maxCellsInSlice, Matrix):
        self.minIngredientsInSlice = minIngredientsInSlice
        self.maxCellsInSlice = maxCellsInSlice
        self.Matrix = Matrix
        self.rows = rows
        self.columns = columns

    def __str__(self):
        print self.Matrix
        return ''


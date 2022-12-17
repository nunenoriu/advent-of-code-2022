# Requirements:
# tree house should be hidden
# 0 shortest 9 tallest
# tree is visible if all trees between it and an edge of grid are shorter

class DayEight:

    def __init__(self):
        text_file = open("../inputs/dayEight.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.sizeDict = {}
        self.rowSplit = []
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        for row in self.dataSplit:
            self.rowSplit.append(list(row))

    def calculate(self):
        numberOfVisibleTrees = 0
        rowCount = 0
        for row in self.rowSplit:
            print("row) {}".format(row))
            if rowCount == 0 or rowCount == len(self.rowSplit) - 1:
                numberOfVisibleTrees += len(row)
            else:
                columnCount = 0
                rowLength = len(row)
                for column in row:
                    print("columnCount {} column {} rowLength {}".format(columnCount, column, rowLength))
                    if columnCount == 0 or columnCount == rowLength - 1:
                        numberOfVisibleTrees += 1
                    else:
                        left = self.check_left(columnCount, row, column)
                        if 1 == left:
                            numberOfVisibleTrees += 1
                        else:
                            right = self.check_right(columnCount, row, column)
                            if 1 == right:
                                numberOfVisibleTrees += 1
                            else:
                                top = self.check_top(columnCount, column, rowCount)
                                if 1 == top:
                                    numberOfVisibleTrees += 1
                                else:
                                    bottom = self.check_bottom(columnCount, column, rowCount)
                                    if 1 == bottom:
                                        numberOfVisibleTrees += 1
                    columnCount += 1
            rowCount += 1
        print("numberOfVisibleTrees {}".format(numberOfVisibleTrees))

    def calculate_scenic_score(self):
        rowCount = 0
        distance = 0
        for row in self.rowSplit:
            print("row {}".format(row))
            if rowCount == 0 or rowCount == len(self.rowSplit) - 1:
                print("ignore row {}".format(row))
            else:
                columnCount = 0
                rowLength = len(row)
                for column in row:
                    currentDistance = 0
                    print("columnCount {} column {} rowLength {}".format(columnCount, column, rowLength))
                    if columnCount == 0 or columnCount == rowLength - 1:
                        print("ignore column {}".format(row))
                    else:
                        left = self.check_left_dist(columnCount, row, column)
                        right = self.check_right_dist(columnCount, row, column)
                        top = self.check_top_dist(columnCount, column, rowCount)
                        bottom = self.check_bottom_dist(columnCount, column, rowCount)
                        print("left {} right {} top {} bottom {}".format(left, right, top, bottom))
                        currentDistance = left * right * top * bottom
                        print("currentDistance {}".format(currentDistance))
                    columnCount += 1
                    if distance < currentDistance:
                        distance = currentDistance
            rowCount += 1

        print("distance {}".format(distance))

    def check_left(self, columnCount, row, column):
        i = columnCount - 1
        while i >= 0:
            if row[i] >= column:
                return 0
            i -= 1
        print("left row {} column {}".format(row, column))
        return 1

    def check_left_dist(self, columnCount, row, column):
        dist = 0
        i = columnCount - 1
        while i >= 0:
            if row[i] >= column:
                return dist + 1
            else:
                dist += 1
            i -= 1
        print("left row {} column {}".format(row, column))
        return dist

    def check_right(self, columnCount, row, column):
        i = columnCount + 1
        while i < len(row):
            if row[i] >= column:
                return 0
            i += 1
        print("right row {} column {}".format(row, column))
        return 1

    def check_right_dist(self, columnCount, row, column):
        dist = 0
        i = columnCount + 1
        while i < len(row):
            if row[i] >= column:
                return dist + 1
            else:
                dist += 1
            i += 1
        print("right row {} column {}".format(row, column))
        return dist

    def check_top(self, columnCount, column, rowCount):
        i = rowCount - 1
        while i >= 0:
            row = self.rowSplit[i]
            if row[columnCount] >= column:
                return 0
            i -= 1
        print("top rowCount {} column {}".format(rowCount, column))
        return 1

    def check_top_dist(self, columnCount, column, rowCount):
        i = rowCount - 1
        dist = 0
        while i >= 0:
            row = self.rowSplit[i]
            if row[columnCount] >= column:
                return dist + 1
            else:
                dist += 1
            i -= 1
        print("top rowCount {} column {}".format(rowCount, column))
        return dist

    def check_bottom(self, columnCount, column, rowCount):
        i = rowCount + 1
        while i < len(self.rowSplit):
            row = self.rowSplit[i]
            if row[columnCount] >= column:
                return 0
            i += 1
        print("bottom rowCount {} column {}".format(rowCount, column))
        return 1

    def check_bottom_dist(self, columnCount, column, rowCount):
        i = rowCount + 1
        dist = 0
        while i < len(self.rowSplit):
            row = self.rowSplit[i]
            if row[columnCount] >= column:
                return dist + 1
            else:
                dist += 1
            i += 1
        print("bottom rowCount {} column {}".format(rowCount, column))
        return dist

if __name__ == '__main__':
    day = DayEight()
    print("Day eight exercise!")
    day.do_split()
    day.split_rows()
    day.calculate_scenic_score()
    day.say_state()

# 99
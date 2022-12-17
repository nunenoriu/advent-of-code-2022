# Requirements:
# X register controls the horizontal sprite
# sprite is 3 pixels wide
# 40w x 6h
# leftmost 0 rightmost 39
# CRT draws a single pixel during each cycle
#

class DayTen:

    def __init__(self):
        text_file = open("../inputs/dayTen.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.rowSplit = []
        text_file.close()

    def say_state(self):
        print("rowSplit {}".format(self.rowSplit))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        for row in self.dataSplit:
            split = row.split(" ")
            self.rowSplit.append(split)

    def draw(self):
        sprite = '###.....................................'
        result = ''
        cycle = 0
        position = -1
        for row in self.rowSplit:
            instruction = row[0]
            cycle += 1
            position += 1
            result += sprite[position]
            if cycle % 40 == 0:
                result = result + '\n'
                position = -1
            if instruction == 'addx':
                cycle += 1
                position += 1
                result += sprite[position]
                if cycle % 40 == 0:
                    result = result + '\n'
                    position = -1
                value = int(row[1])
                sprite = sprite[-value:] + sprite[:-value]

        print(result)

if __name__ == '__main__':
    day = DayTen()
    print("Day eight exercise!")
    day.do_split()
    day.split_rows()
    day.draw()
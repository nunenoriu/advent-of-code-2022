# Requirements:
# clock circuit ticks at constant rate
# each tick is called a cycle
# CPU has a single register X which starts with 1
# addx V after 2 cycles register is increased by value V
# noop one cycle. no effect

class DayTen:

    def __init__(self):
        text_file = open("../inputs/dayTen.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.rowSplit = []
        self.signal = 0
        self.cycles = [20, 60, 100, 140, 180, 220]
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))
        print("signal {}".format(self.signal))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        for row in self.dataSplit:
            split = row.split(" ")
            self.rowSplit.append(split)

    def calculate(self):
        x_cycle = [1, 1]
        for row in self.rowSplit:
            # print("row {}".format(row))
            instruction = row[0]
            x_cycle[1] += 1
            self.checkIfNeedToGetSignal(x_cycle)
            # if instruction == "noop":
            #     print("x_cycle {}".format(x_cycle))
            if instruction == "addx":
                x_cycle = self.addx(x_cycle, int(row[1]))


    def addx(self, x_cycle, amount):
        x_cycle[1] += 1
        x_cycle[0] += amount
        # print("x_cycle {}".format(x_cycle))
        self.checkIfNeedToGetSignal(x_cycle)
        return x_cycle

    def getSignalStrengh(self, x_cycle):
        sum = x_cycle[0] * x_cycle[1]
        self.signal += sum
        print("signal {} x_cycle {} sum {}".format(self.signal, x_cycle, sum))


    def checkIfNeedToGetSignal(self, x_cycle):
        if x_cycle[1] in self.cycles:
            self.getSignalStrengh(x_cycle)

if __name__ == '__main__':
    day = DayTen()
    print("Day eight exercise!")
    day.do_split()
    day.split_rows()
    day.calculate()
    day.say_state()

# 13740
# Requirements:
# Rock      A   X   1
# Paper     B   Y   2
# Scissors  C   Z   3
# total score = shape selected + outcome
# outcome: 0 lost, 3 draw, 6 won
# X - loose, Y - draw, Z - win

class DayTwo:

    def __init__(self):
        text_file = open("../inputs/dayTwo.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.largestNumber = 0
        self.allNumbers = []
        self.sortedNumbers = []
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def get_score(self):
        total = 0
        for x in self.dataSplit:
            total += self.get_pair_score_2(x)
        print("total {}".format(total))

    def get_pair_score(self, pair):
        match pair:
            case "A X":
                return 4
            case "A Y":
                return 8
            case "A Z":
                return 3
            case "B X":
                return 1
            case "B Y":
                return 5
            case "B Z":
                return 9
            case "C X":
                return 7
            case "C Y":
                return 2
            case "C Z":
                return 6

    def get_pair_score_2(self, pair):
        match pair:
            case "A X":
                return 3
            case "A Y":
                return 4
            case "A Z":
                return 8
            case "B X":
                return 1
            case "B Y":
                return 5
            case "B Z":
                return 9
            case "C X":
                return 2
            case "C Y":
                return 6
            case "C Z":
                return 7



if __name__ == '__main__':

    day = DayTwo()
    print("Day two exercise!")
    day.do_split()
    day.get_score()
    day.say_state()

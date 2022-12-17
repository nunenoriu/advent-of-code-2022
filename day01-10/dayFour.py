# Requirements:
# section with unique ID number
# - first = second:
#
class DayFour:

    def __init__(self):
        text_file = open("../inputs/dayFour.txt", 'r')
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
            innersplit = x.split(",")
            first = innersplit[0].split("-")
            second = innersplit[1].split("-")
            one = int(first[0])
            two = int(first[1])
            three = int(second[0])
            four = int(second[1])
            if one < three:
                if two >= three:
                    total += 1
                    print("first 1 {}".format(first))
                    print("second 1 {}".format(second))
            elif one > three:
                if one <= four:
                    total += 1
                    print("first 2 {}".format(first))
                    print("second 2 {}".format(second))
            elif one == three:
                total += 1
                print("first 3 {}".format(first))
                print("second 3 {}".format(second))


        print("total {}".format(total))


    def get_letter_score(self, letter):
        score = 0
        if letter.isupper():
            score = ord(letter) - 38
        else:
            score = ord(letter) - 96
        return score


if __name__ == '__main__':

    day = DayFour()
    print("Day four exercise!")
    day.do_split()
    day.get_score()
    day.say_state()

# Requirements:
# 2 compartments in each rucksack
# every item is a letter
# it's case-sensitive
# each compartment has same number of items

# split in half
# find matching character
# find it's score

class DayThree:

    def __init__(self):
        text_file = open("../inputs/dayThree.txt", 'r')
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
            half1 = x[:len(x)//2]
            half2 = x[len(x)//2:]
            h = set(half1)
            j = set(half2)
            a = list(h & j)
            print(a)
            for i in a:
                total += self.get_letter_score(i)
        print("total {}".format(total))

    def get_score_2(self):
        total = 0
        temp = []
        counter = 0
        for x in self.dataSplit:
            temp.append(x)
            counter += 1
            if counter == 3:
                a = list(set(temp[0]) & set(temp[1]) & set(temp[2]))
                for i in a:
                    print(i)
                    total += self.get_letter_score(i)
                counter = 0
                temp = []
        print("total {}".format(total))



    def get_letter_score(self, letter):
        score = 0
        if letter.isupper():
            score = ord(letter) - 38
        else:
            score = ord(letter) - 96
        return score


if __name__ == '__main__':

    day = DayThree()
    print("Day three exercise!")
    day.do_split()
    day.get_score()
    day.say_state()

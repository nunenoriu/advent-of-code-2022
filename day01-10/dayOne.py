# Requirements:
#   input: Calories
#   - Who carries most Calories
#   -
class DayOne:

    def __init__(self):
        text_file = open("../inputs/dayOne.txt", 'r')
        self.caloriesData = text_file.read()
        self.splitCals = []
        self.largestNumber = 0
        self.allNumbers = []
        self.sortedNumbers = []
        text_file.close()

    def say_state(self):
        print("Largest Number {}".format(self.largestNumber))
        print("All Numbers {}".format(self.allNumbers))

    def find_biggest_cals(self):
        self.splitCals = self.caloriesData.split("\n\n")

    def get_largest_number(self):
        for x in self.splitCals:
            a = x.split("\n")
            total = 0
            for z in a:
                total = total + int(z)
                self.allNumbers.append(total)
            if total > self.largestNumber:
                self.largestNumber = total

    def sort_numbers(self):
        self.sortedNumbers = sorted(self.allNumbers)
        print("Sorted Numbers {}".format(self.sortedNumbers))

    def get_last_element(self):
        a = self.sortedNumbers.pop()
        print("Number {}".format(a))

    def get_last_element_sum(self, x):
        total = 0;
        z = int(x)
        while z > 0:
            a = self.sortedNumbers.pop()
            total += a
            z -= 1

        print("Number {}".format(total))

if __name__ == '__main__':

    day_one = DayOne()
    print("Day one exercise!")
    day_one.find_biggest_cals()
    day_one.get_largest_number()
    day_one.sort_numbers()
    action = input("How many largest cals to add?")
    day_one.get_last_element_sum(action)
    day_one.say_state()

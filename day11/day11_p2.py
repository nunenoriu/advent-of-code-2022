# Requirements:
# starting items  - list worry level
# operation - shows how worry level changes when item is inspected
# test - shows how monkey uses worry level to throw item next
# after inspection, before test, if inspection didn't cause damage worrylevel/3 and floored
# monkeys goes in turn
# floor - each monkey takes a single turn
# when item is thrown, it goes at the end of the list
# if no items, turn ends
import math
from math import floor


class DayEleven:

    def __init__(self):
        self.monkeys2 = [
            [53, 89, 62, 57, 74, 51, 83, 97],
            [85, 94, 97, 92, 56],
            [86, 82, 82],
            [94, 68],
            [83, 62, 74, 58, 96, 68, 85],
            [50, 68, 95, 82],
            [75],
            [92, 52, 85, 89, 68, 82]
        ]

        self.monkeys = [
            [79, 98],
            [54, 65, 75, 74],
            [79, 60, 97],
            [74]
        ]

        self.activity2 = [0, 0, 0, 0, 0, 0, 0, 0]

        self.activity = [0, 0, 0, 0]

        self.min_number = [8388608, 524288, 8192, 131072]


    def calculate(self):
        round = 1
        while round < 21:
            monkeyCounter = 0
            for monkey in self.monkeys:
                while len(monkey) > 0:
                    item = monkey.pop(0)
                    match monkeyCounter:
                        case 0:
                            item = floor(item * 3 / 3)
                            if item % 13 == 0:
                                self.monkeys[1].append(item)
                            else:
                                self.monkeys[5].append(item)
                        case 1:
                            item = floor((item + 2) / 3)
                            if item % 19 == 0:
                                self.monkeys[5].append(item)
                            else:
                                self.monkeys[2].append(item)
                        case 2:
                            item = floor((item + 1) / 3)
                            if item % 11 == 0:
                                self.monkeys[3].append(item)
                            else:
                                self.monkeys[4].append(item)
                        case 3:
                            item = floor((item + 5) / 3)
                            if item % 17 == 0:
                                self.monkeys[7].append(item)
                            else:
                                self.monkeys[6].append(item)
                        case 4:
                            item = floor((item + 4) / 3)
                            if item % 3 == 0:
                                self.monkeys[3].append(item)
                            else:
                                self.monkeys[6].append(item)
                        case 5:
                            item = floor((item + 8) / 3)
                            if item % 7 == 0:
                                self.monkeys[2].append(item)
                            else:
                                self.monkeys[4].append(item)
                        case 6:
                            item = floor((item * 7) / 3)
                            if item % 5 == 0:
                                self.monkeys[7].append(item)
                            else:
                                self.monkeys[0].append(item)
                        case 7:
                            item = floor((item * item) / 3)
                            if item % 2 == 0:
                                self.monkeys[0].append(item)
                            else:
                                self.monkeys[1].append(item)
                    self.activity[monkeyCounter] += 1
                monkeyCounter += 1
            print('round {} monkeys {}'.format(round, self.monkeys))
            round += 1
        print('activity {}'.format(self.activity))
        self.get_result()

    def calculate2(self):
        round = 1
        while round < 21:
            monkeyCounter = 0
            for monkey in self.monkeys:
                while len(monkey) > 0:
                    item = monkey.pop(0)
                    # print('item {} monkeyCounter {}'.format(item, monkeyCounter))
                    match monkeyCounter:
                        case 0:
                            item = self.reduce_number(item, 23)
                            item = item * 19
                            if item % 23 == 0:
                                self.monkeys[2].append(item)
                            else:
                                self.monkeys[3].append(item)
                        case 1:
                            item = self.reduce_number(item, 19)
                            item = item + 6
                            if item % 19 == 0:
                                self.monkeys[2].append(item)
                            else:
                                self.monkeys[0].append(item)
                        case 2:
                            item = self.reduce_number(item, 13)
                            item = item * item
                            if item % 13 == 0:
                                self.monkeys[1].append(item)
                            else:
                                self.monkeys[3].append(item)
                        case 3:
                            item = self.reduce_number(item, 17)
                            item = item + 3
                            if item % 17 == 0:
                                self.monkeys[0].append(item)
                            else:
                                self.monkeys[1].append(item)
                    self.activity[monkeyCounter] += 1
                monkeyCounter += 1
            # print('round {} monkeys {}'.format(round, self.monkeys))
            round += 1
        print('activity {}'.format(self.activity))
        self.get_result()

    def calculate3(self):
        round = 1
        while round < 21:
            monkeyCounter = 0
            for monkey in self.monkeys:
                while len(monkey) > 0:
                    item = monkey.pop(0)
                    match monkeyCounter:
                        case 0:
                            item = floor((item * 19) / 3)
                            if item % 23 == 0:
                                self.monkeys[2].append(item)
                            else:
                                self.monkeys[3].append(item)
                        case 1:
                            item = floor((item + 6) / 3)
                            if item % 19 == 0:
                                self.monkeys[2].append(item)
                            else:
                                self.monkeys[0].append(item)
                        case 2:
                            item = floor((item * item) / 3)
                            if item % 13 == 0:
                                self.monkeys[1].append(item)
                            else:
                                self.monkeys[3].append(item)
                        case 3:
                            item = floor((item + 3) / 3)
                            if item % 17 == 0:
                                self.monkeys[0].append(item)
                            else:
                                self.monkeys[1].append(item)
                    self.activity[monkeyCounter] += 1
                monkeyCounter += 1
            # print('round {} monkeys {}'.format(round, self.monkeys))
            round += 1
        print('activity {}'.format(self.activity))
        self.get_result()

    def get_result(self):
        largest = max(self.activity)
        self.activity.remove(largest)
        second_largest = max(self.activity)
        print(largest * second_largest)

    def reduce_number(self, number, power):
        n = number % power
        new_number = n + power * 2
        print('old {} new {}'.format(number, new_number))
        return new_number

if __name__ == '__main__':
    day = DayEleven()
    print("Day eleven exercise!")
    day.calculate3()

# 10197
# x ^ 0.25 = 2.5045
# s
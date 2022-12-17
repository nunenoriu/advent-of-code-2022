class DayEleven:
    def __init__(self):

        self.monkeys = [
            [53, 89, 62, 57, 74, 51, 83, 97],
            [85, 94, 97, 92, 56],
            [86, 82, 82],
            [94, 68],
            [83, 62, 74, 58, 96, 68, 85],
            [50, 68, 95, 82],
            [75],
            [92, 52, 85, 89, 68, 82]
        ]
        self.activity = [0, 0, 0, 0, 0, 0, 0, 0]
        self.operations = []
        self.mod_arguments = [13, 19, 11, 17, 3, 7, 5, 2]
        self.true_monkeys = [1, 5, 3, 7, 3, 2, 7, 0]
        self.false_monkeys = [5, 2, 4, 6, 6, 4, 0, 1]

    @staticmethod
    def operation_0(number):
        return number * 3

    @staticmethod
    def operation_1(number):
        return number + 2

    @staticmethod
    def operation_2(number):
        return number + 1

    @staticmethod
    def operation_3(number):
        return number + 5

    @staticmethod
    def operation_4(number):
        return number + 4

    @staticmethod
    def operation_5(number):
        return number + 8

    @staticmethod
    def operation_6(number):
        return number * 7

    @staticmethod
    def operation_7(number):
        return number * number

    def assign_ops(self):
        self.operations = [self.operation_0, self.operation_1, self.operation_2, self.operation_3,
                           self.operation_4, self.operation_5, self.operation_6, self.operation_7]

    def get_lcn(self):
        result = 1
        for argument in self.mod_arguments:
            result *= argument
        return result

    def calculate(self):
        round = 0
        lcn = self.get_lcn()
        while round < 10000:
            round += 1
            for index, monkey in enumerate(self.monkeys):
                while len(monkey) > 0:
                    item = monkey.pop(0)
                    self.activity[index] += 1
                    new_number = self.operations[index](item) % lcn
                    if new_number % self.mod_arguments[index] == 0:
                        self.monkeys[self.true_monkeys[index]].append(new_number)
                    else:
                        self.monkeys[self.false_monkeys[index]].append(new_number)
        print(self.activity)

    def get_result(self):
        largest = max(self.activity)
        self.activity.remove(largest)
        second_largest = max(self.activity)
        print('largest * largest {}'.format(largest * second_largest))

if __name__ == '__main__':
    day = DayEleven()
    print("Day eleven exercise!")
    day.assign_ops()
    day.calculate()
    day.get_result()

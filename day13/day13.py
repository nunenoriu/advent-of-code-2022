# Distress Signal
# out of order, need to reorder
# how many pairs are in right order?
# each packet is a list
# first left, second right

class Day13:
    def __init__(self):
        with open("puzzleInput.txt", 'r') as file:
            self.data = file.read()
        self.grid = self.create_grid(self.data)

    def create_grid(self, file):
        grid = file.split("\n\n")
        print('grid {}'.format(grid))
        print(len(grid))
        return grid

    def say_state(self):
        print(self.grid)

    def calculate(self):
        sum = 0
        current_pair_index = 1
        for pair in self.grid:
            split_pair = pair.split('\n')
            # print('index {} pair {} '.format(current_pair_index, split_pair))
            left = self.convert_to_list(split_pair[0])
            right = self.convert_to_list(split_pair[1])
            if self.in_order(left, right):
                print('correct index {} pair {}'.format(current_pair_index, pair))
                sum += current_pair_index
            else:
                print('incorrect index {} pair {}'.format(current_pair_index, pair))
            current_pair_index += 1
        print('result: {}'.format(sum))

    def convert_to_list(self, string):
        bunch_of_chars = [*string]
        result = {}
        depth = 0
        list_index = 0
        should_check = False
        for char_index, char in enumerate(bunch_of_chars):
            if char == '[':
                depth += 1
                list_index += 1
                result[list_index] = []
            elif char == ']':
                depth -= 1
                should_check = True
            elif char == ',':
                continue
            else:
                # print(char)
                if depth == 1 and should_check:
                    if bunch_of_chars[char_index + 1] == ']':
                        # print('char {} depth {} result len {}'.format(char, depth, len(result)))
                        list_index += 1
                        result[list_index] = [-1]
                result[list_index].append(int(char))
        # print(string, result)
        return result

    def in_order(self, left, right):
        if len(left) > len(right):
            print('len(left) > len(right) {} {}'.format(len(left), len(right)))
            return False
        else:
            for key in left:
                # print('key {} value'.format(key))
                left_values = left[key]
                right_values = right[key]
                check_first_only = False
                if left_values.count(-1) > 0:
                    left_values.remove(-1)
                    check_first_only = True
                if right_values.count(-1) > 0:
                    right_values.remove(-1)
                    check_first_only = True
                if check_first_only:
                    if left_values[0] > right_values[0]:
                        print('left_values[0] > right_values[0] {} {}'.format(left_values[0], right_values[0]))
                        return False
                elif len(left_values) > len(right_values):
                    if len(left_values) > len(right_values):
                        print('len(left_values) > len(right_values {} {}'.format(len(left_values), len(right_values)))
                        return False
                else:
                    for index, value in enumerate(left_values):
                        if value > right_values[index]:
                            print('value > right_values[index] {} {}'.format(value, right_values[index]))
                            return False
        return True

if __name__ == '__main__':
    print('Day Thirteen!')
    day = Day13()
    day.say_state()
    day.calculate()

#323
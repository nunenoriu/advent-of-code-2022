# Requirements:
# section with unique ID number
# FIFO
# use withopen instead
class DayFive:

    def __init__(self):
        text_file = open("../inputs/dayFive.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.stacks = []
        self.instructions = []
        self.stackStacks = [[], [], [], [], [], [], [], [], []]
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))
        print("Stacks {}".format(self.stacks))
        print("Instructions {}".format(self.instructions))
        print("stackStacks {}".format(self.stackStacks))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def separate(self):
        n = 0
        while n < 8:
            self.stacks.append(self.dataSplit[n])
            n += 1
        n += 2
        while n < len(self.dataSplit):
            self.instructions.append(self.dataSplit[n])
            n += 1

    def stack_stacks(self):
        for row in self.stacks:
            row_parts = row.split(" ")
            print("row_parts: {} {}".format(row_parts, len(row_parts)))
            current_part = 0
            current_stack = 0
            j = 0
            while current_part < len(row_parts):
                print("current_part: {}".format(row_parts[current_part]))
                if row_parts[current_part] == "":
                    j += 1
                    if j == 4:
                        j = 0
                        current_stack += 1
                        print("current_stack: {} {}".format(current_stack, self.stackStacks[current_stack]))
                else:
                    self.stackStacks[current_stack].insert(0, row_parts[current_part])
                    print("current_stack: {} {}".format(current_stack, self.stackStacks[current_stack]))
                    current_stack += 1
                current_part += 1

        print("stackStacks: {}".format(self.stackStacks))


    def move_around(self):
        for x in self.instructions:
            parts = x.split()
            print("parts: {}".format(parts))
            from_number = int(parts[3]) - 1
            to_number = int(parts[5]) - 1
            this_many = int(parts[1])
            print("parts: {} {} {}".format(from_number, to_number, this_many))
            i = 0
            while i < this_many:
                from_stack = self.stackStacks[from_number]
                print("from_stack: {}".format(from_stack))
                box_to_move = self.stackStacks[from_number].pop(len(self.stackStacks[from_number])- (this_many - i))
                self.stackStacks[to_number].append(box_to_move)
                i += 1

    def print_stacks(self):
        result = ''
        for x in self.stackStacks:
            result += x.pop(len(x)-1)
        print("result: {}".format(result))

if __name__ == '__main__':
    day = DayFive()
    print("Day five exercise!")
    day.do_split()
    day.separate()
    day.stack_stacks()
    day.move_around()
    day.say_state()
    day.print_stacks()

# VLBGSPWSC
# VWLCWGSDQ
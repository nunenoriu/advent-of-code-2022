# Requirements:
# Device needs to lock on to their system
# Add subroutine to detect a start-of-the-packet marker
# Four chars that are all different
# Find number of characters from the beginning of the buffer to the end of first four-char marker

class DayFive:

    def __init__(self):
        text_file = open("../inputs/daySix.txt", 'r')
        self.data = text_file.read()
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))

    def separate(self):
        data_split = list(self.data)
        n = 3
        print("len(data_split) {}".format(len(data_split)))
        print("data_split {}".format(data_split))
        while n < len(data_split):
            one = data_split[n - 3]
            two = data_split[n - 2]
            three = data_split[n - 1]
            four = data_split[n]
            print("values {} {} {} {}".format(one, two, three, four))
            if one == two or one == three or one == four or two == three or two == four or three == four:
                print("n {}".format(n))
            else:
                print("Result {}".format(n + 1))
                return n
            n += 1

    def separate_two(self):
        start = 0
        end = start + 15
        while end <= len(self.data):
            data_split = list(self.data[start:end])
            one = data_split[0]
            two = data_split[1]
            three = data_split[2]
            four = data_split[3]
            five = data_split[4]
            six = data_split[5]
            seven = data_split[6]
            eight = data_split[7]
            nine = data_split[8]
            ten = data_split[9]
            eleven = data_split[10]
            twelve = data_split[11]
            thirteen = data_split[12]
            fourteen = data_split[13]
            if one == two or one == three or one == four or one == five or one == six or one == seven or one == eight or one == nine or one == ten or one == eleven or one == twelve or one == thirteen or one == fourteen:
                print("one {}".format(data_split))
            elif two == three or two == four or two == five or two == six or two == seven or two == eight or two == nine or two == ten or two == eleven or two == twelve or two == thirteen or two == fourteen:
                print("two {}".format(data_split))
            elif three == four or three == five or three == six or three == seven or three == eight or three == nine or three == ten or three == eleven or three == twelve or three == thirteen or three == fourteen:
                print("three {}".format(data_split))
            elif four == five or four == six or four == seven or four == eight or four == nine or four == ten or four == eleven or four == twelve or four == thirteen or four == fourteen:
                print("four {}".format(data_split))
            elif five == six or five == seven or five == eight or five == nine or five == ten or five == eleven or five == twelve or five == thirteen or five == fourteen:
                print("five {}".format(data_split))
            elif six == seven or six == eight or six == nine or six == ten or six == eleven or six == twelve or six == thirteen or six == fourteen:
                print("six {}".format(data_split))
            elif seven == eight or seven == nine or seven == ten or seven == eleven or seven == twelve or seven == thirteen or seven == fourteen:
                print("seven {}".format(data_split))
            elif eight == nine or eight == ten or eight == eleven or eight == twelve or eight == thirteen or eight == fourteen:
                print("eight {}".format(data_split))
            elif nine == ten or nine == eleven or nine == twelve or nine == thirteen or nine == fourteen:
                print("nine {}".format(data_split))
            elif ten == eleven or ten == twelve or ten == thirteen or ten == fourteen:
                print("ten {}".format(data_split))
            elif eleven == twelve or eleven == thirteen or eleven == fourteen:
                print("eleven {}".format(data_split))
            elif twelve == thirteen or twelve == fourteen:
                print("twelve {}".format(data_split))
            elif thirteen == fourteen:
                print("thirteen {}".format(data_split))
            else:
                print("Result {}".format(end - 1))
                return end
            start += 1
            end += 1

if __name__ == '__main__':
    day = DayFive()
    print("Day five exercise!")
    result = day.separate_two()
    # print("Result".format(result))

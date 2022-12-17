# Requirements:
# Determine total size of each directory
# Find all directories of at most 100000

class DayFive:

    def __init__(self):
        text_file = open("../inputs/daySeven.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.sizeDict = {}
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def calculate(self):
        path = []
        for line in self.dataSplit:
            print("line {}".format(line))
            if line.startswith('$'):
                if line.startswith('$ cd'):
                    if line.startswith('$ cd /'):
                        path = ['/']
                    elif line.startswith('$ cd ..'):
                        path.pop()
                    else:
                        lineparts = line.split()
                        path.append(lineparts[2])
                elif line.startswith('$ ls'):
                    print("list {}".format(line))
            elif line.startswith('dir'):
                print("folder {}".format(line))
            else:
                print("file {}".format(line))
                joinedPath = "-".join(path)
                print("joinedPath {}".format(joinedPath))
                lineparts = line.split()
                self.update_size(lineparts[0], joinedPath)

        print("sizeDict {}".format(self.sizeDict))

    def update_size(self, file, joinedPath):
        path = joinedPath.split('-')
        while len(path) > 0:
            joinedPath = "-".join(path)
            if joinedPath in self.sizeDict:
                print("path exists {}".format(path))
                self.sizeDict[joinedPath] += int(file)
            else:
                self.sizeDict[joinedPath] = int(file)
                print("path doesn't exist {}".format(path))
            path.pop()

    def get_size_below(self):
        size = 0
        for key in self.sizeDict:
            current_size = self.sizeDict[key]
            if current_size < 100000:
                size += current_size
        print("size {}".format(size))

    def which_to_delete(self):
        total_size = 70000000
        min_required = 30000000
        used_space = 44125990
        smallestDirectory = 44125990
        difference = 70000000
        for key in self.sizeDict:
            current_size = self.sizeDict[key]
            currently_available = total_size - used_space + current_size
            # print("currently_available {}".format(currently_available))
            if currently_available >= min_required:
                current_difference = currently_available - min_required
                print("current_difference {}".format(current_difference))
                if current_difference < difference:
                    difference = current_difference
                    smallestDirectory = current_size
        print("smallestDirectory {}".format(smallestDirectory))
        print("difference {}".format(difference))

if __name__ == '__main__':
    day = DayFive()
    print("Day seven exercise!")
    day.do_split()
    day.calculate()
    day.which_to_delete()

# 9976905
# 4473403
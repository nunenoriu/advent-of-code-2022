class DayNine:
    def __init__(self):
        text_file = open("../inputs/dayNine.txt", 'r')
        self.dataSplit = []
        self.rowSplit = []
        self.data = text_file.read()

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        for row in self.dataSplit:
            split = row.split(" ")
            self.rowSplit.append(split)

    def get_tail_coords(self):
        coords = [[0, 0], [0, 0]]
        for move in self.dataSplit:
            direction = move[0]
            steps = int(move[1:])
            for _ in range(steps):
                if direction == 'R':
                    coords[1][0] += 1
                elif direction == 'L':
                    coords[1][0] -= 1
                elif direction == 'U':
                    coords[1][1] += 1
                elif direction == 'D':
                    coords[1][1] -= 1
                coords[0] = coords[1][:]
        return coords[1]

if __name__ == '__main__':
    data = ["R1", "U1", "L1", "D1"]
    day_nine = DayNine()
    day_nine.do_split()
    day_nine.split_rows()
    tail_coords = day_nine.get_tail_coords()
    print("Tail coords:", tail_coords)

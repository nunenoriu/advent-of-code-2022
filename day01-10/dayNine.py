# Requirements:
# figure out where not to step
# knots - head and tail of the rope
#

class DayNine:

    def __init__(self):
        text_file = open("../inputs/dayNine.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        self.rowSplit = []
        self.tailCoords = []
        text_file.close()

    def say_state(self):
        print("Data split {}".format(self.dataSplit))
        print("tailCoords {}".format(set(self.tailCoords)))
        print("result {}".format(len(set(self.tailCoords))))

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        for row in self.dataSplit:
            split = row.split(" ")
            self.rowSplit.append(split)

    def calculate(self):
        coordinates = [0, 0, 0, 0]
        for row in self.rowSplit:
            steps = int(row[1])
            direction = row[0]
            i = 0
            if direction == 'R':
                while i < steps:
                    print("row {} coordinates {}".format(row, coordinates))
                    coordinates = self.right(coordinates)
                    i += 1
            if direction == 'L':
                while i < steps:
                    print("row {} coordinates {}".format(row, coordinates))
                    coordinates = self.left(coordinates)
                    i += 1
            if direction == 'U':
                while i < steps:
                    print("row {} coordinates {}".format(row, coordinates))
                    coordinates = self.up(coordinates)
                    i += 1
            if direction == 'D':
                while i < steps:
                    print("row {} coordinates {}".format(row, coordinates))
                    coordinates = self.down(coordinates)
                    i += 1

    def calculate3(self):
        coordinates = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for row in self.rowSplit:
            steps = int(row[1])
            direction = row[0]
            j = 0
            # print("row {} coordinates {}".format(row, coordinates))
            while j < steps:
                i = 0
                # print("coordinates {}".format(coordinates))
                while i < len(coordinates) - 1:
                    first = coordinates[i]
                    second = coordinates[i + 1]
                    withHead = i == 0
                    new_direction = self.determine_direction(first, second, direction, withHead)
                    two_coords = [first[0], first[1], second[0], second[1]]
                    two_coords = self.update_coordinates(two_coords, new_direction, withHead)
                    # print("i {} new_coords {}".format(i, two_coords))
                    coordinates[i][0] = two_coords[0]
                    coordinates[i][1] = two_coords[1]
                    coordinates[i + 1][0] = two_coords[2]
                    coordinates[i + 1][1] = two_coords[3]
                    if i == len(coordinates) - 2:
                        self.tailCoords.append(str(coordinates[i + 1][0]) + '.' + str(coordinates[i + 1][1]))
                        # print("i {} coordinates {}".format(i, coordinates))
                        # print("tail coordinates {}".format(set(self.tailCoords)))
                    i += 1
                j += 1

    def determine_direction(self, head, tail, direction, withHead):
        # print("head {} tail {} direction {}".format(head, tail, direction))
        if withHead:
            return direction
        else:
            if head[0] == tail[0]:
                if head[1] == tail[1]:
                    return direction
                elif head[1] < tail[1]:
                    return 'D'
                elif head[1] > tail[1]:
                    return 'U'
            elif head[0] > tail[0]:
                if head[1] == tail[1]:
                    return 'R'
                elif head[1] < tail[1]:
                    return 'DR'
                elif head[1] > tail[1]:
                    return 'UR'
            elif head[0] < tail[0]:
                if head[1] == tail[1]:
                    return 'L'
                elif head[1] < tail[1]:
                    return 'DL'
                elif head[1] > tail[1]:
                    return 'UL'

    def update_coordinates(self, coordinates, direction, withHead):
        # print("direction {} coordinates {}".format(direction, coordinates))
        if direction == 'R':
            coordinates = self.right(coordinates, withHead)
        elif direction == 'L':
            coordinates = self.left(coordinates, withHead)
        elif direction == 'U':
            coordinates = self.up(coordinates, withHead)
        elif direction == 'D':
            coordinates = self.down(coordinates, withHead)
        elif direction == 'UL':
            coordinates = self.upleft(coordinates, withHead)
        elif direction == 'UR':
            coordinates = self.upright(coordinates, withHead)
        elif direction == 'DL':
            coordinates = self.downleft(coordinates, withHead)
        elif direction == 'DR':
            coordinates = self.downright(coordinates, withHead)
        return coordinates

    def right(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]

        relevant_distance = hx - tx
        if withHead or relevant_distance > 1:
            if hx > tx:
                tx = tx + 1
                if hy > ty:
                    ty = ty + 1
                elif hy < ty:
                    ty = ty - 1
        if withHead:
            hx = hx + 1
        # self.tailCoords.append(str(tx) + '.' + str(ty))
        return [hx, hy, tx, ty]

    def left(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        relevant_distance = hx - tx
        if withHead or relevant_distance < -1:
            if hx < tx:
                tx = tx - 1
                if hy > ty:
                    ty = ty + 1
                elif hy < ty:
                    ty = ty - 1
        if withHead:
            hx = hx - 1
        # self.tailCoords.append(str(tx) + '.' + str(ty))
        return [hx, hy, tx, ty]

    def up(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        relevant_distance = hy - ty
        if withHead or relevant_distance > 1:
            if hy > ty:
                ty = ty + 1
                if hx > tx:
                    tx = tx + 1
                elif hx < tx:
                    tx = tx - 1
        if withHead:
            hy = hy + 1
        # self.tailCoords.append(str(tx) + '.' + str(ty))
        return [hx, hy, tx, ty]

    def down(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        relevant_distance = hy - ty
        if withHead or relevant_distance < -1:
            if hy < ty:
                ty = ty - 1
                if hx > tx:
                    tx = tx + 1
                elif hx < tx:
                    tx = tx - 1
            if withHead:
                hy = hy - 1
        # self.tailCoords.append(str(tx) + '.' + str(ty))
        return [hx, hy, tx, ty]

    def upleft(self, coordinates, withHead):
        # 3, 4, 2, 2,
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        x_distance = hx - tx
        y_distance = hy - ty
        # print("x_distance {} y_distance {}".format(x_distance, y_distance))
        if withHead or x_distance < -1 or y_distance > 1:
            if hx < tx:
                if hy == ty:
                    tx = tx - 1
                elif hy > ty:
                    tx = tx - 1
                    ty = ty + 1
            elif hx == tx and hy > ty:
                # print("hx == tx and hy > ty hx, hy, tx, ty {} {} {} {}".format(hx, hy, tx, ty))
                ty = ty + 1
        if withHead:
            hy = hy + 1
            hx = hx - 1
        return [hx, hy, tx, ty]

    def upright(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        x_distance = hx - tx
        y_distance = hy - ty
        if withHead or x_distance > 1 or y_distance > 1:
            if hx > tx:
                if hy == ty:
                    tx = tx + 1
                elif hy > ty:
                    tx = tx + 1
                    ty = ty + 1
            elif hx == tx and hy > ty:
                ty = ty + 1
        if withHead:
            hy = hy + 1
            hx = hx + 1
        return [hx, hy, tx, ty]

    def downleft(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        # [0, 5, -2, 6]
        x_distance = hx - tx   # 2
        y_distance = hy - ty   # -1
        if withHead or x_distance < -1 or y_distance < -1:
            if hy < ty:
                if hx == tx:
                    ty = ty - 1
                elif hx < tx:
                    tx = tx - 1
                    ty = ty - 1
            elif hy == ty and hx < tx:
                tx = tx - 1
        if withHead:
            hy = hy - 1
            hx = hx -
        return [hx, hy, tx, ty]

    def downright(self, coordinates, withHead):
        hx = coordinates[0]
        hy = coordinates[1]
        tx = coordinates[2]
        ty = coordinates[3]
        # [0, 5, -2, 6]
        x_distance = hx - tx  # 2
        y_distance = hy - ty  # -1
        # print("hx, hy, tx, ty {} {} {} {}".format(hx, hy, tx, ty))
        if withHead or x_distance > 1 or y_distance < -1:
            if hy < ty:
                if hx == tx:
                    ty = ty - 1
                elif hx > tx:
                    # print("hx, hy, tx, ty {} {} {} {}".format(hx, hy, tx, ty))
                    tx = tx + 1
                    ty = ty - 1
            elif hy == ty and hx > tx:
                tx = tx + 1
        if withHead:
            hy = hy - 1
            hx = hx + 1
        return [hx, hy, tx, ty]

if __name__ == '__main__':
    day = DayNine()
    print("Day eight exercise!")
    day.do_split()
    day.split_rows()
    day.calculate3()
    day.say_state()

# tailCoords {'0.0', '3.0', '4.0', '-1.0', '1.0'}
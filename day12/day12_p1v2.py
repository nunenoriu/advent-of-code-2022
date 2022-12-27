# Description:
# heightmap shows the local area from above broken into grid;
# elevation is given in letter, a is smallest z is largest
# S starting position
# E location where signal is best
# S has elevation a, E has elevation z
# get the shortest path
# elevation of current square can be at most one higher than el of current square
# if m you can step to n but not o
#
from collections import deque
from heapq import heappop, heappush

class DayTwelve:
    def __init__(self):
        self.data = []
        with open("puzzleInput.txt", 'r') as f:
            self.data = f.read()

        self.dataSplit = []
        self.rowSplit = []
        self.start = ''
        self.destination = ''
        self.start_nodes = []

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def split_rows(self):
        length = 0
        for index, row in enumerate(self.dataSplit):
            self.rowSplit.append(list(row))
            length += len(row)
            self.nodes = row
        print('range(length) {}'.format(range(length)))

    def can_move(self, start, destination):
        # print('start {} destination {}'.format(start, destination))
        if start == 'S':
            start = 'a'
        if start == 'E':
            start = 'z'
        if destination == 'S':
            start = 'a'
        if destination == 'E':
            destination = 'z'
        boolean = ord(destination) - ord(start)
        return boolean <= 1

    def generate_nodes(self):
        nodes = []
        for row_index, row in enumerate(self.rowSplit):
            for column_index, column in enumerate(row):
                current_node_name = self.generate_node_name(row_index, column_index)
                nodes.append(current_node_name)
        # print(nodes)
        return nodes

    def generate_graph(self):
        nodes = self.generate_nodes()
        graph = {node: [] for node in nodes}

        for row_index, row in enumerate(self.rowSplit):
            for column_index, column in enumerate(row):
                current_node_name = self.generate_node_name(row_index, column_index)
                self.update_start_and_goal(column, current_node_name)
                # check node below
                if row_index < len(self.rowSplit) - 1:
                    bottom = self.generate_node_name(row_index + 1, column_index)
                    row_below = self.rowSplit[row_index + 1]
                    if self.can_move(column, row_below[column_index]):
                        graph[current_node_name].append(bottom)

                if column_index < len(row) - 1:
                    right = self.generate_node_name(row_index, column_index + 1)
                    if self.can_move(column, row[column_index + 1]):
                        graph[current_node_name].append(right)
                if row_index > 0:
                    top = self.generate_node_name(row_index - 1, column_index)
                    row_above = self.rowSplit[row_index - 1]
                    if self.can_move(column, row_above[column_index]):
                        graph[current_node_name].append(top)
                if column_index > 0:
                    left = self.generate_node_name(row_index, column_index - 1)
                    if self.can_move(column, row[column_index - 1]):
                        graph[current_node_name].append(left)
        converted_dict = {}

        for key, values in graph.items():
            converted_values = [(value, 1) for value in values]
            converted_dict[key] = converted_values
        print('start {} destination {}'.format(self.start, self.destination))
        print(len(graph))
        result = self.dijkstra(converted_dict, self.start, self.destination)
        print(result)

    def update_start_and_goal(self, value, name):
        if value == 'S':
            self.start = name
        elif value == 'E':
            self.destination = name

    def generate_node_name(self, row_index, column_index):
        return 'r' + str(row_index) + 'c' + str(column_index)

    def get_current_letter(self, node):
        node_parts = node.split('c')
        row_parts = node_parts[0].split('r')
        # print('node_parts {} row_parts {}'.format(node_parts, row_parts))
        letter = self.rowSplit[int(row_parts[1])][int(node_parts[1])]
        return letter
        # print(letter)

    def dijkstra(self, graph, start, end):
        print('start {} end {} '.format(graph[start], graph[end]))
        # Create a dictionary to store the distances from the start node to all other nodes
        distances = {}

        # Initialize all distances to infinity
        for node in graph:
            distances[node] = float('inf')

        # Set the distance from the start node to itself to be 0
        distances[start] = 0

        # Create a set to store the nodes that have been visited
        visited = set()
        visited_letters = set()
        highest_letter = 'a'
        shortest_distance = float('inf')

        # Create a priority queue to store the nodes that need to be visited
        # We will use the distances as the priority in the priority queue
        queue = []
        heappush(queue, [distances[start], start])

        # Loop until the priority queue is empty
        while queue:

            # Pop the node with the smallest distance from the queue
            current_distance, current_node = heappop(queue)
            if current_node in visited:
                continue
            letter = self.get_current_letter(current_node)
            visited_letters.add(letter)
            if letter == highest_letter and current_distance < shortest_distance:
                shortest_distance = current_distance
            elif ord(letter) > ord(highest_letter):
                highest_letter = letter
                shortest_distance = current_distance

            # Mark the current node as visited
            visited.add(current_node)

            # If the current node is the end node, return the distance
            if current_node == end:
                return current_distance

            for neighbor, weight in graph[current_node]:
                # Calculate the distance from the start node to the neighbor
                distance = current_distance + weight

                # If the distance from the start node to the neighbor is smaller than the current distance, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

                    # Push the neighbor to the priority queue
                    heappush(queue, [distance, neighbor])
        print(visited, len(visited))
        print(len(visited_letters), visited_letters)
        print(shortest_distance, highest_letter)


if __name__ == '__main__':
    print('Day Twelve!')
    day = DayTwelve()
    day.do_split()
    day.split_rows()
    # day.get_indices()
    day.say_state()
    day.generate_graph()

#410 too low

class DayOne:
    def __init__(self, data):
        self.calories_data = data

    def get_largest_number(self):
        largest_number = 0
        all_numbers = []

        for item in self.calories_data:
            total = sum(item)
            all_numbers.append(total)

            if total > largest_number:
                largest_number = total

        return largest_number, all_numbers

if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    day_one = DayOne(data)
    largest_number, all_numbers = day_one.get_largest_number()
    print("Largest number:", largest_number)
    print("All numbers:", all_numbers)

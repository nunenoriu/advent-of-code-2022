class DayTwo:
    def __init__(self, data):
        self.data = data

    def get_score(self):
        total = 0
        for pair in self.data:
            total += self.get_pair_score(pair)
        print("Total:", total)

    def get_pair_score(self, pair):
        scores = {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7,
        }
        return scores[pair]

if __name__ == '__main__':
    data = ["A X", "A Y", "A Z", "B X", "B Y", "B Z", "C X", "C Y", "C Z"]
    day_two = DayTwo(data)
    day_two.get_score()

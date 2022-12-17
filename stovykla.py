# Reikalavimai:
# Rask isrinktus krepsininkus
# Maziausiai naudinga zaideja
# Naudingiausia zaideja
class Stovykla:
    def __init__(self):
        text_file = open("./inputs/krepsininkai.txt", 'r')
        self.data = text_file.read()
        self.dataSplit = []
        text_file.close()

    def do_split(self):
        self.dataSplit = self.data.split("\n")

    def isrink_su_min_balu(self, m):
        atrinkti = []
        for x in self.dataSplit:
            dalys = x.split()
            if float(dalys[1]) >= float(m):
                atrinkti.append(x)
        print("Atrinkti {}".format(atrinkti))

    def isrink_su_maziausiu_balu(self):
        atrinktas = self.dataSplit[0]
        balas = None
        for x in self.dataSplit:
            dalys = x.split()
            if balas is None or float(dalys[1]) <= balas:
                atrinktas = x
                balas = float(dalys[1])
        print("Atrinktas su maziausiu balu {}".format(atrinktas))

    def isrink_su_didziausiu_balu(self):
        atrinktas = self.dataSplit[0]
        balas = None
        for x in self.dataSplit:
            dalys = x.split()
            if balas is None or float(dalys[1]) > balas:
                atrinktas = x
                balas = float(dalys[1])
        print("Atrinktas su didziausiu balu {}".format(atrinktas))

if __name__ == '__main__':
    stovykla = Stovykla()
    stovykla.do_split()
    stovykla.isrink_su_maziausiu_balu()
    stovykla.isrink_su_didziausiu_balu()
    while True:
        action = input("Koks maziausias balas atrinktu zaideju? ")
        stovykla.isrink_su_min_balu(action)

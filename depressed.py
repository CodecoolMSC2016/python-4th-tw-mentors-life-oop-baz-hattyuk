from mentor import Mentor

class DepressedMentor(Mentor):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, low_tolerance_limit):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.low_tolerance_limit = low_tolerance_limit

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def how_many_questions(cls):
        pass






    def becomes_alcoholist(self):
        pass



atesz = Mentor("Attila", "Molnár", 1989, "Male", "Atesz")

atesz = DepressedMentor(atesz.first_name, atesz.last_name, atesz.year_of_birth, atesz.gender, atesz.nickname, 10)

print(atesz.fullname)


from mentor import Mentor

class EasyGoingMentor(Mentor):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, happiness):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.happiness = happiness

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name


    def calculate_mood(self):
        pass

peba = Mentor("Balázs", "Pekár", 1990, "Male", "Peba")

peba = EasyGoingMentor(peba.first_name, peba.last_name, peba.year_of_birth, peba.gender, peba.nickname, 10)
print(peba.fullname)


# question: fullname máshogy?

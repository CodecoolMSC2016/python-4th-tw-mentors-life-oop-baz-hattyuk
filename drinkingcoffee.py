from mentor import Mentor
from random import randint


class Coffeedrinkers(Mentor):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.energy_level = energy_level

    @staticmethod
    def coffee_needed():
        coffee_needed_permentors = []
        mentors_list = Mentor.create_by_csv()
        mentor_dict = {}
        for mentor in mentors_list:
            mentor.energy_level = randint(0,99)
            one_cup_coffee = 10
            needed = (100-mentor.energy_level) // 10
            name = "{} {}".format(mentor.first_name, mentor.last_name)
            mentor_dict[name] = needed
        return mentor_dict


lista = Coffeedrinkers.coffee_needed()
print(lista)
print(lista["Attila Molnár"])

from mentor import Mentor
from random import randint


class Coffeedrinkers(Mentor):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.energy_level = energy_level

    @staticmethod
    def coffee_needed():
        mentors_list = Mentor.create_by_csv()
        mentor_dict = {}
        for mentor in mentors_list:
            mentor.energy_level = randint(0,10)
            one_cup_coffee = 2
            needed = (10-mentor.energy_level) // one_cup_coffee
            name = "{} {}".format(mentor.first_name, mentor.last_name)
            if needed != 0:
                mentor_dict[name] = needed
            #coffee_drinker_object = []
            #objectum = Coffeedrinkers(mentor.first_name, mentor.last_name, mentor.year_of_birth, mentor.gender, mentor.nickname, mentor.energy_level)
            #coffee_driker_object.append(objectum)
        return mentor_dict


print(Coffeedrinkers.coffee_needed())

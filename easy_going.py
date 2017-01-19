from mentor import Mentor
from random import randint


class EasyGoingMentor(Mentor):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, happiness):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.happiness = happiness

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name


    @staticmethod
    def create_object():
        mentors_list = Mentor.create_by_csv()
        mentor_object_list = []
        for mentor in mentors_list:
            mentor.happiness = randint(5,10)
            objectum = EasyGoingMentor(mentor.first_name, mentor.last_name, mentor.year_of_birth, mentor.gender, mentor.nickname, mentor.happiness)
            mentor_object_list.append(objectum)
        return mentor_object_list



peba = Mentor("Balázs", "Pekár", 1990, "Male", "Peba")
atesz = Mentor("Attila", "Molnár", 1989, "Male", "Atesz")
imi = Mentor("Imre", "Lindi", 1990, "Male", "Imi")
szodi = Mentor("Sándor", "Szodoray", 1981, "Male", "Szodi")
robi = Mentor("Róbert", "Kohányi", 1985, "Male", "Robi")
pako = Mentor("Pál", "Monoczki", 1983, "Male", "Pakko")

peba = EasyGoingMentor(peba.first_name, peba.last_name, peba.year_of_birth, peba.gender, peba.nickname, 10)
atesz = EasyGoingMentor(atesz.first_name, atesz.last_name, atesz.year_of_birth, atesz.gender, atesz.nickname, 1)
imi = EasyGoingMentor(imi.first_name, imi.last_name, imi.year_of_birth, imi.gender, imi.nickname, 5)
szodi = EasyGoingMentor(szodi.first_name, szodi.last_name, szodi.year_of_birth, szodi.gender, szodi.nickname, 6)
robi = EasyGoingMentor(robi.first_name, robi.last_name, robi.year_of_birth, robi.gender, robi.nickname, 8)
pako = EasyGoingMentor(pako.first_name, pako.last_name, pako.year_of_birth, pako.gender, pako.nickname, 7)


#print(EasyGoingMentor.create_object()[0].happiness)

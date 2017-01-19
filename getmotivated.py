from mentor import Mentor
import csv

class Mentor_how_motivable(Mentor):

    def __init__(self, imi_mot_skill, atesz_mot_skill, peba_mot_skill, szodi_mot_skill, robi_mot_skill, pako_mot_skill):
        self.imi_mot_skill = imi_mot_skill
        self.atesz_mot_skill = atesz_mot_skill
        self.peba_mot_skill = peba_mot_skill
        self.szodi_mot_skill = szodi_mot_skill
        self.robi_mot_skill = robi_mot_skill
        self.pakko_mot_skill = pakko_mot_skill


    def get_nickname():
        mentor_nicknames = []
        with open("data/mentors.csv") as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                mentor_nicknames.append(row[4])
        return mentor_nicknames


    def how_motivable_are_mentors(nickname, imi_mot_skill, atesz_mot_skill, peba_mot_skill, szodi_mot_skill, robi_mot_skill, pako_mot_skill):
        how_motivable = []
        for name in nickname:
            if name == "Imi":
                how_motivable.append(name + "'s motivation skill is: " + str(imi_mot_skill))
            elif name == "Atesz":
                how_motivable.append(name + "'s motivation skill is: " + str(atesz_mot_skill))
            elif name == "Peba":
                how_motivable.append(name + "'s motivation skill is: " + str(peba_mot_skill))
            elif name == "Szodi":
                how_motivable.append(name + "'s motivation skill is: " + str(szodi_mot_skill))
            elif name == "Robi":
                how_motivable.append(name + "'s motivation skill is: " + str(robi_mot_skill))
            elif name == "Pako":
                how_motivable.append(name + "'s motivation skill is: " + str(pako_mot_skill))
            else:
                how_motivable.append("Unknown mentor added to list")
        return "\n".join(how_motivable)
        




Mentor_how_motivable.get_nickname()
mentor_nicknames = Mentor_how_motivable.get_nickname()
mentormot = Mentor_how_motivable.how_motivable_are_mentors(mentor_nicknames, 5, 10, 7, 6, 8, 6)
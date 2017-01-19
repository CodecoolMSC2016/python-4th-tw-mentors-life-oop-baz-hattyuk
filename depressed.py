from mentor import Mentor
import random

class DepressedMentor(Mentor):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, low_tolerance_limit):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.low_tolerance_limit = low_tolerance_limit

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    @staticmethod
    def is_depressed():
        depressed_mentors = []
        mentors_list = Mentor.create_by_csv()
        for mentor in mentors_list:
            if mentor.nickname != "Atesz":
                mentor.low_tolerance_limit = random.randint(0, 20)
            else:
                mentor.low_tolerance_limit = random.randint(0, 20)
            if mentor.low_tolerance_limit < 14:
                depressed_m = DepressedMentor(mentor.first_name, mentor.last_name, mentor.year_of_birth, mentor.gender, mentor.nickname, mentor.low_tolerance_limit)
                depressed_mentors.append(depressed_m)
        return depressed_mentors

    @staticmethod
    def how_many_questions():

        question_list = ["De hogy jönnek ide a díszlettervezők?",
                        "Mi??? Nem figyeltem. Akkor most mi van vagy mi?",
                        "A zártosztály is lehet osztály, ugye?",
                        "Az appenddel nyitom meg a fájlt, ugye? :O",
                        "Én néha azt sem tudom, hogy ki kihez beszél...Az most baj?"]

        exampl = question_list[random.randint(0, len(question_list)-1)]
        questions = random.randint(0, 100)
        if questions < 10:
            new_questions = random.randint(9, 100)
            amount_of_questions = questions + new_questions
            if amount_of_questions < 10:
                return "Ma megúszták!"
            else:
                print(DepressedMentor.is_depressed()[0].nickname + " gets: " + str(amount_of_questions) + " question in this day. Like this:\n-" + exampl + "\nIt was too much for him!")
                return amount_of_questions
        else:
            print(DepressedMentor.is_depressed()[0].nickname + " gets: " + str(questions) + " question in this day. Like this:\n-" + exampl + "\nIt was too much for him!")
        return questions

    @staticmethod
    def becomes_alcoholist():
        amount_of_alcohol = DepressedMentor.is_depressed()[0].low_tolerance_limit+2
        if DepressedMentor.how_many_questions() > DepressedMentor.is_depressed()[0].low_tolerance_limit:
            x = amount_of_alcohol + DepressedMentor.is_depressed()[0].low_tolerance_limit
            print("\nHe started to drink wine:", x, "botle/day", "and takes some xanax:", DepressedMentor.is_depressed()[0].low_tolerance_limit, "pill/day.")
            return "\nSo the management decided: He have to leave the codecool, as soon as it is possible!!!"
        return("\nHe almost becomes alcoholist.\nBut the management decided he have to leave the codecool! :()")


print(DepressedMentor.becomes_alcoholist())

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
            mentor.low_tolerance_limit = random.randint(0, 20)
            if mentor.low_tolerance_limit < 9:
                depressed_m = DepressedMentor(mentor.first_name, mentor.last_name, mentor.year_of_birth, mentor.gender, mentor.nickname, mentor.low_tolerance_limit)
                depressed_mentors.append(depressed_m)
        return depressed_mentors

    @staticmethod
    def how_many_questions():

        question_list = ["De hogy jönnek ide a díszlettervezők?",
                        "Mi??? Nem figyeltem. Akkor most mi van? Mi?",
                        "A zártosztály is lehet osztály, ugye?",
                        "Az appenddel nyitom meg a fájlt, ugye? :O",
                        "Én néha azt sem tudom, hogy ki kihez beszél...Az most baj?"]

        exampl = question_list[random.randint(0, len(question_list)-1)]
        questions = random.randint(0, 100)
        if questions < 10:
            new_questions = random.randint(9, 100)
            amount_of_questions = questions + new_questions
            if amount_of_questions < 10:
                return "Ma megúszta!"
            else:
                print("\n" + atesz.fullname + " gets: " + str(amount_of_questions) + " question in this day. Like this:\n-" + exampl + "\nIt was too much for him!")
                return amount_of_questions
        else:
            print("\n" + atesz.fullname + " gets: " + str(questions) + " question in this day. Like this:\n-" + exampl + "\nIt was too much for him!")
            return questions

    @staticmethod
    def becomes_alcoholist(low_tolerance_limit):
        amount_of_alcohol = round(low_tolerance_limit/2)
        if atesz.how_many_questions() > low_tolerance_limit:
            print("\nAtesz tolerance limit is maximum:", atesz.low_tolerance_limit, "questions.")
            x = amount_of_alcohol + atesz.low_tolerance_limit
            print("He started to wine:", x, "botle of beer/day", "and takes some xanax:", low_tolerance_limit, "pill/day.")
            return "\nSo the management decided: He have to leave the codecool, as soon as it is possible!!!"
        return("\nHe almost becomes alcoholist.\nBut the management decided he have to leave the codecool! :()")

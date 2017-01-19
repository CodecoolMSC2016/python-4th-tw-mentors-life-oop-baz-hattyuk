from mentor import Mentor
import random

class DepressedMentor(Mentor):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, low_tolerance_limit):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname)
        self.low_tolerance_limit = low_tolerance_limit

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    def is_depressed(self):
        in_the_class = ""
        not_in_this_class = []
        not_in_this_class.append("They are not in the depressed mentor class:")
        mentors_list = Mentor.create_by_csv()
        for mentor in mentors_list:
            if mentor.nickname != "Atesz":
                not_in_this_class.append(mentor.nickname)
            else:
                in_the_class += mentor.nickname
                in_the_class += " is in the depressed mentor class!"
        print(not_in_this_class)
        return "{} is in the depressed mentor class.".format(atesz.nickname)

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




atesz = DepressedMentor("Attila", "Molnár", 1989, "Male", "Atesz", random.randint(0, 20))
print(atesz.is_depressed())
#print("Type of Atesz:", type(atesz))
##print(atesz.how_many_questions())
#print(atesz.becomes_alcoholist(random.randint(0, 20)))

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
            if mentor.low_tolerance_limit < 10:
                depressed_m = DepressedMentor(mentor.first_name, mentor.last_name, mentor.year_of_birth, mentor.gender, mentor.nickname, mentor.low_tolerance_limit)
                depressed_mentors.append(depressed_m)
        return depressed_mentors

    @staticmethod
    def how_many_questions(depressed_mentor_list):
        result = []
        question_list = ["De hogy jönnek ide a díszlettervezők?",
                        "Mi??? Nem figyeltem. Akkor most mi van vagy mi?",
                        "A zártosztály is lehet osztály, ugye?",
                        "Az appenddel nyitom meg a fájlt, ugye? :O",
                        "Én néha azt sem tudom, hogy ki kihez beszél...Az most baj?"]

        for mentor in depressed_mentor_list:
            random_question = question_list[random.randint(0,4)]
            questions = random.randint(5, 100)
            result_elements = []
            result_elements.append(mentor.nickname)
            result_elements.append(questions)
            result_elements.append(random_question)
            result.append(result_elements)
        return result


    @staticmethod
    def becomes_alcoholist(spec_depressed_mentor_list):
        result = []
        for mentor in spec_depressed_mentor_list:
            result_elements = []
            result_elements.append(mentor.nickname)
            if mentor.low_tolerance_limit < 7:
                result_elements.append(True)
            else:
                result_elements.append(False)
            result.append(result_elements)
        return result

#print(DepressedMentor.how_many_questions(DepressedMentor.is_depressed()))
#print(DepressedMentor.becomes_alcoholist(DepressedMentor.is_depressed()))

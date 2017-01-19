from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        return CodecoolClass("Miskolc", 2016, Mentor.create_by_csv(), Student.create_by_csv())

    @staticmethod
    def find_mentor_by_full_name(full_name):
        name = full_name.split()
        first_name = name[0]
        last_name = name[1]

        mentors_list = Mentor.create_by_csv()

        is_in = False

        for mentor in mentors_list:
            if mentor.first_name == first_name and mentor.last_name == last_name:
                is_in = True

        if is_in == True:
            print ("{} {} was found in mentors".format(first_name, last_name))
        else:
            print ("{} {} was not found in mentors".format(first_name, last_name))

    @staticmethod
    def find_student_by_full_name(full_name):
        name = full_name.split()
        first_name = name[0]
        last_name = name[1]

        students_list = Student.create_by_csv()

        is_in = False

        for student in students_list:
            if student.first_name == first_name and student.last_name == last_name:
                is_in = True

        if is_in == True:
            print ("{} {} was found in students".format(first_name, last_name))
        else:
            print ("{} {} was not found in students".format(first_name, last_name))

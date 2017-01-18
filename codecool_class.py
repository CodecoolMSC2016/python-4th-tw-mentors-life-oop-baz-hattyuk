from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.location = location
        self.year = year
        self.mentors = []
        self.students = []

    def generate_local():
        all_class = []
        mentors_list = Mentor.create_by_csv()
        students_list = Student.create_by_csv()
        for item in mentors_list:
            cc = CodecoolClass()
            cc.first_name = mentors_list[0]
            all_class.append(cc)
        return all_class

print(CodecoolClass.generate_local()[0].first_name)

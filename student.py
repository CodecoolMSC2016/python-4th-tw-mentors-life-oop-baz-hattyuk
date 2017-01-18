from person import Person
import csv


class Student(Person):

    def __init__(self, first_name="", last_name="", year_of_birth="", gender="", knowledge_level=0, energy_level=0):
        super().__init__()
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    @classmethod
    def create_by_csv(cls):
        student_list = []
        with open("data/students.csv") as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                one_student = Student()
                one_student.first_name = row[0]
                one_student.last_name = row[1]
                one_student.year_of_birth = row[2]
                one_student.gender = row[3]
                one_student.knowledge_level = int(row[4])
                one_student.energy_level = int(row[5])
                student_list.append(one_student)
            return student_list


student1 = Student.create_by_csv()

print(student1[0].first_name, student1[0].last_name, student1[0].year_of_birth)

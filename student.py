from person import Person
import csv


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    @classmethod
    def create_by_csv(cls, csv_file = "data/students.csv"):
        student_list = []
        with open(csv_file, "r") as myfile:
            for line in myfile.readlines():
                line = line.strip("\n")
                line = line.split(", ")
                one_student = Student()
                one_student.first_name = line[0]
                one_student.last_name = line[1]
                one_student.year_of_birth = line[2]
                one_student.gender = line[3]
                one_student.knowledge_level = int(line[4])
                one_student.energy_level = int(line[5])
                students.append(one_student)
        return student_list

print(Student.create_by_csv)

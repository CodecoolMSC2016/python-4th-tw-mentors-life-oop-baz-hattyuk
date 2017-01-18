from person import Person
import csv


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = knowledge_level
        self.energy_level = energy_level

    @classmethod
    def create_by_csv(cls):
        student_list = []
        with open("data/students.csv") as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                one_student = cls(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]))
                student_list.append(one_student)
                for word in row:
                    if word == " ":
                        raise ValueError("Missing data from students.csv!")
            return student_list

stud = Student.create_by_csv()
print(stud[0].first_name, stud[0].last_name)

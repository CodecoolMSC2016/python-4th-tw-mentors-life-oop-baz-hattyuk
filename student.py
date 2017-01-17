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
            for line in myfile:
                line = line.split(", ")
                #print(line[0] + " valami")=f.name

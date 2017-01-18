from person import Person
import csv


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls):
        with open('data/mentors.csv') as csvfile:
            mentors_list = []
            data = csv.reader(csvfile)
            for row in data:
                person = cls(row[0], row[1], row[2], row[3], row[4])
                try:
                    person.nickname = row[4]
                except IndexError:
                    print("No nickname found!!, for: {} {}".format(person.first_name, person.last_name))
                    exit()
                mentors_list.append(person)
        return mentors_list


mentor1 = Mentor.create_by_csv()
print(mentor1[0].first_name, mentor1[0].last_name)

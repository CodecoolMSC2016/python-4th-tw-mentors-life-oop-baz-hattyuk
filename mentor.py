from person import Person
import csv


class Mentor(Person):

    def _init__(self, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls):
        with open('data/mentors.csv') as csvfile:
            mentors_list = []
            data = csv.reader(csvfile)
            for row in data:
                person = Mentor()
                person.first_name = row[0]
                person.last_name = row[1]
                person.year_of_birth = row[2]
                person.gender = row[3]
                try:
                    person.nickname = row[4]
                except IndexError:
                    print("No nickname found!!, for: {} {}".format(person.first_name, person.last_name))
                    exit()
                mentors_list.append(person)
        return mentors_list



mentor1 = Mentor.create_by_csv()

print(mentor1[0].first_name, mentor1[0].last_name)

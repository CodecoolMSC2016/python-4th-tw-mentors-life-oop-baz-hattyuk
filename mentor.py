from person import Person


class Mentor(Person):


    def _init__(self, first_name, last_name, year_of_birth, gender, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, filename):
        with

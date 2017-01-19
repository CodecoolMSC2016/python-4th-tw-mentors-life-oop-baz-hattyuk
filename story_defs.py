from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from depressed import DepressedMentor
from easy_going import EasyGoingMentor


def choosing_menu():
    choosing_list = []
    mentor_list = Mentor.create_by_csv()
    counter = 1
    for mentor in mentor_list:
        name = "{}. {} {}".format(counter, mentor.first_name, mentor.last_name)
        choosing_list.append(name)
        counter +=1
    print("\n".join(choosing_list))

def choosed():
    choosen = int(input("Choose a mentor, who's day you want to have a sneak peak!  "))
    mentor_list = Mentor.create_by_csv()
    return (mentor_list[choosen-1].first_name, mentor_list[choosen-1].last_name)


def story1():
    print("\n Soo {} goes to Codecool in the weekdays.".format(choosed))

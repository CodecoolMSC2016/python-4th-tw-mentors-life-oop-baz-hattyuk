from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from drinkingcoffee import Coffeedrinkers
from depressed import DepressedMentor
from easy_going import EasyGoingMentor
import time
import os

def choosing_menu():
    choosing_list = []
    mentor_list = Mentor.create_by_csv()
    counter = 1
    for mentor in mentor_list:
        name = "{}. {} {}".format(counter, mentor.first_name, mentor.last_name)
        choosing_list.append(name)
        counter +=1
    print("\n".join(choosing_list))


def choosed(choosen):
    result = []
    mentor_list = Mentor.create_by_csv()
    result.append(mentor_list[choosen-1].first_name)
    result.append(" ")
    result.append(mentor_list[choosen-1].last_name)
    return "".join(result)

def choosed_nickname(choosen):
    mentor_list = Mentor.create_by_csv()
    choosed_mentor_nickname = mentor_list[choosen-1].nickname
    return choosed_mentor_nickname

def get_energy(choosen):
    name = choosed(choosen)
    name = str(name)
    coffe_dict = Coffeedrinkers.coffee_needed()
    return coffe_dict[name]

def story1(choosen):
    how_many_coffee = get_energy(choosen)
    print("\n Soo {} goes to Codecool in the weekdays.".format(choosed(choosen)))
    print("In each day, every mentor has a specific enery level. Today, {}'s energy isn't 100%,"
          "so he needs to drink {} cups of coffee.".format(choosed_nickname(choosen), how_many_coffee))
    time.sleep(6)
    os.system('clear')
    print("""\
                    (  )   (   )  )
                     ) (   )  (  (
                     ( )  (    ) )
                     _____________
                    <_____________> ___
                    |             |/ _ "\"
                    |               | | |
                    |               |_| |
                 ___|             |\___/
                /    \___________/    "\"
                \_____________________/

                    """)
    for count_down in range(how_many_coffee, 0, -1):
        print(count_down)
        time.sleep(0.5)
    os.system('clear')

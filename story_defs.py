from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from drinkingcoffee import Coffeedrinkers
from getmotivated import Mentor_how_motivable
from depressed import DepressedMentor
from easy_going import EasyGoingMentor
import time
import os
from random import randint

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
    if name in coffe_dict:
        return coffe_dict[name]
    else:
        return 0

def story1(choosen):
    how_many_coffee = get_energy(choosen)
    if how_many_coffee == 0:
        print("This mentor is not drinking coffee this day!")
        time.sleep(2)
        os.system('clear')
    else:
        print("\nSoo {} goes to Codecool in the weekdays.".format(choosed(choosen)))
        print("In each day, every mentor has a specific enery level. Today, {}'s energy isn't 100%,"
              "so he needs to drink {} cup(s) of coffee.".format(choosed_nickname(choosen), how_many_coffee))
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
            time.sleep(1)
        os.system('clear')

def story2(choosen):
    print("After having/not having coffee, {} has to make motivation speech.".format(choosed_nickname(choosen)))
    Mentor_how_motivable.get_nickname()
    mentor_nicknames = Mentor_how_motivable.get_nickname()
    mentormot = Mentor_how_motivable.how_motivable_are_mentors(mentor_nicknames, 6, 3, 7, 6, 8, 6)
    if int(mentormot[choosen-1][::-1][0]) >= 6:
        print("\n{} can motive students, so codecoolers are happy today, and they don't lose energy.".format(choosed_nickname(choosen)))
        time.sleep(3)
    else:
        print("\n{} can't motive students well, so codecoolers got tired of the day.".format(choosed_nickname(choosen)))
        print("\nCause of the bad motivation, students lose energy, so now the studens has: \n")
        students_energy_level = Student.create_by_csv()
        students_by_energy = []
        for student in students_energy_level:
            energy_levels = []
            energy_levels.append(student.first_name)
            energy_levels.append(student.last_name)
            energy_levels.append(str(student.energy_level))
            energy_levels.append("--->")
            energy_levels.append(str(student.energy_level - randint(1, 5)))
            students_by_energy.append(energy_levels)
        for student in students_by_energy:
            print(" ".join(student))
        time.sleep(9)
        os.system('clear')

def story3(choosen):
    todays_questions = DepressedMentor.how_many_questions(DepressedMentor.is_depressed())
    print("During the day, {} got many questions, from coodecoolers. ".format(choosed_nickname(choosen)))
    for mentor in range(len(todays_questions)):
        if todays_questions[mentor][0] == choosed_nickname(choosen):
            print("\nTo be accurate, codecoolers asked {} questions, like: {}".format(todays_questions[mentor][1], todays_questions[mentor][2]))
            if todays_questions[mentor][1] > 70:
                print("\n{} thinks, that this is too much for him for a day.".format(choosed_nickname(choosen)))
            else:
                print("\n{} think, that he can still tolerate this.".format(choosed_nickname(choosen)))
            time.sleep(3)


    depressed_mentor = DepressedMentor.becomes_alcoholist(DepressedMentor.is_depressed())
    get_alcoholist = "good"
    for mentor_index in range(len(depressed_mentor)):
        if depressed_mentor[mentor_index][0] == choosed_nickname(choosen):
            get_alcoholist = "bad"
    print("\nUsually at the end of the day, mentors can feel good(happy) or bad(depressed). Depended on this day, {} feels {}.".format(choosed_nickname(choosen), get_alcoholist))
    time.sleep(3)


    if get_alcoholist == "bad":
        print("\nBecause of this feel, he started to drink wine: {} bottles/day, and takes some xanax: {} pill/day.".format(randint(1,5), randint(1,5)))
        print("\nSuch a sad story, but the management thought, he need to leave codecool!! BYE BYE")
    if get_alcoholist == "good":
        mentor_happiness = EasyGoingMentor.create_object()[choosen-1].happiness
        print("\nThis day was good for {}, so he has calender, where he always write's how happy is he at the end of the day, he wrote {}.".format(choosed_nickname(choosen), mentor_happiness))

def search_in_class(answer):
    if answer == "y" or answer == "Y":
        answer_class = input("Do you wanna search a student or mentor?")
        if answer_class == "mentor":
            name = input("Give a name, what you want to search: ")
            CodecoolClass.find_mentor_by_full_name(name)
        if answer_class == "student":
            name = input("Give a name, what you want to search: ")
            CodecoolClass.find_student_by_full_name(name)
    else:
        pass

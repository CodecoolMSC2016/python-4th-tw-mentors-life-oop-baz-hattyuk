from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from drinkingcoffee import Coffeedrinkers
from getmotivated import Mentor_how_motivable
from depressed import DepressedMentor
from easy_going import EasyGoingMentor
from story_defs import *
import os
import time
from random import randint


codecool_msc = CodecoolClass.generate_local()


def main():
    answer = input("Do you wanna search for mentor or student? If yes press y: ")
    while answer == "y" or answer == "Y":
        search_in_class(answer)
        answer = input("Do you wanna search again? If yes press y: ")
    os.system('clear')
    choosing_menu()
    choosen = int(input("Choose a mentor, who's day you want to have a sneak peak!  "))
    choosed(choosen)
    choosed_nickname(choosen)
    story1(choosen)
    story2(choosen)
    story3(choosen)


if __name__ == "__main__":
    main()

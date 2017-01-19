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
    choosing_menu()
    choosen = int(input("Choose a mentor, who's day you want to have a sneak peak!  "))
    choosed(choosen)
    choosed_nickname(choosen)
    story1(choosen)
    story2(choosen)

main()

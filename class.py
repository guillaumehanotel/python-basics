#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from pprint import pprint
import random
import sys
import os


class Animal(object):
    # double underscore = private
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    # constructeur
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name, self.__height, self.__weight,
                                                                     self.__sound)


cat = Animal("Whiskers", 33, 10, "Moew")
print(cat.toString())


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        super(Dog, self).__init__(name, height, weight, sound)
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.get_name(),
                                                                                     self.get_height(),
                                                                                     self.get_weight(),
                                                                                     self.get_sound(),
                                                                                     self.__owner)
    # Paramètres facultatifs
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Derek")
print(spot.toString())

spot.multiple_sounds()



# Polymorphisme
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

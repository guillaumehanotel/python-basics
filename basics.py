#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from pprint import pprint
# from __future__ import print_function
import random
import sys
import os



def ex6_1():
    tab = []
    for i in range(0, 7):
        tab.append(i)
    pprint(tab)


def ex6_2():
    tab = ['a', 'e', 'i', 'o', 'u', 'y']
    pprint(tab)


def ex6_3():
    notes = []
    for i in range(0, 10):
        note = input("Entrez une note entre 0 et 20 : ")
        if note > 20 or note < 0:
            print("Entre 0 et 20 !")
        else:
            notes.append(note)

    somme = sum(notes)
    print(somme / len(notes))


# ex6_1()
# ex6_2()
# ex6_3()


'''
+ - * / % 
** Exponentielle
// Résultat division entière
'''

name = "Foo"
number = 15

print("{1}{0}".format(name, number))


# ----------------------------
# Tableau

def list():
    arr = []
    for i in range(1, 11):
        arr.append(i)

    print(arr[3:7])

    other_list = ['Foo', 'Bar']

    # Nouveau tableau avec 2 tableau
    fusion = [arr, other_list]

    # Fusion des tableaux
    arr2 = arr + other_list

    pprint(arr2)

    # accéder à un élément d'un tableau à 2 dim
    print(fusion[1][1])

    # ajouter un élément
    fusion[1].append("lol")

    # ajouter à un certain index
    arr2.insert(2, "Test")

    # trier
    arr2.sort()

    # inverser
    arr2.reverse()

    # Supprimer par une valeur
    arr2.remove("Foo")

    # Supprimer par un index
    del arr2[5]

    # num elem
    print(len(arr2))

    # max elem
    print(max(arr))

    # min elem
    print(min(arr))

    pprint(arr2)

    # parcourt de liste

    # FOR (EACH)
    for elem in arr2:
        print(elem)

    # WHILE
    i = 0
    while i < len(arr2):
        print(elem)
        i += 1

    # ENUMERATE
    for i, elem in enumerate(arr2):
        print("à l'indice {} se trouve {}".format(i, elem))


# --------------------------
# tuple

def tuple():
    pi_tuple = (3, 1, 4, 1, 5, 9)

    tuple_vide = ()
    tuple_non_vide = (1,)  # est équivalent à ci dessous
    tuple_non_vide = 1,
    tuple_avec_plusieurs_valeurs = (1, 2, 5)

    len(pi_tuple)


def dictionary():
    super_heroes = {'Batman': 'Bruce Wayne',
                    'SuperMan': 'Clark Kent',
                    'Hulk': 'Bruce Banner'}

    print(super_heroes['Batman'])
    del super_heroes['Hulk']

    print(len(super_heroes))

    super_heroes['SuperMan'] = "Other"

    print(super_heroes.get("SuperMan"))

    print(super_heroes.keys())

    print(super_heroes.values())


def input():
    # Input
    print("Your name")
    name = sys.stdin.readline()
    print("Hello " + name + "llaume")


def string():
    string = "azertyuio pqsdf ghjklm"
    # 4 premiers caractères
    print(string[0:4])
    # 5 derniers
    print(string[-5:])
    # tous sauf les 5 derniers
    print(string[:-5])
    # concaténation
    print(string[:4] + " yo")
    # formattage
    print("{} is my {} letter and my number {} number is {} %".format('X', 'favorite', 1, .14))
    # premiere lettre en maj
    print(string.capitalize())
    # position à laqe=uelle il trouve la chaine
    print(string.find("rty"))
    # si y a que des caractères
    print(string.isalpha())

    print(string.isalnum())

    print(string.replace("azerty", "hello"))

    print(string.strip())

    words = string.split(" ")
    pprint(words)


def input_output():
    test_file = open("test.txt", "wb")

    print(test_file.mode)
    print(test_file.name)

    # write
    test_file.write("texte")
    test_file.close()

    # read
    test_file = open("test.txt", "r+")
    text_in_file = test_file.read()
    print(text_in_file)

    # remove file
    os.remove("test.txt")


# list()
# dictionary()
# input()
# string()
input_output()

# os.system('ls')
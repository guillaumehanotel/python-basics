#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from pprint import pprint
import random
import math
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




genes = "()1234567890à\"/\\-'’.,ùçêâéèabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

solution = "Classifying documents, or websites, can be an interesting way to start. Start with a list of domains that you like on a topic, and a bunch of unrelated domains. Now try to build a system that will pick out the other domains you like. This will introduce several of the concepts behind machine learning"
generation = 0


# tire une lettre au pif dans les possibilités
def random_gene():
    random_int = random.randint(0, len(genes)-1)
    return genes[random_int]


# génère une proposition de solution de longueur égale à la solution
def make_chromosome():
    # une proposition
    value = ""
    for x in range(0, len(solution)):
        value += random_gene()
    return value


# tire un index au hasard dans la proposition et change son element
def mutate(phrase):
    # Index random
    index = random.randint(0, len(solution)-1)
    # On transforme le string en liste pour modifier un élément
    tab_phrase = list(phrase)
    # on change l'élément à l'index pris au hasard par un gene random
    tab_phrase[index] = random_gene()
    # on transforme la liste en string
    phrase = ''.join(str(x) for x in tab_phrase)
    return phrase


# calcule le score d'une phrase
def quality(phrase):
    score = 0
    for i, elem in enumerate(phrase):
        if solution[i] == elem:
            score += 1
    return score


proposition = make_chromosome()

# Tant que la proposition n'est pas égale à la solution
while proposition != solution:
    mutation = mutate(proposition)
    if quality(mutation) > quality(proposition):
        proposition = mutation
        print(chr(27) + "[2J")
        print(bcolors.OKBLUE + "Gen " + str(generation) + " : " + bcolors.ENDC + str(proposition))
    generation += 1




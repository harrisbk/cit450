#======================================#
#
# file: decisionTree
# desc: read a csv file, randomize data,
#   stratify it, apply a method to
#   predict the value, and return the
#   accuracy
#
# auth: Brennan Harris
# date: 11 may 2015
#
#======================================#

import csv
import math
from random import shuffle

class analyzeList():

    def __init__(self):
        self.list = []
        self.learnSet = []
        self.testSet = []

    def menu(self):
        self.file = raw_input("enter the csv filename: ")
        self.classPosition = int(raw_input("enter the row position of the classification [1 for 1st, 2 for 2nd, etc.]: "))

    def read(self):

        with open(self.file) as iris_data:

            dater = csv.reader(iris_data)

            for thing in dater:
                self.list.append(thing)

            shuffle(self.list)

    def split(self):

        length = len(self.list)

        self.learnSet = range(0,int(.7*length))
        self.testSet = range(0,int(.3*length))

        count = 0

        for i in range(0, int(.7*length)):
            try:
                self.learnSet[i] = self.list[i]
                count += 1
            except:
                pass

        for i in range(0,int(.3*length)):
            try:
                self.testSet[i] = self.list[count]
                count += 1
            except:
                pass
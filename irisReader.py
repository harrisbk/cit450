#======================================#
#
# file: irisReader
# desc: read a csv file, randomize data,
#   stratify it, apply a method to
#   predict the value, and return the
#   accuracy
#
# auth: Brennan Harris
# date: 25 apr 2015
#
#======================================#

import csv
from random import shuffle

class analyzeIris():

    def menu(self):
        self.file = raw_input("enter the csv filename: ")

    def read(self):

        with open(self.file) as iris_data:

            dater = csv.reader(iris_data)

            self.list =[]

            for thing in dater:
                self.list.append(thing)

            shuffle(self.list)

    def split(self):

        self.learnSet = []
        self.testSet = []

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

    def learn(self):

        self.learnedVal = 'Iris-setosa'

    def guess(self):

        self.correctCount = 0
        self.falseCount = 0

        for i in self.testSet:
            if self.learnedVal in i[4]:
                self.correctCount += 1
            else:
                self.falseCount += 1

        self.total = self.correctCount + self.falseCount

        self.percent = int(100 * (float(self.correctCount) / float(self.total)))

    def analyze(self):

        print "The learned value was accurate for "+ str(self.percent) +"% of the test data"

start = analyzeIris()
start.menu()
start.read()
start.split()
start.learn()
start.guess()
start.analyze()
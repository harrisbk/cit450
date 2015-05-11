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
import math
from random import shuffle
from operator import itemgetter
from collections import Counter
#from sklearn import neighbors

class analyzeIris():

    def __init__(self):
        self.list =[]
        self.learnSet = []
        self.testSet = []
        self.correctCount = 0
        self.falseCount = 0

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

    def getEucDist(self, inst1, inst2, length=4):
        distance = 0
        for i in range(length):
            try:
                distance += pow((float(inst1[i]) - float(inst2[i])), 2)
            except:
                pass
        return math.sqrt(distance)

    def neighbors(self,testInst):

        k = 3
        distances = []
        length = len(testInst)-1
        for i in range(1,len(self.learnSet)):
            dist = self.getEucDist(testInst,self.learnSet[i],length)
            distances.append((self.learnSet[i],dist))
        distances.sort(key=itemgetter(1))
        neighbors = []
        for i in range(k):
            neighbors.append(distances[i][0])
        return neighbors

    def guess(self,neighbors):

        list = []
        for i in neighbors:
            list.append(i[self.classPosition - 1])

        classification = Counter(list)
        mode = classification.most_common(1)[0][0]
        print mode
        return mode

    def analyze(self):

        for i in self.testSet:
            guess = self.guess(self.neighbors(i))
            if guess in i[self.classPosition - 1]:
                self.correctCount += 1
            else:
                self.falseCount += 1

        self.total = self.correctCount + self.falseCount

        self.percent = int(100 * (float(self.correctCount) / float(self.total)))

        print "The learned value was accurate for "+ str(self.percent) +"% of the test data"

start = analyzeIris()
start.menu()
start.read()
start.split()
start.analyze()
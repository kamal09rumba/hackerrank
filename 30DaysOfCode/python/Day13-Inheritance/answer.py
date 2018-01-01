#!/usr/bin/python
import sys


# Task 
# You are given two classes, Person and Student, where Person is the base class and 
# Student is the derived class. Completed code for Person and a declaration for 
# Student are provided for you in the editor. Observe that Student inherits 
# all the properties of Person.

class Person:
 def __init__(self, firstName, lastName, idNumber):
  self.firstName = firstName
  self.lastName = lastName
  self.idNumber = idNumber
 def printPerson(self):
  print "Name:", self.lastName + ",", self.firstName
  print "ID:", self.idNumber
class Student(Person):
 def __init__(self,firstName,lastName,idNumber,scores=None):
  Person.__init__(self,firstName, lastName, idNumber)
  if scores is None:
   self.scores = []
  else:
   self.scores = scores
 def calculate(self):
  avg = sum(self.scores)/len(self.scores)
  if  90 <= avg <= 100:
   return 'O'
  if  80 <= avg < 90:
   return 'E'
  if  70 <= avg < 80:
   return 'A'
  if  55 <= avg < 70:
   return 'P'
  if  40 <= avg < 55:
   return 'D'
  if  avg < 40 :
   return 'T'
  else:
   return 'None'

line = raw_input('Enter Name and ID number:-\n').split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input('Enter number scored:-\n')) # not needed for Python
scores = map(int, raw_input('Enter scored number-\n').split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()

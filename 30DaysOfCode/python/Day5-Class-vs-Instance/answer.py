#!/usr/bin/python
class Person:
  def __init__(self,initialAge):
    if initialAge<0:
      self.age = 0
      print 'Age is not valid, setting age to 0'
    else:
      self.age=initialAge

  def amIOld(self):
    if self.age<13:
      print 'You are young.'
    elif self.age>=13 and self.age<18:
      print 'You are teenager.'
    else:
      print 'You are old.'
  def yearPasses(self):
#   self.age = self.age+1 
    self.age +=1

t=int(raw_input('Enter a Range: '))
for i in range(0,t):
 age=int(raw_input('Enter a positive or negative number: '))
 p=Person(age)
 p.amIOld()
 for j in range(0,3):
  p.yearPasses()
 p.amIOld()
 print("")

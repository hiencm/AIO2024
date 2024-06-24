# -*- coding: utf-8 -*-
"""M01W3 Exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sL-VuMA9FS5dBXIU-x0OEPQn_vGg0jdH
"""

import torch
import torch.nn as nn

data = torch.Tensor([1,2,3])
data

softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
output

class MySoftmax(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    x_exp = torch.exp(x)
    total = x_exp.sum(0, keepdim=True)
    return x_exp/total

#Test
my_softmax = MySoftmax()
output = my_softmax(data)
output

data = torch.Tensor([1,2,30000000])
data

my_softmax = MySoftmax()
output = my_softmax(data)
output

class StableSoftmax(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    c = torch.max(x, dim=0)
    x_exp = torch.exp(x - c.values)
    total = x_exp.sum(0, keepdim=True)
    return x_exp/total

#Test
data = torch . Tensor ([1 , 2 , 3])
stable_softmax = StableSoftmax()
output = stable_softmax(data)
output

from abc import ABC, abstractmethod


class Person(ABC):
  def __init__(self, name, yob):
    self._name = name
    self._yob = yob

  def get_yob(self):
    return self._yob

  @abstractmethod
  def describe(self):
    pass

class Student(Person):
  def __init__(self, name, yob, grade):
    super().__init__(name=name, yob=yob)
    self._grade = grade

  def describe(self):
    print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Doctor(Person):
  def __init__(self, name, yob, specialist):
    super().__init__(name=name, yob=yob)
    self._specialist = specialist

  def describe(self):
    print(f"Student - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Teacher(Person):
  def __init__(self, name, yob, subject):
    super().__init__(name=name, yob=yob)
    self._subject = subject

  def describe(self):
    print(f"Student - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Ward():
  def __init__(self, name):
    self.__name = name
    self.__list_people = list()

  def add_person(self, person: Person):
    self.__list_people.append(person)

  def describe(self):
    print(f"Name: {self.__name}")
    for p in self.__list_people:
      p.describe()

  def count_doctor(self):
    counter = 0
    for p in self.__list_people:
      if isinstance(p, Doctor):
        counter += 1
    return counter

  def sort_yob(self):
    return self.__list_people.sort(key = lambda x: x.get_yob(), reverse=True)

  def compute_average(self):
    total = 0
    counter = 0
    for p in self.__list_people:
      if isinstance(p, Teacher):
        total += p.get_yob()
        counter += 1
    return total / counter

#test
student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward ( name =" Ward1 ")
ward1.add_person ( student1 )
ward1.add_person ( teacher1 )
ward1.add_person ( teacher2 )
ward1.add_person ( doctor1 )
ward1.add_person ( doctor2 )
ward1.count_doctor ()

class MyStack:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__stack = []

  def is_empty(self):
    return len(self.__stack) == 0

  def is_full(self):
    return len(self.__stack) == self.__capacity

  def push(self, item):
    if self.is_full():
      raise Exception('Overflow')
    self.__stack.append(item)

  def pop(self):
    if self.is_empty():
      raise Exception('Underflow')
    self.__stack.pop()

  def top(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    return self.__stack[-1]

# Test
my_stack = MyStack(4)
my_stack.is_empty()
my_stack.push(5)
my_stack.push(6)
#my_stack.push(7)
my_stack.is_empty()
my_stack.is_full()
#my_stack.pop()
my_stack.top()

class MyQueue:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__queue = []

  def is_empty(self):
    return len(self.__queue) == 0

  def is_full(self):
    return len(self.__queue) == self.__capacity

  def enqueue(self, item):
    if self.is_full():
      raise Exception('Overflow')
    self.__queue.append(item)

  def dequeue(self):
    if self.is_empty():
      raise Exception('Underflow')
    self.__queue.pop(0)

  def front(self):
    if self.is_empty():
      raise Exception('Queue is empty')
    return self.__queue[0]

# Test

my_queue = MyQueue(5)
my_queue.is_empty()
my_queue.enqueue(5)
my_queue.enqueue(6)
#my_queue.enqueue(7)
#my_queue.enqueue(8)
#my_queue.enqueue(9)
my_queue.is_full()
my_queue.front()

my_queue.dequeue()
my_queue.front()
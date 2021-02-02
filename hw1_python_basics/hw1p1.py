#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

#[A]
print('\nA')
for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

#[B]
print('\n\nB')
newlist=[len(x) for x in list_of_names]
print('lenght of names:')
print(newlist)
#[E]
import person

people={list_of_names[i]:person.person(list_of_names[i],list_of_ages[i],list_of_heights_cm[i])for i in range(0,len(list_of_names))}
print('\n\nE')
print (people) 

#[F]
a=np.array(list_of_ages)

b=np.array(list_of_heights_cm)

#[G]
mean_of_ages=np.mean(a)
print('\n\nG')
print(f"The mean of ages of the people is {mean_of_ages}")

#[H]
plt.scatter(list_of_ages,list_of_heights_cm)
plt.xlabel("age")
plt.ylabel("height")
plt.grid(axis='both')
plt.title("Scatter Plot of Age and Height")
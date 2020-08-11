import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#Exercise 1
print((a<0).sum())

#Exercise 2
print((a>0).sum())

#Exercise 3
#try 1
#pos_num = a > 0
#even_num = a % 2 == 1
#desired_range = pos_num & even_num
#desired_nums = a[desired_range]
#print(desired_nums.shape)

#try 2
#pos_num = a == a > 0
#even_num = a % 2 == 1

# return a boolean array with True for values that meet both conditions
pos_and_even_nums = (a > 0) & (a % 2 == 0)
# sum the True values to get a total of values that meet both conditions
print((pos_and_even_nums).sum())

#Exercise 4
add_three_a = a + 3
add_three_pos_nums = add_three_a % 2 == 0
print(add_three_pos_nums.sum())

#Exercise 5
sq_a = a ** 2
print('Mean for Squared a: ')
print(sq_a.mean())
print('Standard Deviation for Squared a: ')
print(sq_a.std())

#Exercise 6
#centering
a_mean = a.mean()
a_center = a - a_mean
print(a_center)

#Exercise 7
def zscore(x):
    return ((x - a_mean) / a.std())
print('Z Score of each data point: ')
print(zscore(a))















#
#Notes from chat
#
#
#https://numpy.org/doc/stable/reference/generated/numpy.where.html
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])np.where(a < 5, a, 10*a)array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])
#
#b = np.array([    [3, 4, 5],    [6, 7, 8]])b.sum()
#np.sum(b)
#
#
#squares = [i ** 2 for x in b for in x]squares = [i ** 2 for x in b for i in x]for x in b:
#       for i in x:
#           squares.append( i ** 2)
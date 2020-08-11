import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#Exercise 1
print((a<0).sum())
#maggie's alternate answer
len(a[a < 0])

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
add_three_pos_nums = add_three_a > 0
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
plt.hist(a_center)

#Exercise 7
def zscore(x):
    return ((x - a_mean) / a.std())
print('Z Score of each data point: ')
print(zscore(a))
#answer from class review
a_z_score = a_center / a.std()
print('Z scores: ')
print(a_z_score)
#if data is centered and scaled, a_z_score.std() will be 1 and a_z_score.mean() will be 0.

#
#
#

#Exercise 8 (copied from Life without Numpy)
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1

for n in a:
    product_of_a *= n

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n**2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]

#
#
#

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
#sum_of_b = 0
#for row in b:
#    sum_of_b += sum(row)
b = np.array(b)
b.sum()

# Exercise 2 - refactor the following to use numpy. 
#min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
#max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = b.max()
max_of_b


# Exercise 4 - refactor the following using numpy to find the mean of b
#mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
#product_of_b = 1
#for row in b:
#    for number in row:
#        product_of_b *= number
product_of_b = b.prod()
product_of_b

# Exercise 6 - refactor the following to use numpy to find the list of squares 
#squares_of_b = []
#for row in b:
#    for number in row:
#        squares_of_b.append(number**2)
squares_of_b = b ** 2
squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b
#odds_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 != 0):
#            odds_in_b.append(number)
odds_in_b = b[b % 2 == 1]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
#evens_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 == 0):
#            evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]
evens_in_b

# Exercise 9 - print out the shape of the array b.
print(b.shape)

# Exercise 10 - transpose the array b.
print(b.T)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(-1, 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2













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
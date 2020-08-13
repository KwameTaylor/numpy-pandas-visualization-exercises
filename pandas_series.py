import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Exercise 1
print(' \n \n Exercise 1 \n')
#a
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
print('Fruits series: ')
print(fruits)
#b
print(fruits.describe())
#print(type(fruits))
#c
unique_fruits = fruits.unique()
print(unique_fruits)
#print(type(unique_fruits))
#d
print(fruits.value_counts())
#e
print(fruits.mode())
#f
print(fruits.value_counts().tail(1))
#g
print(fruits.max())
#h
print(fruits[fruits.str.len() >= 5])
#i
print(fruits.str.capitalize())
#j
print(fruits.str.count('a'))
#k
print(fruits.str.count('[aeiou]'))
#l
#first try commented
#contains_two_or_more_o_count = 0
#print(fruits.apply(lambda n: n.str.contains('[%o%o%]')))
print(fruits[fruits.apply(lambda fruit: fruit.count('o') > 1)])
#m
print(fruits[fruits.str.contains('berry')])
#n
print(fruits[fruits.str.contains('apple')])
#o
print(fruits[(fruits.str.count('[aeiou]')).idxmax()])

#Exercise 2
print(' \n \n Exercise 2 \n')
money_series = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print(type(money_series))
money_series_float = money_series.str.replace('$', '')
money_series_float = money_series_float.str.replace(',', '')
money_series_float = money_series_float.astype(float)
print(money_series_float)
print('Max: ')
print(money_series_float.max())
print('Min: ')
print(money_series_float.min())
money_series_bins = pd.cut(money_series_float, 4)
pd.cut(money_series_float, 4).value_counts().sort_index(ascending=False).plot(kind='barh', color = 'thistle', ec='black', width=1)
plt.title('4 Bins to Rule Them All')
plt.xlabel('Count')
plt.show()

#Exercise 3
print(' \n \n Exercise 3 \n')
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
print('Max exam score: ')
print(exam_scores.max())
print('Mean exam score: ')
print(exam_scores.mean())
print('Median exam score: ')
print(exam_scores.median())
plt.hist(exam_scores)
plt.show()
def num_grade(score):
    if score >= 88:
        return "A"
    elif 80 <= score < 88:
        return "B"
    elif 67 <= score < 80:
        return "C"
    elif 60 <= score < 67:
        return "D"
    else:
        return "F"
exam_grades = exam_scores.apply(num_grade)
print(exam_grades)
curve_diff = 100 - int(exam_scores.max())
exam_scores_curved = exam_scores + curve_diff
exam_grades_curved = exam_scores_curved.apply(num_grade)
print('Exam scores curved: ')
print(exam_scores_curved)
print('Exam grades curved: ')
print(exam_grades_curved)

#Exercise 4

#faiths version
#string_list = string.replace('', ' ').strip().split(' ')

print(' \n \n Exercise 4 \n')
string_series = pd.Series('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
string_series = string_series.str.extractall("(.)")
vowels = list('aeiou')
consonants = list('bcdfghjklmnpqrstvwxyz')
print(string_series)
print('Most freq occuring letter: ')
print(string_series.mode())
print('Least freq occuring letter: ')
#print(string_series.value_counts().tail(1))
print('Vowel count: ')
#print(string_seriesstring_series.str.lower().str.count('[aeiou]').sum())
print('Consonant count: ')
#print(string_series[string_series.isin('aeiou')])
#now create a version of the series that is uppercased
#create a bar plot of the freqs of the 6 most freq occuring letters
#string_series.value_counts().head(6).plot(kind='barh', width=.8)
#plt.title('Top 6 Letters')
#plt.show()

#Exercise 5
print(' \n \n Exercise 5 \n')
#Complete the exercises from 
# but use pandas Series for the data structure instead of lists and use Series subsetting/indexing
# and vectorization options instead of loops and lists.

# 17 list comprehension problems in python

#fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

#numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
#numbers_plus_one = []
#for number in numbers:
#    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
#numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
#output = []
#for fruit in fruits:
#    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using pandas. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
fruits = pd.Series(['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'])
uppercased_fruits = fruits.str.upper()
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use pandas to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = fruits.str.capitalize()
print(capitalized_fruits)

# Exercise 3 - Use pandas to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels = fruits[fruits.str.count('[aeiou]') > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = fruits[fruits.str.count('[aeiou]') == 2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_str_len = fruits.str.len()
print(fruits[fruits_str_len > 5])

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_equal_to = fruits[fruits.str.len() == 5]
print(fruits_equal_to)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
print(fruits[fruits_str_len < 5])

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
print(fruits.str.len())

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = fruits[fruits.str.contains('a')]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
numbers = pd.Series([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9])
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = numbers[numbers % 2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = numbers[numbers > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = numbers[numbers < 0]
print(negative_numbers)

# Exercise 14 - use pandas w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
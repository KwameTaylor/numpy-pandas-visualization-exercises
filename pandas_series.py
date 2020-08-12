import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Exercise 1
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
print((fruits.str.count('a')).sum())
#k
print(fruits.str.count('[aeiou]'))
#l
#come back to this one later
#contains_two_or_more_o_count = 0
#print(fruits.apply(lambda n: n.str.contains('[%o%o%]')))
#m
print(fruits[fruits.str.contains('berry')])
#n
print(fruits[fruits.str.contains('apple')])
#o
print(fruits[fruits.str.count('[aeiou]')].max())

#Exercise 2
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
print(money_series_bins)
plt.hist(money_series_float)
plt.show()
#not sure why the histo isn't plotting with the bins... come back to this later
#TypeError: unorderable types: Interval() < float() when i try to plt.hist(money_series_bins)

#Exercise 3
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
print(string_series[letters_series.isin(vowels)])
print('Consonant count: ')
#print(string_series[string_series.isin('aeiou')])
#now create a version of the series that is uppercased
#create a bar plot of the freqs of the 6 most freq occuring letters

#Exercise 5
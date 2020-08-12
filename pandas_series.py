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
#plt.hist(money_series_bins)
#plt.show()
#not sure why the histo isn't plotting... come back to this later
#TypeError: unorderable types: Interval() < float()

#Exercise 3
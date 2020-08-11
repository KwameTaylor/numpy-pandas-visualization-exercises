import pandas as pd
import numpy as np

#Exercise 1
#a
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
#b
print(fruits.describe())
print(type(fruits))
#c
unique_fruits = fruits.unique()
print(unique_fruits)
print(type(unique_fruits))
#d
#print(unique_fruits.value_counts)
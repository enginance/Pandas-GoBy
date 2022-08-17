##############################################################################################################
# ██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
# ██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
# ██████╔╝███████║██╔██╗██║██║░░██║███████║╚█████╗░
# ██╔═══╝░██╔══██║██║╚████║██║░░██║██╔══██║░╚═══██╗
# ██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██████╔╝
# ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░
##############################################################################################################

##############################################################################################################
# References    
##############################################################################################################
# https://medium.datadriveninvestor.com/python-pandas-library-for-beginners-a-simplified-guide-for-getting-started-and-ditching-20992b7cd4da
# https://medium.com/pythoneers/pandas-handbook-for-beginners-in-10-minutes-721bd5d1fcf2
# https://medium.com/wicds/a-comprehensive-guide-to-pandas-for-data-science-64ed1be1bafe


##############################################################################################################
# Thanks to    
##############################################################################################################
# https://github.com/bendgame/JerkyNotebook


##############################################################################################################
# Pandas Handbook
##############################################################################################################

# CTRL + C + K --> adds comments to selected text
# CTRL + K + U --> removes comments to selected text

##############################################################################################################
# Installation with pip or Anaconda:
##############################################################################################################
# pip install pandas
# or
# conda install pandas

import pandas as pd


#set the file path
# filepath = r'Data\beef-jerky\jerky.csv'
filepath = r'jerky.csv'


##############################################################################################################
# Using read_csv to open the csv file into a pandas DataFrame
##############################################################################################################
#open the csv data into a dataframe named df
df = pd.read_csv(filepath)


##############################################################################################################
# Introduction to Exploring DataFrames
##############################################################################################################
#Example of n values
df.head(1) #returns top 1 row
print("returns top 1 row")
print(df.head(1))

df.tail(10) #returns last 10 rows
print("returns last 10 rows")
print(df.tail(10))

#display the columns
df.columns
print("display the columns")
print(df.columns)

#display the index
df.index
print("display the index")
print(df.index)

#Display the first 5 rows using .head()
df.head()
print("Display the first 5 rows using .head()")
print(df.head())

#Display the last 5 rows using .tail()
df.tail()
print("Display the last 5 rows using .tail()")
print(df.tail())

#generate statistics 
df.describe()
print("generate statistics")
print(df.describe())

#display the columns and data types
df.info()
print("display the columns and data types")
print(df.info())


##############################################################################################################
# Working with Data
##############################################################################################################
#only select the brand column
df['brand'].head()
print("only select the brand column")
print(df['brand'].head())
# OR
# df.head()['brand']

#select the brand and flavor column. Notice the double bracket [[]]
df[['brand', 'flavor']].head()
print("select the brand and flavor column. Notice the double bracket [[]]")
print(df[['brand', 'flavor']].head())

#return unique values
print("Selecting the unique values from a column using .unique()")
print(df['brand'].unique())

print("Selecting the count of unique values from a column using .nunique()")
print(df['brand'].nunique())


##############################################################################################################
# Selecting Data
##############################################################################################################
#slicing the dataframe
df[['brand','flavor']][5:7]
print("slicing the dataframe")
print(df[['brand','flavor']][5:7])

#return the rows with a value Original in column flavor
df[['brand','flavor']].loc[df['flavor'] == 'Original']
print("return the rows with a value Original in column flavor")
print(df[['brand','flavor']].loc[df['flavor'] == 'Original'])

#return the rows with a value Original in column flavor
df[['brand','flavor']].iloc[[0,4]]
print("return the rows with a value Original in column flavor with indices selection")
print(df[['brand','flavor']].iloc[[0,4]])


##############################################################################################################
# Common Operations and Functions
##############################################################################################################
#Use .Count() to find the number of rows
df[['brand', 'flavor']].count()
print("Use .Count() to find the number of rows")
print(df[['brand', 'flavor']].count())

#Use .mean() to find the mean sodium value
df['sodium'].mean()
print("Use .mean() to find the mean sodium value")
print(df['sodium'].mean())
#438.3333333333333

# Use .median() to find the median sodium value
df['sodium'].median()
print("Use .median() to find the median sodium value")
print(df['sodium'].median())
#470.0

# Use .mode() to find the mode sodium value
df['sodium'].mode()
print("Use .mode() to find the mode sodium value")
print(df['sodium'].mode())
#520

# Use .min() to find the minimum sodium value
df['sodium'].min()
print("Use .min() to find the minimum sodium value")
print(df['sodium'].min())
#140

# Use .max() to find the maximum sodium value
df['sodium'].max()
print("Use .max() to find the maximum sodium value")
print(df['sodium'].max())
#650


##############################################################################################################
# Creating New Columns
##############################################################################################################
# DataFrame[‘column name’] = something

#make a copy
df_copy = df.copy()
print("make a copy")
print(df_copy)

#add a new column
df_copy['My_New_Column'] = 1
print("add a new column")
print(df_copy['My_New_Column'])

#display the new column
df_copy[['brand','flavor','My_New_Column']].head(3)
print("display the new column")
print(df_copy[['brand','flavor','My_New_Column']].head(3))

#create a new column displaying the mean value of sodium
df_copy['sodium_mean'] = df['sodium'].mean()
df_copy[['brand','flavor','sodium','sodium_mean']].head(3)
print("create a new column displaying the mean value of sodium")
print(df_copy[['brand','flavor','sodium','sodium_mean']].head(3))


##############################################################################################################
# More Advanced Columns
##############################################################################################################      
#use a for loop to create a new column
average_calories = df_copy['calories'].mean()
above_average = []
for calories in df_copy['calories']:
    if calories > average_calories:
        above_average.append(1)
    else:
        above_average.append(0)
df_copy['above_average_calories'] = above_average
print("use a for loop to create a new column")
print(df_copy['above_average_calories'])
print(df_copy[['brand','flavor','sodium','above_average_calories']].head(3))



##############################################################################################################
# List comprehensions
##############################################################################################################
# The for loop is not optimal; look at all that code! I can imagine using a for loop if the readability is of utmost important, 
# but most often I will go the pythonic route and try to use a list comprehension.

#Use list comprehensions to create new columns
#Create a new column that outputs a 1 if the cost is greater than #the average. Else 0
df_copy['above_average_calories'] = [1  if n > average_calories else 0 for n in df_copy['calories']]
print("Create a new column that outputs a 1 if the cost is greater than #the average. Else 0")
print(df_copy['above_average_calories'])

#Create a word_count column that outputs the number of words in the #manufactureDescription
df_copy['word_count'] = [len(str(words).split(" ")) for words in df_copy['manufactureDescription']]
print("Create a word_count column that outputs the number of words in the #manufactureDescription")
print(df_copy['word_count'])

#Display the top 3 rows
df_copy[['brand','flavor','above_average_calories','word_count']].head(3)
print("Display the top 3 rows")
print(df_copy[['brand','flavor','above_average_calories','word_count']].head(3))

#Create a new column that outputs the number of words in the manufactureDescription
df_copy['word_count']= df_copy['manufactureDescription'].apply(lambda x: len(str(x).split(" ")))
print("Create a new column that outputs the number of words in the manufactureDescription")
print(df_copy[['brand','flavor','above_average_calories','word_count']].head(3))


##############################################################################################################
# Sorting, Grouping and Pivoting Data
##############################################################################################################
#sort the data 
df_copy[['brand','protein', 'calories','flavor']].sort_values('calories', ascending = False)
print("Sort the data by calories descending")
print(df_copy[['brand','protein', 'calories','flavor']].sort_values('calories', ascending = False))

#group by brand and calc mean
df_copy[['brand','protein', 'calories','gluten free']].groupby('brand').mean()
print("Calculate the mean protein and calories grouped by brand.")
print(df_copy[['brand','protein', 'calories','gluten free']].groupby('brand').mean())


##############################################################################################################
# Use pandas.pivot_table() to create a spreadsheet-like pivot table
##############################################################################################################
# For the pivot table example, import numpy to use aggregate functions
import numpy as np
pd.pivot_table(df_copy, index = ['brand'], values = ['calories'], aggfunc = np.mean)
print("Use pandas.pivot_table() to create a spreadsheet-like pivot table")
print(pd.pivot_table(df_copy, index = ['brand'], values = ['calories'], aggfunc = np.mean))

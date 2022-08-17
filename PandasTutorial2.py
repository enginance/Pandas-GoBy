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
# https://medium.com/pythoneers/pandas-handbook-for-beginners-in-10-minutes-721bd5d1fcf2


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

##############################################################################################################
# Read Data From a File
##############################################################################################################
# import pandas as pd
# data = pd.read_csv('data.csv') ##data.csv is the filepath for data


##############################################################################################################
# Read Data From a URL
##############################################################################################################
# Read Data From a URL
data=pd.read_csv('https://raw.githubusercontent.com/Abhayparashar31/machine-learning-projects/master/titanic_dataset/data/train.csv') ## pass url as input
## TO read data from github first click on raw then copy the url and paste in the function
print("Read Data From a URL")
print(data)


##############################################################################################################
# Creating our own Dataframe and series objects
##############################################################################################################
# In pandas to create a dataset, we have DataFrame that can be used to create a data frame. let see it in code.

import pandas as pd
names = ["karl","anna","larry","louis"] ## Column 1
age = [20,23,19,22]             ## Column 2
dataset = list(zip(names,age))   ## Combine both columns
df = pd.DataFrame(dataset,columns=['Names', 'Age'])
                 ## dataset name ## columns names
print("Creating our own Dataframe and series objects")
print(df)
# ##########OUTPUT############
#    Names  Age
# 0  karl   20
# 1  anna   23
# 2  larry  19
# 3  louis  22


##############################################################################################################
# We can also create a DataFrame using series.
##############################################################################################################
# We can also create a DataFrame using series.

series1 = pd.Series(["BMW","TOYOTA","SWIFT"])
series2 = pd.Series(["RED","BLUE","WHITE"])
## Using series
df = pd.DataFrame({"model":series1,"color":series2})
print("We can also create a DataFrame using series.")
print(df)
# ##########OUTPUT##########
#    model  color
# 0  BMW    RED
# 1  TOYOTA BLUE
# 2  SWIFT  WHITE


##############################################################################################################
# Add, update, and deleting rows and column
##############################################################################################################

##############################################################################################################
# Adding a new column to the data frame
##############################################################################################################
modelNumber = ['0215E6','0216E7','0217E8']
df['modelNumber'] = modelNumber
print("Adding a new column to the data frame")
print(df)
# ########OUTPUT############
#    model  color  modelNumber
# 0  BMW    RED    0215E6
# 1  TOYOTA BLUE   0216E7
# 2  SWIFT  WHITE  0217E8


##############################################################################################################
# Update a new column in the data frame
##############################################################################################################
Brand = ["TATA","TOYOTA","AUDI"]
df['model'] = Brand
print("Update a new column in the data frame")
print(df)
# ########OUTPUT##########
#    model  color  modelNumber
# 0  TATA   RED    0215E6
# 1  TOYOTA BLUE   0216E7
# 2  AUDI   WHITE  0217E8


##############################################################################################################
# Deleting a Row and Column
##############################################################################################################
## Drop Column
df_copy = df.drop('color',axis=1)
print("Drop Column")
print(df_copy)

## Drop Row
df_copy = df.drop([1])
print("Drop row")
print(df_copy)


##############################################################################################################
# Retrieving Data
##############################################################################################################

##############################################################################################################
# Retrieving a particular column
##############################################################################################################
df['model']
print("Retrieving a particular column")
print(df['model'])
# #####output######
# 0      TATA
# 1      TOYOTA
# 2      AUDI

df['model'][:1]  ##top two rows
print("Retrieving a particular column, top two rows")
print(df['model'][:2])
# #####output######
# 0      TATA
# 1      TOYOTA


##############################################################################################################
# Retrieving rows and columns
# Using iloc
##############################################################################################################
df.iloc[:,0]        ### all rows and 0 columns
df.iloc[:,0:2]      ### all rows and 0,1 columns
df.iloc[0,0:2]      ### 0 row and 0,1 columns
df.iloc[0,:]        ### 0 row and all columns
df.iloc[1,1]        ### 1 row and 1 columns

print("Example retrieving 1 row and 1 columns")
print(df.iloc[1,1]  )

# selecting 0th, 2th, 4th, and 7th index rows
print("selecting 0th, 2th, 4th, and 7th index rows")
print(data.iloc[[0, 2, 4, 7]])

# selecting rows from 1 to 4 and columns from 2 to 4
print("selecting rows from 1 to 4 and columns from 2 to 4")
print(data.iloc[1: 5, 2: 5])


##############################################################################################################
# Retrieving rows and columns
# Using loc
##############################################################################################################
df.loc[0:1]      ### 0,1 row and 0,1 columns
df.loc[0]        ### 0 row
df.loc[:]        ### all rows and columns
df.loc[0,:]      ### 0 rows and all columns

print("Retrieving 0 rows and all columns")
print(df.loc[0,:])



##############################################################################################################
# Exporting Data to files
##############################################################################################################
# After doing all the processing on the data then we need to dump the data into a file.

### Let's first create a DataFrame
## Create dataset
import random
names = ['Bob','Jessica','Mary','John','Mel']
random.seed(500)
random_names = [names[random.randint(0,len(names)-1)] for i in range(1000)]
random_number = [random.randint(0,1000) for i in range(1000)]
data = list(zip(random_names,random_number))
df = pd.DataFrame(data,columns=['Name','Number'])
## save it to a csv file
df.to_csv('data1.csv',index=False,header=False)
### open the save csv file
df = pd.DataFrame(data,columns=['Name','Number'])
df.head()

print("save it to a csv file and open the save csv file")
print(df.head())



##############################################################################################################
# Different types of functions in pandas
# Group by: This function is used to split the data into groups based on some criteria.
# pandas objects can be split on any of their axes.
##############################################################################################################
demo = {
'letter':["a","b","c","d","a","c","c","d"],
'a':[1,2,3,4,5,6,7,8],
'b':[1,4,9,16,25,36,49,64]
}
df = pd.DataFrame(demo)
df.groupby("letter").sum()
print("Example of group by letter to get the sum value")
print(df.groupby(['letter']).sum())
# ###OUTPUT####
# letter a  b
# a      62 6
# b      2  4
# c      16 94
# d      12 80


df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
print(df)
#    Animal  Max Speed
# 0  Falcon      380.0
# 1  Falcon      370.0
# 2  Parrot       24.0
# 3  Parrot       26.0
df.groupby(['Animal']).mean()
print("Example of group by Animal to get the mean value")
print(df.groupby(['Animal']).mean())
#         Max Speed
# Animal
# Falcon      375.0
# Parrot       25.0



##############################################################################################################
# Different types of functions in pandas
# Sum : Pandas DataFrame.sum()function is used to return the sum of the values for the requested axis by the user.
##############################################################################################################
demo = {
'letter':["a","b","c","d","a","c","c","d"],
'a':[1,2,3,4,5,6,7,8],
'b':[1,4,9,16,25,36,49,64]
}
df = pd.DataFrame(demo)


df["a"].sum()
print("Example sum of a dataframe")
print(df["a"].sum())
# ###OUTPUT##
# 36


##############################################################################################################
# Different types of functions in pandas
# Max: Return the maximum of the values for the requested axis. default axis=None.
##############################################################################################################
df["a"].max()
print("Example max of a dataframe")
print(df["a"].max())
# ###OUTPUT##
# 8


##############################################################################################################
# Different types of functions in pandas
# Min: Return the minimun of the values for the requested axis. default axis=None.
##############################################################################################################
df["a"].min()
print("Example min of a dataframe")
print(df["a"].min())
# ###OUTPUT##
# 1


##############################################################################################################
# Different types of functions in pandas
# Unique: Find all the unique values in the given column or dataset.
##############################################################################################################
df['letter'].unique()
print("Example unique values of a dataframe")
print(df['letter'].unique())
# ###OUTPUT###
# array(['a', 'b', 'c', 'd'], dtype=object)



##############################################################################################################
# Different types of functions in pandas
# Sample: Generates a random sample of data or shuffles rows of dataframe.
##############################################################################################################
df = df.sample(frac=1)
print("Example sample or shuffles rows of a dataframe")
print(df)
# ###OUTPUT######
# letter a  b
# d      12 80
# a      62 6
# c      16 94
# b      2  4



##############################################################################################################
# Merging Two DataFrames
# Pandas provide the simplest way to combine two data frames together. 
# There are many build-in functions present in pandas. 
##############################################################################################################
# Let’s Look Each One By One but first let’s create two dummy datasets of 5 records each using the above techniques You have understood.

##### DataFrame 1
names = ["karl","anna","larry","louis"]
age = [20,23,19,22]
id = [1,2,3,4]
dataset = list(zip(id,names,age))
df1 = pd.DataFrame(dataset,columns=['id','names','age'])
print("Dataframe 1 is: ")
print(df1)
#### DataFrame 2
info = {"id":[1,2,3,4],"Email":["xyz@gmail.com","XYZ@gmail.com","Demo@gmail.com","Louis231@gmail.com"]}
df2 = pd.DataFrame(info)
print("Dataframe 2 is: ")
print(df2)



##############################################################################################################
# Merging Two DataFrames
# Concat:  It is used when both the data frames have the same columns.
##############################################################################################################
df = pd.concat([df1,df2])
print("Concat:  It is used when both the data frames have the same columns.")
print(df)
# #########OUTPUT##########
#  id names age Email
# 0 1 karl  20.0 NaN
# 1 2 anna  23.0 NaN
# 2 3 larry 19.0 NaN  👈NaN Values Because of New Column
# 3 4 louis 22.0 NaN
# 0 1 NaN   NaN  xyz@gmail.com 👈 Append After df1 ends
# 1 2 NaN   NaN  XYZ@gmail.com
# 2 3 NaN   NaN  Demo@gmail.com
# 3 4 NaN   NaN  Louis231@gmail.com

##### To make it More Understandable we can also add Keys to 
df = pd.concat([df1,df2],keys=['df1', 'df2'])
print("To make it More Understandable we can also add Keys to ")
print(df)



##############################################################################################################
# Merging Two DataFrames
# Merge : It is Used to Merge Two Data Set Using Joins and Keys. 
# It is Mostly Used to Combine Two Data Set Into Each other Based on a common Key.
##############################################################################################################
df = df1.merge(df2,on='id')
print("Merge : It is Used to Merge Two Data Set Using Joins and Keys. ")
print(df)
# #######OUTPUT##########
#   id names age Email
# 0 1 karl  20  xyz@gmail.com
# 1 2 anna  23  XYZ@gmail.com
# 2 3 larry 19  Demo@gmail.com
# 3 4 louis 22  Louis231@gmail.com
# Common ID     Merging of New Column



##############################################################################################################
# EDA (Exploratory Data Analysis)
##############################################################################################################
## Reading data
df = pd.read_csv('https://raw.githubusercontent.com/Abhayparashar31/machine-learning-projects/master/heart_disease/heart.csv')
df.head(2)
print("EDA (Exploratory Data Analysis) read csv")
print(df.head(2))
# #####OUTPUT#####
# age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal target
# 0 63 1 3 145 233 1 0 150 0 2.3 0 0 1 1 
# 1 37 1 2 130 250 0 1 187 0 3.5 0 0 2 1 

##############################################################################################################
# df.dtype : Return the datatype of the columns
print("df.dtype : Return the datatype of the columns")
print(df.dtypes)

##############################################################################################################
# df.describe() : Give a description of data
print("df.describe() : Give a description of data")
print(df.describe())

##############################################################################################################
# df.info() : Print a concise summary of a DataFrame.
print("df.info() : Print a concise summary of a DataFrame.")
print(df.info())

##############################################################################################################
# df.isnull().sum() : Returns the sum of all null values
df.isnull().sum()    ### df.isna().sum()
print("df.isnull().sum() : Returns the sum of all null values")
print(df.isnull().sum())

##############################################################################################################
# df.nunique() : Find the total number of unique values in each columns
df.nunique()
print("df.nunique() : Find the total number of unique values in each columns")
print(df.nunique())
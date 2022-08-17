##############################################################################################################
# ██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░░██████╗
# ██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
# ██████╔╝███████║██╔██╗██║██║░░██║███████║╚█████╗░
# ██╔═══╝░██╔══██║██║╚████║██║░░██║██╔══██║░╚═══██╗
# ██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██████╔╝
# ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░
##############################################################################################################


##############################################################################################################
# Loading data into Pandas
##############################################################################################################
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# Print head
print(df.head(5))

# Print tail
print(df.tail(5))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(df.head(5))

print(df['HP'])


##############################################################################################################
# Reading Data in Pandas
##############################################################################################################
# Read Headers
print(df.columns)

# Read each Column
print(df[['Name', 'Type 1', 'HP']])

# Read Each Row
print(df.iloc[0:4])
for index, row in df.iterrows():
    print(index, row['Name'])
df.loc[df['Type 1'] == "Grass"]

# Read a specific location (R,C)
print(df.iloc[2,1])


##############################################################################################################
## Sorting/Describing Data
##############################################################################################################
df.sort_values(['Type 1', 'HP'], ascending=[1,0])

print(df)


##############################################################################################################
# Making changes to the data
##############################################################################################################
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

print(df.head(5))


##############################################################################################################
## Saving our Data (Exporting into Desired Format)
##############################################################################################################
# df.to_csv('modified.csv', index=False)

# df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')


##############################################################################################################
## Filtering Data
##############################################################################################################
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

new_df.reset_index(drop=True, inplace=True)

print(new_df)

new_df.to_csv('filtered.csv')


##############################################################################################################
## Conditional Changes
##############################################################################################################
# df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

# df

df = pd.read_csv('modified.csv')

print(df)


##############################################################################################################
## Aggregate Statistics (Groupby)
##############################################################################################################
df = pd.read_csv('modified.csv')

# I initialize the "count" field and assign number 1 to each item
df['count'] = 1

# to group everything by Type 1 and then subgroup by Type 2 we can do the following
df.groupby(['Type 1', 'Type 2']).count()['count']

# if I want to count them
df.groupby(['Type 1']).count()
print(df.groupby(['Type 1']).count())


print(df.groupby(['Type 1', 'Type 2']).count()['count'])

##############################################################################################################
# to see which group has the highest attack
df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)

print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))


##############################################################################################################
## Working with large amounts of data
##############################################################################################################
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])
    
print(new_df)

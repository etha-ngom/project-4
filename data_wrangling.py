import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Imports csv as df
df = pd.read_csv("data/uncivilized.csv")

# Removes unwanted unknown column
df = df[df.columns[1:]]

# Removes the United States of America
df = df.drop(903)
df.reset_index(inplace=True)

# Shows the data types of each column and how many null values there are
# print(df.info())

# Removing the space at the front of the column name " Debt at end of fiscal year"
df.rename(columns={" Debt at end of fiscal year" : "Debt at end of fiscal year"}, inplace=True)

# Fixing the columns that are len = 1 dictionaries (actually strings, but look like dictionaries)
# Correction, Education, Health, Utilities, Welfare
df["Correction"] = df["Correction"].apply(lambda x : int(x[list(x).index(":")+2:-1]))
df["Education"] = df["Education"].apply(lambda x : int(x[list(x).index(":")+2:-1]))
df["Health"] = df["Health"].apply(lambda x : int(x[list(x).index(":")+2:-1]))
df["Utilities"] = df["Utilities"].apply(lambda x : int(x[list(x).index(":")+2:-1]))
df["Welfare"] = df["Welfare"].apply(lambda x : int(x[list(x).index(":")+2:-1]))
# print(df.info())

# Now, fixing the more complicated dictionaries
# Financial Aid, Intergovernmental.1, Natural Resources, Transportation,

# For Financial Aid, there are 2 different dictionary keys ("Assistance and Subsidies" and "Cash and Securities")
# I will sum them and keep the sum under "Financial Aid"
# This is an absolute monstrosity, but it works and makes sense if you break it down.
# I created it by perfecting the extraction of each value separately. I might explain it in the readme.
df["Financial Aid"] = df["Financial Aid"].apply(lambda x : int(x[int(list(x).index(":")+2):list(x).index(",")]) + int(x[list(x).index(":", (list(x).index(":", (list(x).index(":")+1))))+2:-1]))

# For Intergovernmental.1, there are 2 different dictionary keys ("Intergovernmental Expenditure" and "Intergovernmental to Combined and Unallocable")
# I'm not sure the difference between Intergovernmental and Intergovernmental.1, but I will keep them both for now
# I'm also going to sum them and keep them under the umbrella column just in case we want it later
# Same command as the Financial Aid, but with this column
df["Intergovernmental.1"] = df["Intergovernmental.1"].apply(lambda x : int(x[int(list(x).index(":")+2):list(x).index(",")]) + int(x[list(x).index(":", (list(x).index(":", (list(x).index(":")+1))))+2:-1]))

# For Natural Resources, there are 2 different dictionary keys and one dictionary within the second ("Natural Resources Construction" and "Parks", which has "Parks Total Expenditure Inside")
# I'm going to have the "Natural Resources Construction" as the "Natural Resources" value, then create a separate "Parks Total Expenditure" column
# The "re':" in the index argument of the first line is the end of the "Parks Total Expenditure" key
# I realize that I might have been able to do that with the "Financial Aid" column, but oh well
df["Parks Total Expenditure"] = df["Natural Resources"].apply(lambda x : int(x[x.index("re':")+5:-2]))
df["Natural Resources"] = df["Natural Resources"].apply(lambda x : int(x[x.index(":")+2:x.index(",")]))

# For transportation, there's an embedded dictionary, but only one number still.
# I will just need to extract that number
df["Transportation"] = df["Transportation"].apply(lambda x : int(x[x.index("re':")+5:-2]))

# Lastly, for some reason, a new column named "index" was added at some point.
# Getting rid of that should be the final touch.
df = df[df.columns[1:]]

# That's all folks
# Now, I will export the DataFrame into a .csv so that we can continue with the project.
print(df.info())
print(df.head())
df.to_csv("data/finance.csv")

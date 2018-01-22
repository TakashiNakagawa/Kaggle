#%%
#%matplotlib inline
import pandas as pd
pd.read_csv("./train.csv")
pd.read_csv("./test.csv")

#%%
import os
print(os.getcwd())
print(os.listdir("./"))

#%%
df= pd.read_csv("train.csv").replace("male",0).replace("female",1)
df["Age"].fillna(df.Age.median(), inplace=True)

#%%
import matplotlib.pyplot as plt
split_data = []
for survived in [0, 1]:
    split_data.append(df[df.Survived==survived])
    
temp = [i["Pclass"].dropna() for i in split_data] #df.dropna()は欠損値のある行を除く
plt.hist(temp, histtype="barstacked", bins=3)


#%%
temp = [i["Age"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=16)


#%%
df.columns

#%%
df["FamiliySize"] = df["SibSp"] + df["Parch"] + 1
df2 = df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], axis=1)
print(df2)
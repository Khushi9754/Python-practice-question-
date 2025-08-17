import pandas as pd
data={
    "Name":["khushi","palak","nidhi","kanak","varsha","yogita","monika","mona"],
    "Age":[22,23,25,28,29,49,54,39],
    "Salary":[1000,2000,3000,None,4000,5000,6000,7000],
    "Performance":[92,85,40,25,67,48,90,95]
}
df=pd.DataFrame(data)
print(df)
print("salary more than 4000")


#print(df[(df["win_by_runs"]>15) & (df["season"]>2015)])
print("salary more than 4000")
print(df[ df["Salary"] > 4000 ])

print("salary more than 4000 AND OTHER CONDITION")
print(df[ (df["Salary"]>4000) & (df["Age"]>25) ])

print("to add new col at last")
df["New_col"]=df["Salary"]+10
print(df)

print("add new col at specific index")
df.insert(0,"ID",[1,2,3,4,5,6,7,8])
print(df)

print("add new col at specific index")
df.loc[3,"New_col"]=1090
print(df)

print("modify col")
df["Salary"]=df["Salary"]*100
print(df)

print("drop any one col")
df.drop(columns=["New_col"],inplace=True)
print(df)

print("drop multiple col")
df.drop(columns=["ID","Performance"],inplace=True)
print(df)

#print("drop NaN values rows(axis=0 by default) or col(axis=1)")
#print("it is for row")
df.dropna(inplace=True)
print(df)

#print("drop NaN values rows(axis=0) or col(axis=1)")
#print("it is for col")
df.dropna(axis=1,inplace=True)
print(df)

print("see how many NaN values are present")
print(df.isnull().sum())

print("ye wo rows dega jisme NaN values hogi")
see=df.isnull().any(axis=1)
#any me wo dekhega row wise ki har col me null value hai kya hiogi to wo row de dega
print(df[see])

print("fill karna NaN values ")
#df.fillna(value,inplace=True/False)
df.fillna(0,inplace=True)
print(df)

print("fillna with condittion")
data={
    "Name":["khushi","palak","nidhi","kanak","varsha","yogita","monika","mona",None],
    "Age":[22,23,25,28,29,49,54,39,None],
    "Salary":[1000,2000,3000,None,4000,5000,6000,7000,None],
    "Performance":[92,85,40,25,67,48,90,95,None]
}
df=pd.DataFrame(data)
#ab ye isme sb jgah int value bharega name me bhi
df.fillna(df["Salary"].mean(),inplace=True)
print(df)

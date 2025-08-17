import pandas as pd
data={
    "Name":["khushi","palak","kanak","nidhi","pooja"],
    "Age":[22,23,25,26,20],
    "Salary":[20000,30000,10000,40000,None],
    "Performance":[56,37,28,None,48]
}
df=pd.DataFrame(data)
print(df)
data1=df.describe()
print(data1)
df.insert(2,"Roll_no",[12,23,25,26,23])
print(df)

#to update the specific value
df.loc[3,"Performance"]=56
print(df)

#it is just update the salary col
#it does not work for nan value as it gives error
df["Age"]=df["Age"]*10
print(df)

df.drop(columns=["Roll_no"],inplace=True)
print(df)

df.drop(columns=["Performance","Salary"],inplace=True)
print(df)
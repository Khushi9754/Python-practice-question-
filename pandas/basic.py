import pandas as pd

df=pd.Series([1,2,3,4,5])
#print(df)

data={
    "Name":["khushi","palak","nidhi","kanak"],
    "Age":[22,21,29,24]
}
df1=pd.DataFrame(data)
print(df1)

#Q1.Upar banaye DataFrame ke first 3 rows print karo.
#Q2.DataFrame ka size (rows x columns) aur column types print karo.
#"Q3.Age" column ka mean aur maximum value nikal kar print karo.

print(df1.head(3))
print(df1.info())
print(df1.describe())

#Q4.DataFrame me sirf "Name" column select karo.
#Q5.First 2 rows aur "Name" column select karo.
#Q6.Wo rows select karo jahan "Age" 25 se zyada ho.

print(df1["Name"])
print(df1.iloc[0:2,0])
print(df1[df1["Age"]>25])

#Ek new DataFrame create karo jisme kuch "Age" aur "Salary" missing (NaN) ho.
#"Salary" ke missing values ko alag-alag columns ke liye alag value se fill karo:
#"Salary" → 50000
#"Bonus" → 5000

#"Department" column ke missing values ko mode (sabse common value) se fill karo.
#Sirf un rows ko select karo jahan "Salary" missing nahi hai.

data1={
    "Name":["khushi","palak","nidhi","kanak"],
    "Age":[22,None,29,None],
    "Salary":[2000,3000,None,None]
}
df2=pd.DataFrame(data1)
print(df2)

df2["Bonus"]=[20,None,30,None]
df2.fillna({"Salary":50000,"Bonus":5000},inplace=True)
print(df2)

df2["Depart"]=["IT","cs","cs",None]
df2.fillna({"Depart":"cs"},inplace=True)
print(df2)

print(df2[df2["Salary"].notnull()])
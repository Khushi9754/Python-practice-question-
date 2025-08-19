import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Khushi', 'Raj', 'Meera'],
    'Age': [20, 21, 19, 22, 20],
    'City': ['Delhi', 'Mumbai', 'Indore', 'Pune', 'Delhi'],
    'Marks': [85, 90, 75, 95, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#Select Name and City of all students whose Age > 20.
#Select the Marks of students from Delhi only.
#Get the details (Name, Marks) of students whose Marks ≥ 85 and Age ≤ 20.
#Update the Marks of Khushi to 92 using .loc.
#Select the last 3 rows but only the columns Name and Age

print(df.loc[df["Age"]>20,["Name","City"]])
print(df.loc[df["City"]=="Delhi","Marks"])
print(df.loc[(df["Age"]<=20) & (df["Marks"]>=85),["Name","Marks"]])
df.loc[df["Name"]=="Khushi","Marks"]=92
print(df)
print(df.loc[:,["Name","Age"]].tail(3))


#Select only the Name column of students from "Mumbai".
#Select Age and Marks of the student whose Name is "Aman".
#Select the first 2 rows with columns Name and Age.

#Select all rows where Marks < 50 and show only Name and City.

#Update the City of "Ravi" to "Bangalore".
#Increase Marks by 5 for students whose Age < 18.

#Select rows where City is either "Delhi" or "Indore", but only show Name and Marks.
#Update Age to 25 for all students whose Marks ≥ 90.
data = {
    "Name": ["Aman", "Khushi", "Ravi", "Neha", "Sanya", "Arjun", "Meera", "Kunal"],
    "Age": [19, 21, 20, 22, 18, 23, 17, 20],
    "City": ["Delhi", "Mumbai", "Indore", "Delhi", "Pune", "Bangalore", "Indore", "Delhi"],
    "Marks": [88, 76, 92, 67, 45, 81, 95, 59],
    "Department": ["CS", "IT", "CS", "ECE", "ME", "IT", "CS", "ECE"]
}
df = pd.DataFrame(data)
#print(df)

print(df.loc[df["City"]=="Mumbai","Name"])
print(df.loc[df["Name"]=="Aman",["Age","Marks"]])
print(df.loc[:,["Name","Age"]].head(2))
print(df.loc[df["Marks"]<50,["Name","City"]])
df.loc[df["Name"]=="Ravi","City"]="Bangalore"
print(df)
df.loc[df["Age"]<18,"Marks"]=df.loc[df["Age"]<18,"Marks"]+5
print(df.loc[df["Age"]<18,["Name","Age","Marks","City"]])

print(df.loc[(df["City"]=="Delhi") | (df["City"]=="Indore"),["Name","Marks"]])
df.loc[df["Marks"]>=90,"Age"]=25
print(df)

#Select every alternate row’s Name and Marks.
#Select rows where Marks is between 70 and 90 (inclusive).
#Update Marks to 100 for all students whose City = "Delhi" and Age < 21.
#Select the last 2 rows with only Name, City, and Marks.
#Replace NaN values in City with "Unknown" using .loc.
#Swap Marks of the first and last student using .loc.

print(df.loc[::2,["Name","Marks"]])
print(df.loc[(df["Marks"]>=70) & (df["Marks"]<=90),:])
df.loc[(df["City"]=="Delhi") & (df["Age"]<21),"Marks"]=100
print(df)
print(df.loc[:,["Name","Marks","City"]].tail(2))

import numpy as np

data1 = {
    "Name": ["Aman", "Khushi", "Ravi", "Neha", "Sanya", "Arjun", "Meera", "Kunal"],
    "Age": [19, 21, 20, 22, 18, np.nan, 17, 20],
    "City": ["Delhi", "Mumbai", np.nan, "Delhi", "Pune", "Bangalore", "Indore", "Delhi"],
    "Marks": [88, 76, 92, np.nan, 45, 81, 95, np.nan],
    "Department": ["CS", "IT", "CS", "ECE", "ME", "IT", np.nan, "ECE"]
}
df1 = pd.DataFrame(data1)
#print(df)
df1.loc[df1["City"].isna(),"City"]="Unknown"
print(df1)
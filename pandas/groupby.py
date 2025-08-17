#Find the average salary of employees in each department.
#Count the number of employees in each department.
#Find the maximum salary in each department.
#Find the minimum experience in each department.
#Calculate the average salary by gender.
#Find the sum of salaries in each department.
#Find the department with the highest average experience.

import pandas as pd

data = {
    "Employee": ["Amit", "Neha", "Raj", "Simran", "Karan", "Priya", "Arjun", "Meera", "Rohit", "Anjali"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [40000, 55000, 48000, 60000, 42000, 65000, 50000, 41000, 62000, 52000],
    "Experience": [2, 5, 3, 7, 4, 8, 6, 2, 9, 5],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)
print(df)

group1=df.groupby("Department")["Salary"].mean()
print(group1)

group2=df.groupby("Department")["Employee"].count()
print(group2)

group3=df.groupby("Department")["Salary"].max()
print(group3)

group4=df.groupby("Department")["Experience"].min()
print(group4)

group5=df.groupby("Gender")["Salary"].mean()
print(group5)

group6=df.groupby("Department")["Salary"].sum()
print(group6)

group7=df.groupby("Department")["Experience"].mean().max()
print(group7)

#Group employees by department and gender → count employees in each group.
#Find the highest salary for each gender in each department.
#Calculate both mean salary and mean experience for each department.

group8=df.groupby(["Department","Gender"]).count()
print(group8)

group9=df.groupby(["Department","Gender"])["Salary"].max()
print(group9)

group10=df.groupby("Department")[["Salary","Experience"]].mean()
print(group10)

#Find the top 2 highest salaries in each department.
#Q12.For each department, find the total salary of Male employees and Female employees separately.
#Q14.For each department, calculate minimum, maximum, and average salary in one go (use .agg).
#Q15.Find which department has the highest number of employees.

mark=df.sort_values("Salary",ascending=False)
group11=mark.groupby("Department").head(2)
print(group11)

group12=df.groupby(["Department","Gender"])["Salary"].sum()
print(group12)

group14=df.groupby("Department").describe()
print(group14)

group15=df.groupby("Department")["Employee"].count()
maxi=group15.idxmax()
print(maxi)

#Q16.For each gender, find the average experience across departments.
#Q17.Find the ratio of Male to Female employees in each department.

group16=df.groupby(["Department","Gender"])["Experience"].mean()
print(group16)

group17=df.groupby(["Department","Gender"])["Gender"].count()
print(group17)

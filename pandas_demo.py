import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\khushi pawar\Untitled Folder\matches.csv")
#print(df)
#Show all the column names and their data types.
print(df.info())

#Select only the team1, team2, and winner columns.
print(df[["team1","team2","winner"]])

#Filter matches where city is "Mumbai".
mark=df["city"]=="Mumbai"
print(df[mark])

#Find all matches where dl_applied is 1.
mark=df["dl_applied"]==1
print(df[mark])

#Count how many matches each team has won.
mark=df["winner"].value_counts()
print(mark)

#Get the top 5 players who have the most player_of_match awards.
mark=df["player_of_match"].value_counts().head()
print(mark)

#Find matches where win_by_runs is greater than 50.
mark=df["win_by_runs"]>50
print(df[mark])

mark1=df["win_by_wickets"]>7
print(df[mark1])

#mark1=df["team1"].value_counts()
#mark2=df["team2"].value_counts()
#mark3=mark1+mark2
#print(mark3.sort_values())
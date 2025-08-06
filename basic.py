person1=int(input("enter age:"))
person2=int(input("enter age:"))
person3=int(input("enter age3:"))
if person1>person2:
    if person1>person3:
        print(person1,"is the oldest")
    else:
        print(person3,"is the oldest")
else:
    if person2>person3:
        print(person2,"is the oldest")
    else:
        print(person3,"is the oldest")
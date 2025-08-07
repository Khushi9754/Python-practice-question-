
#Write a lambda to add 10 to a number.
a=lambda x:x+10
print(a(5))

#Write a lambda to multiply two numbers.
b=lambda x,y:x*y
print(b(5,2))

#Create a lambda that returns the square of a number.
c=lambda x:x*x
print(c(5))

#Use lambda to check if a number is even.
d=lambda x:"even" if x%2==0 else "odd"
print(d(5))

#Use lambda with map() to square all numbers in a list.
li=[1,2,3,4,5]
e=list(map(lambda x:x*x,li))
print(e)

#Use lambda with filter() to get only odd numbers from a list.
li=[1,2,3,4,5]
f=list(filter(lambda x:x%2!=0,li))
print(f)

#Write a lambda that returns the maximum of two numbers.
max=lambda x,y:x if x>y else y
print(max(70,8))

#Use lambda to check if a string starts with a vowel.
vowel=lambda x:x[0] in "aeiou"
print(vowel("khushu"))

#Write a lambda function that returns the length of a string.
le=lambda x:len(x)
print(le("khushi"))

#Use lambda to get the last character of a string
last=lambda x:x[-1]
print(last("khushi"))

#Sort a list of tuples based on the second element using lambda.
#data = [(1, 3), (2, 1), (4, 2)]
data = [(1, 3), (2, 1), (4, 2)]
data=sorted(data,key=lambda x:x[1])
print(data)

#Use map() and lambda to convert a list of strings to uppercase.
words = ['apple', 'banana', 'kiwi']
upper=list(map(lambda x:x.upper(),words))
print(upper)

#Sort a list of strings by their length using a lambda.
words = ['apple', 'banana', 'kiwi']
word=sorted(words,key=lambda x:len(x))
print(word)

#Use filter() and lambda to get all strings that are palindromes.
words = ['apple', 'banana', 'kiwi','madam']
pali=list(filter(lambda x:x[:]==x[::-1],words))
print(pali)

#Use lambda with reduce() to find the product of all numbers in a list.
import functools
li=[1,2,3,4,5]
a=functools.reduce(lambda x,y:x+y,li)
print(a)

#Write a lambda that returns the cube of a number if it’s odd, else the square.
depend=lambda x:x*x*x if x%2!=0 else x*x
print(depend(6))

#Create a lambda that checks if a year is a leap year.
year=lambda x:"leap" if (x%4==0 and (x%100!=0 or x%400!=0)) else "not leap"
print(year(1900))

#Use lambda to extract domain names from a list of email addresses.
#emails = ['john@example.com', 'alice@gmail.com']
emails = ['john@example.com', 'alice@gmail.com']
domain=list(map(lambda x:x.split("@")[1],emails))
print(domain)

#Use lambda with map() to reverse every string in a list.
words = ['apple', 'banana', 'kiwi']
rev=list(map(lambda x:x[::-1],words))
print(rev)

#Filter out all negative numbers from a list using lambda.
num=[2,3,6,-1,2,-3,2]
remove=list(filter(lambda x:x>0,num))
print(remove)

#Given a list of dictionaries, sort by a key using lambda.
#people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20},{'name': 'Charlie', 'age': 30}]
people = [
  {'name': 'Alice', 'age': 25},
  {'name': 'Bob', 'age': 20},
  {'name': 'Charlie', 'age': 30}
]

arrange=sorted(people,key=lambda x:x['age'])
print(arrange)

#Write a lambda to extract the first digit of a number.
first=lambda x:int(str(x)[0])
print(first(764217))

#Write a Python program using list comprehension to create a new list that contains the square of each number in the original list.
li=[1,2,3,4,5]
sqaure=[i*i for i in li]
print(sqaure)

#Use lambda in a list comprehension to double only even numbers.
li=[1,2,3,4,5]
do_even=[(lambda x:x*x)(i) for i in li if i%2==0]
print(do_even)
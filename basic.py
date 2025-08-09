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
        
#Write a program that will convert celsius value to fahrenheit
cel=int(input("enter the temp"))
frah=cel * (9/5) + 32
print(frah)

#User will input (2numbers).Write a program to swap the numbers
one=int(input("enter no1:"))
two=int(input("enter no2:"))      
one,two=two,one
print(one)
print(two)

#Write a program that will give you the sum of 3 digits
num=(input("enter number:"))
k=0
for i in num:
  no=int(i)
  k=k+no
print("the sum of ",num,"is",k)

#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
num=int(input("enter the no"))
original=num
a=num%10
num=num//10

b=num%10
num=num//10

c=num%10
d=num//10

rev=a*1000+b*100+c*10+d
print(rev)
if rev==original:
  print(True)
else:
  print(False)

#Write a program that will tell whether the number entered by the user is odd or even.
num=int(input("enetr the num"))
if num%2==0:
  print("even")
else:
  print("odd")


#Write a program that will tell whether the given year is a leap year or not.
year=int(input("enter year:"))
if year%4==0 and (year%100!=0) or (year%400==0):
  print("leap year")
else:
  print("not a leap year")

#Write a program to find the euclidean distance between two coordinates.
# (x 2 − x 1 ) 2 + ( y 2 − y 1 ) 2
import math
x1=int(input("enetr the num x1:"))
x2=int(input("enetr the num x2:"))
y1=int(input("enetr the num y1:"))
y2=int(input("enetr the num y2:"))
dis=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(dis)

#Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
x1=int(input("enetr the angle 1:"))
x2=int(input("enetr the angle 2:"))
x3=int(input("enetr the angle 3:"))
if (x1+x2+x3)==180:
  print("it is a triangle")
else:
  print("it not a triangle")

#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
x1=int(input("enetr the num cost:"))
x2=int(input("enetr the num selling:"))
if x1<x2:
  print("it is a profit")
else:
  print("it is a loss")

#Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
principle=int(input("enter the principle value"))
rate=int(input("enter the rate "))
intrest=int(input("enter the intrest"))
S_I=((principle*rate*intrest)/100)
print("simple intrest is",S_I)

#Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math
r=int(input("enter the radius"))
h=int(input("enter the height"))
vol=(math.pi*(r**2)*h)
num=vol/1000
cost=40*num  
print("volume of cylinder is",vol)
print("cost of milk is",cost)

#Write  a program that will tell whether the given number is divisible by 3 & 6.
num=int(input("enter the num:"))
if num%3==0 and num%6==0:
  print("divisible by 3 and 6")
else:
  print("not divisible by 3 and 6")

#Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.
time=input("enter the time")
a,b= time.split(':')
hour,min=int(a),int(b)
if hour>=12:
  hour-=12
elif hour==0 and min==0:
  hour=12
min=min*6
hour=(hour*30)+min*0.5
diff=hour-min
print("angle between hour and min is",abs(diff))

#Write a program that will determine weather when the value of temperature and humidity is provided by the user.
#TEMPERATURE(C)      HUMIDITY(%)      WEATHER
#>= 30                 >=90           Hot and Humid
#>= 30                 < 90            Hot
#<30                   >= 90          Cool and Humid
#<30                   <90            Cool
temp=int(input("enter the temp:"))
hum=int(input("enter the humidity:"))
if temp>=30 and hum>=90:
  print("hot and humid")
elif temp>=30 and hum<90:
  print("hot")
elif temp<30 and hum>=90:
  print("cool and humid")
elif temp<30 and hum<90:
  print("cool")

#Write a program that will take three digits from the user and add the square of each digit.
num=input("enter the number:")
k=0
for i in num:
  k=k+(int(i)**2)
print("the sqaure of number is",k)

#Write a program that will check whether the number is armstrong number or not.
num=(input("enetr the number:"))
k=0
le=len(num)
for i in num:
  k=k+(int(i)**le)
if k==int(num):
  print("armstrong num..")
else:
  print("not a armstrong num..")

#Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
choice=int(input("Menu:\n1.cm to ft\n2.km to miles\n3.usd to inr\n4.exit\nenter choice:"))
#print(choice)
if choice==1:
  cm=int(input("enter cm"))
  ft=cm/30.48
  print(cm,"cm","to",ft,"ft")
elif choice==2:
  km=int(input("enter km"))
  miles=km/1.609344
  print(km,"km","to",miles,"miles")
elif choice==3:
  usd=int(input("enter usd"))
  inr=usd*82.50
  print(usd,"usd","to",inr,"inr")
elif choice==4:
  print("exit")

#Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.
n=int(input('enter the num'))
k=0
for i in range(1,n+1):
  k+=i
print("the sum of ",n,"is",k)

#Write a program that can multiply 2 numbers provided by the user without using the * operator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
result = 0
for i in range(b):
    result += a
print("Multiply is", result)

#Write a program that can find the factorial of a given number provided by the user.
n=int(input('enter the num'))
k=1
for i in range(1,n+1):
  k=k*i
print("the factorial of ",n,"is",k)


#Write a program to print the first 25 odd numbers
k=0
num=1
while k<25:
  if num%2!=0:
    print("odd numbers",num)
    k +=1
  num+=1


#Write a program to print whether a given number is prime number or not
num = int(input("Enter number:"))
if num <= 1:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")


#Print all the armstrong numbers in the range of 100 to 1000
for i in range(100,1001):
  k=0
  le=len(str(i))
  for j in str(i):
    k=k+(int(j)**le)
  if k==i:
    print(i,"is a armstrong num",k)
  else:
     print(i,"is not a armstrong num",k)


#The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
#10th year - 10000
#9th year - 9000
#8th year - 8100 and so on

rate=1.1      
current_popu=10000
print("10th year population is",current_popu)
#year=int(input("enter the years:"))
for i in range(9,0,-1):
   current_popu=current_popu/rate
   print(i,"th year populationi",int(current_popu))


#Write a program to print all the unique combinations of 1,2,3 and 4
count=0
for i in range(1,5):
  for j in range(1,5):
    for k in range(1,5):
      for m in range(1,5):
        if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
          print(i,j,k,m)
          count+=1
print(count)

#User will provide 2 numbers you have to find the HCF of those 2 numbers
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if num1<num2:
  small=num1
else:
  small=num2
for i in range(1,small+1):
  if num1%i==0 and num2%i==0:
   hcf=i
print("the hcf of",num1,"and",num2,"is",hcf)

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
num=int(input("enter the number:"))
if num==1:
  print("the vlue is ",1)
else:
  count=num+(num*11)+(num*111)
  print("the value is",count)

#Take a number from the user and find the number of digits in it. 
num=input("enter the num:")
count=0
for i in num:
  count+=1
print(count)

#Print all factors of a given number provided by the user.
num=int(input("enter the num:"))
print("factor of ",num,"is")
for i in range(1,num+1):
  if num%i==0:
   print(i)

#Find the reverse of a number provided by the user(any number of digit) 
num=input("enter the num:")
rev=num[::-1]
print("the reverse is ",rev)

#Write a program to print the following pattern
#*
#**
#***
#****
#*****

num=int(input("enter the num"))
for i in range(1,num+1):
  for j in range(0,i):
    print("*",end="")
  print("")
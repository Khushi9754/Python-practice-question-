#Write a function to add two numbers
def add(x,y):
    str_add=x+y
    return str_add
print(add(5,9))

#Write a function to subtract two numbers.
def subtrat(x,y):
    str_minus=x-y
    return str_minus
print(subtrat(5,9))

#Write a function to multiply two numbers.
def multiply(x,y):
    str_multiply=x*y
    return str_multiply
print(multiply(5,9))

#Write a function to divide two numbers.
def divide(x,y):
    str_divide=x/y
    return int(str_divide)
print(divide(45,5))


#Write a function to return the square of a number.
def sqaure(n):
    double=n*n
    return double
print(sqaure(5))

#Write a function to return the cube of a number.
def cube(n):
    triple=n*n*n
    return triple
print(cube(5))

#Write a function to check if a number is even.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(5))

#Write a function to check if a number is odd.
def is_odd(n):
    if n%2!=0:
        return True
    else:
        return False
print(is_odd(5))

#Write a function to return the larger of two numbers.
def large(a,b):
    if a>b:
        return a
    else:
        return b
print(large(4,7))

#Write a function to return the smaller of two numbers.
def small(a,b):
    if a<b:
        return a
    else:
        return b
print(small(4,7))

#Write a function to find the maximum of three numbers
def large_three(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
    return max(a,b,c)
print(large_three(47,2,55))

#Write a function that takes a string and returns its length.
def length(s):
    return len(s)
print(length("khushi"))

#Write a function that prints a welcome message with a name
def welcome(s):
    return "welcome "+ s
print(welcome("khushi"))

#Write a function to check if a string is a palindrome.
def palindrome(s):
    low=s.lower()
    if low==low[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

print(palindrome("123"))

#Write a function that counts vowels in a string.
def vowel(s):
    vowels="aeiou"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
print(vowel("khushi"))

#Write a function that counts consonants in a string.
def consonant(s):
    vowels="aeiou"
    count=0
    for i in s:
        if i not in vowels:
            count+=1
    return count
print(consonant("khushi"))

#Write a function that capitalizes the first letter of each word.
def capi(s):
    return s.capitalize()

print(capi("ahushi"))

#Write a function to find duplicates from a list.
def duplicate(li):
    dup=[]
    for i in li:
        if  li.count(i)>1 and i not in dup:
            dup.append(i)
    
    return li
li=[1,2,1,2,3,4]
print(duplicate(li))

#Write a function to remove duplicates from a list.
def dupli(s):
    a=list(set(s))
    return a
li=[1,2,1,2,3,4]
print(dupli(li))

#Write a function to remove duplicates from a list.
def remove_dup(li):
    result=[]
    for i in li:
        if i not in result:
            result.append(i)
    return result
li=[1,2,1,2,3,4]
print(remove_dup(li))

#Write a function to return the sum of all elements in a list.
def sum_list(li):
    a=sum(li)
    return a
li=[1,2,3,4,5]
print(sum_list(li))

#Write a function to return the average of numbers in a list.
def average(li):
    count=0
    for i in li:
        count=count+i
    a=count/len(li)
    return int(a)
li=[1,2,3,4,5]
print(average(li))

#Write a function that takes a list and returns only even numbers.
def only_even(li):
    even=[]
    for i in li:
        if i%2==0:
            even.append(i)

    return even
li=[1,2,3,4,5]
print(only_even(li))

#Write a function that takes a list and returns only odd numbers.
def only_odd(li):
    odd=[]
    for i in li:
        if i%2!=0:
            odd.append(i)

    return odd
li=[1,2,3,4,5]
print(only_odd(li))

#Write a function that checks if an element exists in a list.
def exist(n,li):
    if n in li:
        return f"{n} exist in list"
    else:
        return f"{n} not exist in list"

li=[1,2,3,4,5]
print(exist(4,li))

#Write a function to find the second largest number in a list.
def sec_large(li):
    a=sorted(li,reverse=True)
    return a[1]
li=[1,23,3,43,5]
print(sec_large(li))

#Write a function to return the maximum and minimum of a list.
def max_or_min(li):
    a=max(li)
    b=min(li)
    return a,b
li=[1,23,3,4,5]
print(max_or_min(li))

#Write a function that counts the frequency of each element in a list.
def freq(li):
    count={}
    for i in li:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

    for key in count:
        print(key,count[key])

li=[1,23,3,3,4,5]
print(freq(li))

#Write a function to find the factorial of a number (using loop).
def fac(n):
    count=1
    for i in range(1,n+1):
        count=count*i
    return count
print(fac(5))

#Write a function to generate Fibonacci series up to n terms..
def fibo(n):
    first=0
    second=1
    print(first)
    print(second)
    for i in range(1,n-1):
        third=first+second
        first=second
        second=third
        print(third)
print(fibo(12))

#Write a function to check if a number is prime.
def is_prime(n):
    if n<=2:
        print("it is prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print("not prime")
                return
        print("prime")

print(is_prime(7))

#Write a function to return the sum of digits of a number.
def add_all(n):
    a=str(n)
    count=0
    for i in a:
        count=count+int(i)
    return count
print(add_all(15345))

#Write a function to reverse a number.
def rev_num(n):
    a=str(n)
    return a[::-1]
print(rev_num(153))

#Write a function to check if a number is a palindrome.
def num_pal(n):

        a=str(n)
        if a[:]==a[::-1]:
            print("pali")
        else:
            print("not pali")

print(num_pal(153))


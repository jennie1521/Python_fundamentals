#Print "Hello, World!"
print("Hello, World")

#Take your name as input and print
greet  =input("Enter ur name:");
print("Hello", greet)

#3.Take two numbers and print their sum.
number1 = int(input("Enter your no 1:",));
number2 = int(input("enter your no 2:"));
sum=number1+number2
print(sum)

#4.Find the area of a rectangle.
length=float(input("enter 1st side of rentangle:"));
breadth=float(input("enter 2nd side of rectangle:"));
area_of_rect=length*breadth
print(area_of_rect)

#5.Find the area of a circle.
r=int(input("enter the radius of circle:"));
area_of_circle=3.14*r**2
print(area_of_circle)

#6.Convert Celsius to Fahrenheit.
c=float(input("enter the temp in celcius:"));
f=(9/5)*c+32
print("Temp in fahrenheit:",f)

#7: Swap Two Numbers Using a Third Variable
a=int(input("enter number a:"));
b=int(input("enter number b:"));
temp=a;
a=b;
b=temp;
print(a,b)

#8: Swap Two Numbers (Without Using a Third Variable)
c=30;
d=50;
c,d=d,c
print(c,d)

#9.Calculate simple interest.
amount=int(input("enter the amount:"));
year=int(input("enter the no of years:"));
rate=int(input("enter the rate:"));
simple_interest= (amount*year*rate)/100
print(simple_interest)

#10.Calculate the average of three numbers.
num1=int(input("enter num 1:"));
num2=int(input("enter num 2:"));
num3=int(input("enter num 3:"));
avg=(num1+num2+num3)/3
print(avg)

# check whether a number is even or odd
def check_even_odd(num):
    if num%2==0:
        print("This is Even number")
    else:
        print("This is odd number")
check_even_odd(31);
check_even_odd(8);
check_even_odd(101);

#find largest of two numbers
def find_largest(a,b):
    if a>b:
        print(a)
    else:
        print(b)
find_largest(20,30); 
find_largest(5,98); 
find_largest(1007,10020);

#find the smallest of three numbers
def find_smallest(a,b,c):
    if a<b and a<c:
        print(a, "is smaller")
    elif b<a and b<c:
        print(b, "is smaller")
    elif c<a and c<b:
        print(c,"is smaller")
find_smallest(20,30,15);
find_smallest(790,80,105);
find_smallest(26,3,10);

#check whether a number is positive, negative, zero
def check_number(num):
    if num>0:
        print("This is Positive number ")
    elif num<0:
        print("This is negative number ")
    else:
        print("This is Zero")
check_number(33);
check_number(-30);
check_number(0);

#check whether a year is leap or not
def check_leap_or_not(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,"year is leap")
    else:
        print(year,"year is not leap")
check_leap_or_not(1800);
check_leap_or_not(1600);
check_leap_or_not(2024);

#check whether a number is divisible by both 5 and 11
def check_div_by5and11(num):
    if num%5==0 and num%11==0:
        print("Divisible by both")
    else:
        print("not divisible")
check_div_by5and11(55);
check_div_by5and11(10);
check_div_by5and11(22);

#check a character is vowel or consonant
def vowel_or_consonant(char):
    if len(char)==1 and char.isalpha():
        if char.lower() in 'aeiou':
            print(char,"is vowel")
        elif char not in "aeiou":
            print(char,"is consonant")
    else:
        print("invalid")
vowel_or_consonant('g');
vowel_or_consonant('u');
vowel_or_consonant('A');

#find the square and cube of number
number=int(input("enter the number:"))
square=number*number
cube=square*number
print("the square of",number,"is",square,"and the cube is", cube)


#check whether a person is eligible to vote
def check_vote_eligible(age):
    if age >= 18:
        print("eligible")
    else:
        print("not eligible")
check_vote_eligible(20);
check_vote_eligible(10);
check_vote_eligible(18);

#find grades based on marks
def grades(marks):
    if marks >= 90:
        print("Grade A")
    elif marks<90 and marks>=75:
        print("Grade B")
    elif marks<75 and marks>=45:
        print("Grade C")
    elif marks<45:
        print("Fail")
grades(78);
grades(95);
grades(30);

# find if a number is 2 digit number
def is_two_digit_num(num):
    if num>=10 and num<=99:
        print("This is two digit number")
    else:
        print("Not a two digit number")
is_two_digit_num(0);
is_two_digit_num(56);
is_two_digit_num(100);

#find whether a charcter is uppercase or lowercase
def check_case(char):
    if len(char)==1 and char.isalpha():
        if char.islower():
            print("Lowercase character")
        elif char.isupper():
            print("Uppercase character")
check_case('A');
check_case('f');
check_case('Z');

# for loop
for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(50,0,-1):
    print(i)

#1-100 odd numbers
for i in range(1,101):
    if i%2!=0:
        print(i) 
#even numbers
for i in range(1,101,2):
    print(i) 

#sum of n natural numbers
sum=0
n=10
for i in range(n+1):
    sum=sum+i
print(sum)

#factorial
fact=1
n=5
for i in range(2,n+1):
    fact=fact*i
print(fact)

#perform operations
def numbers(a,b):
    sum=a+b
    print(sum)

    subtract=a-b
    print(subtract)

    multiply=a*b
    print(multiply)

    division=a/b
    print(division)

    reminder=a%b
    print(reminder)

    power=a**b
    print(power)

numbers(20,3);

#check whether two numbers are equal
def chcek_equal(a,b):
    if a==b:
        print("Equal")
    else:
        print("Not Equal")
chcek_equal(20,20);
chcek_equal(40,30);  

#count number of vowels
text="I am Janvi Yadav"
count=0
for char in text.lower():
    if char in 'aeiou':
        count+=1
print(count)

#count number of consonant
text="I am Janvi Yadav"
count=0
for char in text.lower():
    if char not in 'aeiou':
        count+=1
print(count) 

#reverse a string 
str="Hey, how much is this."
print(str[::-1]) 

#check whether a string is palindrome
str="appa"
str1=str[::-1]
if str==str1:
    print("This is palindrome")

#count spaces in a string
str="Janvi is beautiful girl in her family."
print(str.count(" "))

#count digits in a string
text="My mane is janvi kundan yadav and my age is 21."
count=0
for ch in text:
    if ch.isdigit():
        count+=1
print(count)

#count uppercase letters
text="My mane is Janvi Kundan Yadav and my age is 21."
count=0
for ch in text:
    if ch.isupper():
        count+=1
print(count)

#count lowercase letters
text="My mane is Janvi Kundan Yadav and my age is 21."
count=0
for ch in text:
    if ch.islower():
        count+=1
print(count)

#remove all spaces
text="My mane is Janvi Kundan Yadav and my age is 21."
print(text.replace(" ",""))

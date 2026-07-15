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

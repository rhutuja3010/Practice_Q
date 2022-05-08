# Write a python program to input any character andcheck whether it is alphabet, digit or specialcharacter.
# s=input("enter the alphabet , digit or special_chr  :")
# if (s>="a" and s<="z") or (s>="A" and s<="Z"):
#     print("this is alphabet")
# elif (s>='0' and s<='9'):
#     print("this is digit")
# else:
#     print("this is special_chr") 


# .Write a python program to check whether a characteris uppercase or lowercase alphabet.
# alphabet=input("enter the alphabet :")
# if  alphabet>="a" and  alphabet<="z":
#     print("this is lower_case character")
# else:
#     print("this is upper_case character")

# Write a python program to input week number and printweek day
# day=input("enter the day  :")
# if day=="1":
#     print("sunday")
# elif day=="2":
#     print("monday")
# elif day=="3":
#     print("tuesday")
# elif day=="4":
#     print("wednesday")
# elif day=="5":
#     print("thusday")
# elif day=="6":
#     print("friday")
# elif day=="7":
#     print("saturday")
# else:
#     print("holyday")




# The given number is of one digited or two digitedor three digited or more than three digited.
# n=int(input("enter the number :"))
# if n>=0 and n<=9:
#     print("This is one digit number") 
# elif n>=10 and n<=99:
#     print("This is two digit number") 
# elif n>=100 and n<=999:
#     print("This is three digit number") 
# else:
#     print("this is more than 4 digit number")



# .The entered number is smallest 4 digit number ornot.
# number=int(input("enter the number :"))
# if number==1000:
#     print(" this number is smallest 4 digit number")
# else:
#     print(" this number is not smallest 4 digit number")


# Whether the triangle will be an obtuse-angle, ora right-angle or an acute-angle triangle.
# angle=int(input("enter the angle :"))
# if angle<90:
#     print(angle,":this is acute angle")
# elif angle==90:
#     print(angle,":this is right angle")
# elif angle<360:
#     print(angle,":this is obtuse angle")
# else:
#     print("this is not any angle")


# 54.Write a Python program to display the current dateand time.
# import datetime
# dt=datetime.datetime.today()
# print(dt)



# 51.Write a Python program to calculate the length ofa string.
# string=input("enter the string :")
# print(len(string))

# 53.Write a Python program to change a given string toa new string where the first and last chars havebeen exchanged.


# swap characters in string
# def swap(string):
#       return string[-1:] + string[1:-1] + string[:1]
#  # take string from user
# str1 = input("Please Enter String : ")
# print (swap(str1))


# string="rhutuja"
# s=string[-1:] + string[1:-1] + string[:1]
# print(s)

# string="rhutuja"
# for i in string:
#     s=string[-1] + string[1:-1] + string[0]
# print(s)

# s=(input("enter the string :"))
# # s="rhutuja"
# if type(s)==str:
#     print(s[-1] + s[1:-1] + s[0])
# else:
#     print("wrong")


# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# i=0
# l=[]
# for i in range(len(a)):
#     # print(a[i])
#     for j in range(len(b)):
#         print(b[-j])
        # l.append(a[i],b[j])
# print(l)
# for j in len(b):
# i=0
# l=[]
# k=0
# while i<len(a):
#     j=1
#     while j-1:
#         l.append(a[i],k[j])
#         if i==5:
#             break
#         j+=1
#     i+=1
# print(l)




#  Accept any city from the user and display the monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
# city_name=input("entre the city_name :")
# if city_name=="Delhi":
#     print("the monument of that city is Red Fort")
# elif city_name=="Agra":
#     print("the monument of that city is Taj Mahal")
# elif city_name=="Jaipur":
#     print("the monument of that city is Jal Mahal")
# else:
#     print("Temple")

# a=[28,[48,[10,5,[7,3],3,[5]],10]]
# print(a[1][1][2][1])


# a=[1,2,[5,[6,[7,0,3],7],],3,[6],4,5]
# print(a[2][1][2])


# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
# If age does not fall in any range then display the following message: “Enter appropriate age”
# Age
# Sex
# Wage/day
# >=18 and <30
# M
# 700
 
# F
# 750
# >=30 and <=40
# M
# 800
 
# F
# 850
# Accept three numbers from the user and display the second largest number.
# age=int(input("enetr the age :"))
# if age>=18 and age<30:
#     print("sex is female wages is 750 or sex is male wages is 700 ")
# elif age>=30 and age<=40:
#     print("sex is female wages is 850 or sex is male wages is 800 ")
# else:
#     print("Enter appropriate age")



# Accept three numbers from the user and display the second largest number.

# a=int(input("enter the 1st number :"))
# b=int(input("enter the 2nd number :"))
# c=int(input("enter the 3rd number :"))
# if (a>b and a<c) or (a<b and a>c) :
#     print(a,": is second largest")
# elif (b>a and b<c) or (b<a and b>c):
#     print(b,"is  second grater")
# else:
#     print(c,"is second grater")


# size=int(input("entre the size :"))
# a=[45,68,67,13]
# i=0
# rem=0
# sum=0
# f=0
# while i<len(a):
#     b=a[i]
#     rem=a[i]%10
#     f=a[i]//10
#     sum=f*10
#     i+=1
#     print(b,"=",sum,"+",rem)



#  Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days  : Rs 3/day.
# Ten to 15 days  : Rs 4/day
# After 15 days    : Rs 5/day

# day=int(input("enter the day :"))
# if day>=1 and day<=5:
#     print("the charge for library is 2.Rs")
# elif day>=6 and day<10:
#     print("the charge for library is 3.Rs")
# elif day>=10 and day<=15:
#     print("the charge for library is 4.Rs")
# else:
#     print("the charge for library is 5.Rs")


# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# i=1500
# while i<=2700:
#     if i%5==0 and i%7==0:
#         print(i)
#     i+=1
    # print(i)
# Write a python program to input angles of a triangle and check whether triangle is valid or not.

# angle1=int(input("enter the 1st angle :"))
# angle2=int(input("enter the 2nd angle :"))
# angle3=int(input("enter the 3rd angle :"))  
# total= angle1+angle2+angle3
# if total==180:
#     print("it is a triangle")
# else:
#     print("it is not traingle")


# Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.
# side1=int(input("enter the 1st side :"))
# side2=int(input("enter the 2nd side :"))
# side3=int(input("enter the 3rd side :"))
# if side1==side2==side3:
#     print("traingle is equilateral")
# elif side3==side2 or side3==side1 or side2==side1 or side2==side3 or side1==side2 or side1==side3:
#     print("traingle is isosceles")
# else:
#     print("traingle is scalene ")



# Write a python program to calculate profit or loss.
# selling_prise=int(input("enter the selling_prise :"))
# buy_prise=2000
# if selling_prise<buy_prise:
#     print("profit:",buy_prise-selling_prise)
# else:
#     print("loss:",selling_prise-buy_prise)


# Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the billunit

# unit=int(input("enter the units :"))
# if unit<=50:
#     count_unit=unit*0.50
#     discount=count_unit*20/100
#     total_bill=count_unit-discount
#     print("unit =",unit,"bill=",total_bill,"Rs")
# elif unit>50 or unit<100:
#     count_unit=unit*0.75
#     discount=count_unit*20/100
#     total_bill=count_unit+discount
#     print("unit =",unit,"bill=",total_bill,"Rs")
# elif unit>=100 or unit<250:
#     count_unit=unit*1.20
#     discount=count_unit*20/100
#     total_bill=count_unit+discount
#     print("unit =",unit,"bill=",total_bill,"Rs")
# elif unit>=250:
#     count_unit=unit*1.50
#     discount=count_unit*20/100
#     total_bill=count_unit+discount
#     print("unit =",unit,"bill=",total_bill,"Rs")
# else:
#     print("invalid")




# string=input("entre the string :")
# string="rhutuja"
# i=0
# while i<len(string):
#     j=0
#     while j<=i:
#         print(string[j],end="")
#         j+=1
#     i+=1
#     k=0
#     while k<=1:
#         print("_",end="")
#         k+=1




# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if i!=j and j!=k and k!=i :
#                 print(a[i],a[j],a[k] )
#             k+=1
#         j+=1
#     i+=1

# Write a python program to check whether a number is negative, positive or zero.
# num=int(input("enter the number :"))
# if num<0:
#     print(num,"number is negative")
# elif num>0:
#     print(num,"number is positive")
# else:
#     print("number is zero")


# Write a python program to check whether a number is divisible by 5 and 11 or not.
# num=int(input("enter the number :"))
# if num%5==0 and num%11==0:
#     print("it is divisible")
# else:
#     print("not divisible ")

# Write a Python program to create the multiplication table (from 1 to 10) of a number.

# num=int(input("enter the number :"))
# if num>0:
#     print(num*1)
#     print(num*2)
#     print(num*3)
#     print(num*4)
#     print(num*5)
#     print(num*6)
#     print(num*7)
#     print(num*8)
#     print(num*9)
#     print(num*10)
# else:
#     print("no")

# Write a Python program to calculate the length of a string
# string=input("enter the string :")
# print("length :",len(string))

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# string=input("entre the string :")
# if "ing" in string:
#     a=string.replace("ing","ly") 
#     print(a)
# elif "ly" in string:
#     b=string.replace("ly","ing")
#     print(b)
# else:
#     c=(string+"ingly")
#     print(c)

# Write a python program to check whether a year is leap year or not.
# year=int(input("entre the year :"))
# if year%100==0:
#     if year%400==0:
#         print(year,"century year")
#     else:
#         print(year,"not leap year")
# else:
#     if year%4==0:
#         print(year,"it is leap year")
#     else:
#         print(year,"not leap year")

# Write a python program to check whether a character is an alphabet or not.
# character=input("enter the alphabet :")
# if character>="a" or character<="z":
#     print(character," :it is alphabet")
# else:
#     print(character," :it is not aplhabet")


# Write a python program to input any alphabet and check whether it is vowel or consonant.
# alphabet=input("enter the alphabet :")
# if alphabet=="a" and "A"or alphabet=="e" and "E" or alphabet=="i" and "I" or alphabet=="o" and "O" or alphabet=="u" and "U":
#     print("this is vowel")
# else:
#     print("this is consulant")


# # Write a python program to input any character and check whether it is alphabet, digit or special character.
# var=str(input("enter the var :"))
# if var>="A" or var<="Z":
#     print("it is alphabet")
# elif (var)>0:
#     print("it is number")
# else:
#     print("it is special character")

# a=[2,5,6,7,8,9,3]
# i=0
# l=[]
# while i<len(a):
#     l.append(a[i]**2)
#     i+=1
# print(l) 



# A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.
# No_of_items=int(input("enter the items :"))
# cost=int(input("entre the cost :"))
# total_cost=No_of_items*cost
# if total_cost>=1000:
#     discount=total_cost*10/100
#     final_cost=total_cost-discount
#     print("final_cost",final_cost,"Rs,","Discount=",discount)
# elif total_cost<1000:
#     print("total_cost:",total_cost,"Rs")
# else:
#     print("invalid")



# A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years. Ask users for their salary and year of service and print the net bonus amount.
# salary=int(input("enter the salary :"))
# year=int(input("enter the year :"))
# if year<5:
#     print(salary)
# elif year>=5:
#     bonus=salary*5/100
#     net_bonus=salary+bonus
#     print("salary:",salary,",","net_bonus",net_bonus)
# else:
#     print("invalid")



# a=[2,0,5,6,7,0,0,5,0,1,0,0]
# l=[]
# for i in a:
#     if i !=0:
#         l.append(i)
# print(l)

# a=[1,3,6,9,4,6,7]
# l=[]
# for i in a:
#     if i%2==0:
#         l.append(i)
# print(l)

# a=[120,200,300,1230,450]
# l=[]
# for i in a:
#     if i!=0:
#         l.append(i)
# print(l)
# string=input("enter the string :")
# i=0
# while i<len(string):
#     print(string[i].upper()+string[i].lower()*i,end="_")
#     i+=1


# string=input("enter the string :")
# string="rhutuja"
# i=0
# while i<len(string):
#     print(string[i].upper()+string[i].lower()*i,end="_")
#     i+=1
#     j=0
#     while j<=i:
#         print("_",end="")
#         j+=1
#         # k=0


# string="rhutuja"
# i=0
# while i<len(string):
#     print(string[i].upper()+string[i].lower()*i,end="_")
#     i+=1
#     j=0
#     while j<=i:
#         print("_",end="")
#         j+=1


# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"
# num=int(input("enter the number :"))
# if num%5==0:
#     print("Hello")
# else:
#     print("Bey")


# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#         Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# unit=int(input("enter the unit :"))
# if unit<100:
#     print(unit)
# elif unit<=100 or unit<200:
#     a=unit*5
#     print(a)
# elif unit>=200:
#     b=unit*10
#     print(b)
# else:
#     print("invalid")


#  Write a program to display the last digit of a number.
# n=int(input("enter the number :"))
# m=n%10
# if m>0:
#     print(m)
# else:
#     print("invalid")


# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%

# cost=int(input("enter the cost price of bike :"))
# if cost>100000:
#     print("15% Tax")
# elif cost>50000 and cost <=100000:
#     print("10% Tax")
# elif cost<=50000:
#     print("5% Tax")
# else:
#     print("invalid")



# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# if a<b:
#     print(b,"is grater")
# else:
#     print(a,"is grater")


# Write a program to check whether a number entered is a three digit number or not.
# n=int(input("enter the number :"))
# b=str(n)
# if len(b)==3:
#     print("3 digit number")
# else:
#     print(" not 3 digit number")


# Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC.
# bp=int(input("enter the b.p :"))
# if bp==100:
#     print("water is boiling")
# else:
#     print("water is not boiling ")

# Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16


# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# o=input("enter the operator ")
# if o=="+":
#     print(a+b)
# elif o=="-":
#     print(a-b)
# elif o=="*":
#     print(a*b)
# elif o=="/":
#     print(a/b)
# else:
#     print("invalid")


# Write a Python program to guess a number between 1 to 9

# n=int(input("enter the number :"))
# if n>=1 and n<=9:
#     print("n is between 1 to 9")
# else:
#     print("not")

# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

# n=int(input("enter the number :"))
# n1=int(input("enter the number :"))
# sum=int(n+n1)
# if(sum )>=15 or (sum)<=20:
#     print("20")
# else:
#     print("no")

# Write a Python program to check a string represent an integer or not
# s=str(input("enter the str"))
# a1=int(s)
# if int(s)>=0:
#     print("integer")
# elif 's'>='a' or s<='z':
#     print("str")
# else:
#     print("another")

# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c

# print("The median is", median)



# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


# str = "Welcome Python"
# a = str.split()
# print (a)


# . Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them .
# Input1: kumar 
# Input 2:nayak
# Output: nayak kumar

# s1=input("enter :")
# s2=input("enter ")
# print(s2,s1)


# Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java

# extension=input("enter the string :")
# filename="abc.java"
# print(filename[4:])


# Write a Python program to test whether a number is within 100 of 1000 or 2000

# num=int(input("enter the num :"))
# if num>=1000 and num<=2000:
#     print("number is within 100 of 1000 or 2000")
# else:
#     print("no")

# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

# s=input("enter the string :")
# if "Is" in s:
#     print("unchanged")
# else:
#     print(s+"Is")



# Take 2 inputs and add them if the result is oddprint result odd hain, and if it is not print oddnahi hain
# n1=int(input("enter the n1"))
# n2=int(input("enter the n2"))
# n3=n1+n2
# if n3%2==0:
#     print("even")
# else:
#     print("odd")


# Ask a input whether it is raining or not if it is raining then say baarish ho rahi hain, otherwisetu bahar jaakekhel le.
# a=input("whether it is raining or not")
# if a=="raining":
#     print("baarish ho rahi hain")
# else:
#     print("bahar jaakekhel le")


# Ask a user to tell the speed of his vehicle, ifspeed is more than 70kmph, ask him to pay that thatmuchspeed multiplied by 50rs. Like if his speed 100kmph,you need to ask him the fine(100-70)*50=? This isthe fine
# amount he needs to pay, if his speed is not more 70, say him stay home, stay safe
# speed=int(input("enter the speed :"))
# if speed<70:
#     print("stay home, stay safe")
# elif speed>=70:
#     fine=(speed-70)*50
#     print("fine:",fine )
# else:
#     print("no fine")


# 66.The given number is of one digited or two digitedor three digited or more than three digited.
# num=str(input("enter the digit :"))
# length=len(num)
# if length==1:
#     print("one digit")
# elif length==2:
#     print("two digit")
# elif length==3:
#     print("three digit")
# else:
#     print("more than three digit")



# import json
# # a={"a":23,"b":1,"c":2}
# a={'a':23,'b':1,'c':2}
# with open  ("file.json","w") as f:
#     json.dump(a,f,indent=3)


# import json 
# # a={"a":1,"b":2,"c":3,"d":4}
# a={'a':23,'b':1,'c':2}
# print(json.dumps(a))

# import json 
# a='{"a":1,"b":2,"c":3,"d":4}'
# print(json.loads(a))

# import json 
# with open ("file.json","r") as f:
#     b=json.load(f)
# #     print(b)

# x=(json.dumps(b))
# print(x)
# print(json.loads(x))

# n=int(input("enter num"))
# if n//1000:
#     print(n//1000)
# if n//500:
#     print(n//500)
# if n//200:
#     print(n//200)


# Write a python program to check whether a number is negative, positive or zero.
# num=int(input("enter the number :"))
# if num<0:
#     print(num,"number is negative")
# elif num>0:
#     print(num,"number is positive")
# else:
#     print("number is zero")


# Write a python program to check whether a number is divisible by 5 and 11 or not.
# num=int(input("enter the number :"))
# if num%5==0 and num%11==0:
#     print("it is divisible")
# else:
#     print("not divisible ")

# Write a Python program to create the multiplication table (from 1 to 10) of a number.

# num=int(input("enter the number :"))
# if num>0:
#     print(num*1)
#     print(num*2)
#     print(num*3)
#     print(num*4)
#     print(num*5)
#     print(num*6)
#     print(num*7)
#     print(num*8)
#     print(num*9)
#     print(num*10)
# else:
#     print("no")

# Write a Python program to calculate the length of a string
# string=input("enter the string :")
# print("length :",len(string))

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# string=input("entre the string :")
# if "ing" in string:
#     a=string.replace("ing","ly") 
#     print(a)
# elif "ly" in string:
#     b=string.replace("ly","ing")
#     print(b)
# else:
#     c=(string+"ingly")
#     print(c)

# Write a python program to check whether a year is leap year or not.
# year=int(input("entre the year :"))
# if year%100==0:
#     if year%400==0:
#         print(year,"century year")
#     else:
#         print(year,"not leap year")
# else:
#     if year%4==0:
#         print(year,"it is leap year")
#     else:
#         print(year,"not leap year")

# Write a python program to check whether a character is an alphabet or not.
# character=input("enter the alphabet :")
# if character>="a" or character<="z":
#     print(character," :it is alphabet")
# else:
#     print(character," :it is not aplhabet")


# Write a python program to input any alphabet and check whether it is vowel or consonant.
# alphabet=input("enter the alphabet :")
# if alphabet=="a" and "A"or alphabet=="e" and "E" or alphabet=="i" and "I" or alphabet=="o" and "O" or alphabet=="u" and "U":
#     print("this is vowel")
# else:
#     print("this is consulant")


# Write a python program to input any character and check whether it is alphabet, digit or special character.
# var=(input("enter the var :"))
# if var>="a" and var<="z":
#     print("it is alphabet")
# elif int(var)>0:
#     print("digit")
# elif str(var)=="@" or str(var)=="#":
# elif "@" in var:
# # else:
#     print("it is special chr")
    # if var>0:
    #     print("it is number")
    # else:
    #     print("it is special character")

# a=[2,5,6,7,8,9,3]
# i=0
# l=[]
# while i<len(a):
#     l.append(a[i]**2)
#     i+=1
# print(l) 

# The given character is an uppercase letter or lowercaseletter or a digit or a special character.
# aplphabet=input("enter the alphabet :")
# if aplphabet>="A" and aplphabet<="Z":
#     print("upper case")
# else:
#     print("lower case")




# n=input("enter the number :")
# a=len(n)-2
# b=int(n)//10**a
# c=b%10
# if c==3:
#     print("yes")
# else:
#     print("no")



# l=[]
# i=0
# while i<5:
#     a=int(input("enetr :"))
#     l.append(a)
#     i+=1
# print(l)


# amount=int(input("enter the amount :"))
# if amount>=10 or amount<=20:
#     print("note of 10 rupees :",amount//10)
#     if amount>=20 or amount<=50:
#         print("note of 20 rupees :",amount//20)
#         if amount>=50 or amount<=100:
#             print("note of 50 rupees :",amount//50)
#             if amount>=100 or amount<=200:
#                 print("note of 100 rupees :",amount//100)
#                 if amount>=200 or amount<=500:
#                     print("note of 200 rupees :",amount//200)
#                     if amount>=500 or amount<=1000:
#                         print("note of 500 rupees :",amount//500)
#                         if amount>=1000 or amount<=2000:
#                             print("note of 1000 rupees :",amount//1000)
#                             if amount>=2000:
#                                 print("note of 2000 rupees :",amount//2000)
#                             # else:
#                                 # print("1")
#                         else:
#                             print("2")
#                     else:
#                         print("3")
#                 else:
#                     print("4")
#             else:
#                 print("5")
#         else:
#             print("6")
#     else:
#         print("7")
# else:
#     print("8")









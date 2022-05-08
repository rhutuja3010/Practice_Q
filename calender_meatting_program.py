from datetime import datetime
# print("officetime : 9am To 5pm")
# dt=datetime(2016,3,27,14,30,47)
# print(dt) 
# dt1=datetime()
# print(dt)


import datetime
import random
print("OFFICETIME : 10AM TO 17PM")
dt=datetime.datetime.today()
print(dt)
date=str(input("enter the date :"))
month=str(input("enter the month :"))
year=str(input("enter the year :"))
print(date+"-"+month+"-"+year)

# # prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))


# m=dt.strftime("%I")
# print(m)

# e=3
# i=0
# while i<e:
    # e1=input("enter the date :")
    # e1=input('%m/%d/%Y %I:%M %p')
    # e1=input('%m/%d/%Y %I:%M %p')
    # print(e1)
    # i+=1



'''from random import randrange
from datetime import timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

from datetime import datetime
d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
print(random_date(d1, d2))'''


from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


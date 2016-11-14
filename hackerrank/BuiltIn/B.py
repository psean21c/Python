'''
Leap Day
Created on Nov 14, 2016

@author: simon.park

The year can be evenly divided by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, 
the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 

'''
def is_leap(year):
    leap = False
    
    # Approach 1
    if (year % 4 ==0) and (year % 400 == 0):
        leap = True
    elif (year % 4 ==0) and (year % 100 == 0):
        leap = False
    elif year % 4 ==0:
        leap = True
        
    # Approach 2 : More simplified
    if (year % 100 == 0) and (year %400 != 0):
        leap = False
    elif (year % 4 == 0):
        leap = True

    return leap

print(is_leap(2000))
print(is_leap(2004))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2200))
print(is_leap(2300))
print(is_leap(2500))
print(is_leap(2016))



year = int(input())
print(is_leap(year))

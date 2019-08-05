a=int(input("enter a year:"))
if(a%100==0)and(a%400==0)and(a%4==0):
   print("the year is leap year")
else:
   print("the year is not a leap year")
   

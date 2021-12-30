import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
 
  
# display the calendar
for i in range(1,13):
    print(i)
    print(calendar.month(yy,i))

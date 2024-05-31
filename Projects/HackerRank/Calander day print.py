import calendar

# a = calendar.TextCalendar(firstweekday=6).formatyear(2015)
# print(a) # print calendar in string

from datetime import datetime 

# date_str = input()
# date_obj = datetime.strptime(date_str,'%m-%d-%Y')
# day_of_week = date_obj.strftime('%A')
# print(day_of_week)



month,date,year = input("").split() # in format of MM-DD-YYYY 
day = calendar.day_name[calendar.weekday(year=int(year),month=int(month),day=int(date))]
print(day.upper())
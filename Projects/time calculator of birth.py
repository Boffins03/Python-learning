from datetime import datetime
import time

# Get the current date and time
now = datetime.now()

# Extract the hours, minutes, and seconds
hoursnow = now.hour
minutesnow = now.minute
secondsnow = now.second


def Calculate_days(start_date, end_date):
    # Convert the string dates to datetime objects
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')

    # Calculate the difference between the two dates
    delta = end_date - start_date

    # Return the number of days
    return delta.days

# Test the function
start_date = input("Enter your DOB : ")
end_date = time.strftime("%d-%m-%Y")
calculate_days=Calculate_days(start_date, end_date)
# print(calculate_days)

# Check if user know time or not
a=input("Do you know the time of your birth:")
if a == 'yes' or a == 'Yes':
    h=int(input("Enter the hour you born(24-hour):"))
    a=input("Do you know the minute when you born:")
    if a == 'yes' or a == 'Yes':
        m=int(input("Enter the minute you born:"))
        a=input("Do you know the second when you born:")
        if a == 'yes' or a == 'Yes':
            s=int(input("Enter the second you born:"))
        else:
            s=0
    else:
        m, s =0,0
else:
    h, m, s = 0,0,0


# Calculating hours
def Hours(calculate_days,hoursnow,h):
    return ((calculate_days*24)+hoursnow-h)

hours=Hours(calculate_days,hoursnow,h)

# Calculating minutes
def Minutes(hours,minutesnow,m):
    return ((hours*60)+minutesnow-m)

minutes=Minutes(hours,minutesnow,m)

# Calculating second
def Second(minutes,secondsnow,s):
    return ((minutes*60)+secondsnow-s)

second=Second(minutes,secondsnow,s)


while True:
    userinput=input("What you want to find 'Days, Hours, Minutes, Second': ").lower()
    if userinput=='days' or 'hours' or 'minutes' or 'second':
        if userinput=='days':
            print(calculate_days)
            break
        elif userinput=='hours':
            print(hours)
            break
        elif userinput=='minutes':
            print(minutes)
            break
        elif userinput=='second':
            print(second)
            break
       
    else:
        userinput=input("What you want to find 'Days, Hours, Minutes, Second'")    



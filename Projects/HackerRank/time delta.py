from datetime import datetime

def time_diff(t1,t2):
    # Parse the timestamps
    datetime1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    datetime2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    # Calculate the time difference in seconds
    time_difference_seconds = abs((datetime2 - datetime1).total_seconds())

    return int(time_difference_seconds)


testcase = int(input())
answer = []

for i in range(testcase):
    # Parse the timestamps
    timestamp1 = input()
    timestamp2 = input()
    answer.append(time_diff(timestamp1,timestamp2))
    
for i in answer:
    print(i)        


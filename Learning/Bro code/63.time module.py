import time 
print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))
time_obj=time.localtime()
print(time_obj)
time.strftime('%b %D %Y %H:%M:%S',time_obj)
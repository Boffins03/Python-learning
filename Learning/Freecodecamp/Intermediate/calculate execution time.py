import time 

start_time = time.time()

# your code 
z = 0
for i in range(1,100):
    z += i
        
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:",execution_time, "seconds")
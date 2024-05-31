import time

# def fib(number):
#     fib_series = [1,1]
#     if number > 2:
#         for _ in range(number-2):
#             fib_series.append(fib_series[-1]+fib_series[-2])
#         return fib_series
#     elif number == 2:
#         return fib_series
#     elif number <= 0:
#         return 1
#     else:
#         fib_series = [1]
#         return fib_series
    
# question = int(input("Enter the position:"))

# start_time = time.perf_counter_ns()

# fiboonacci = fib(question)

# print(fiboonacci[-1])
# end_time = time.perf_counter_ns()
# execution_time_ns = end_time - start_time
# print("Execution time",execution_time_ns)

# # fiboonacci using recursion
# def fib(number):
#     if number <= 2:
#         return 1
#     elif number <= 0:
#         return 0
#     else:
#         return fib(number - 1) + fib(number - 2)

# start_time = time.perf_counter_ns()
# print(fib(question))
# end_time = time.perf_counter_ns()
# execution_time_ns = end_time - start_time
# print("Execution time",execution_time_ns)

# fiboonacci using recursion momoization
def fib(number,memo = {}):
    if number in memo:
        return memo[number]
    if number <= 2:
        return 1
    elif number <= 0:
        return 0
    else:
        memo[number] = fib(number - 1,memo) + fib(number - 2,memo)
        return memo[number]

start_time = time.perf_counter_ns()
print(fib(5))
print(fib(15))
print(fib(25))
print(fib(50))
end_time = time.perf_counter_ns()
execution_time_ns = end_time - start_time
print("Execution time",execution_time_ns)

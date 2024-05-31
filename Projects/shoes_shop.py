X = int(input("No of shoes"))  # Number of shoes
shoe_sizes = list(map(int, input("List of availabe shoe sizes").split()))  # List of available shoe sizes
N = int(input("No of customers"))  # Number of customers
available_sizes = {}
for size in shoe_sizes:
    if size in available_sizes:
        available_sizes[size] += 1
    else:
        available_sizes[size] = 1
total_earnings = 0
for _ in range(N):
    customer_data = input().split()
    size, price = int(customer_data[0]), int(customer_data[1])
    if size in available_sizes and available_sizes[size] > 0:
        total_earnings += price
        available_sizes[size] -= 1
print(total_earnings)

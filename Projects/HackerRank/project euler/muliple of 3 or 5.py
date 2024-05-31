if __name__ == '__main__':
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        
        # Calculate the sum of all numbers divisible by 3 or 5 up to n
        sum_divisible = sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
        
        print(sum_divisible)
# fast code
def sum_divisible_by_k(k, n):
    # Calculate the highest multiple of k less than or equal to n
    highest_multiple = (n - 1) // k
    
    # Calculate the sum of an arithmetic series
    return k * (highest_multiple * (highest_multiple + 1)) // 2

if __name__ == '__main__':
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
    
        # Calculate the sum of all numbers divisible by 3 or 5 up to n
        sum_divisible = (sum_divisible_by_k(3, n) +
                         sum_divisible_by_k(5, n) -
                         sum_divisible_by_k(15, n))
        
        print(sum_divisible)

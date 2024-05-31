# Bubble sort
a = [4, 24, 72, 13, 5, 2, 4]
print(f'Unsorted list: {a}')
for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(f'Sorted list using Bubble Sort: {a}')

# Insertion sort
a = [3, 234, 6, 24, 2, 56, 2, 6, 1, 8, 89, 9, 0]
print(f"Unsorted list: {a}")
for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print(f"Sorted list using Insertion Sort: {a}")

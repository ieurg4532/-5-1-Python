
n = int(input("n = "))

print(f"Enter {n} array elements:")

arr = [int(input()) for _ in range(n)]

print("Original array: ", arr)

sum = 0
for i in arr:
    if i > 0 and i % 2 == 0:
        sum += i 

print("Sum: ", sum)
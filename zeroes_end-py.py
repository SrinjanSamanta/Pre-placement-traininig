arr = []

n = int(input("Enter number of elements in the array: "))

print("Enter", n, "elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

result = []
count_zero = 0

for num in arr:
    if num != 0:
        result.append(num)
    else:
        count_zero += 1

result.extend([0] * count_zero)

print("Array after moving zeroes to the end:", result)

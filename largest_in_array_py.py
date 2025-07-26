arr = []

n = int(input("Enter number of elements in the array: "))

print("Enter", n, "elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num

print("The largest element is:", max_val)

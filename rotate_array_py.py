arr = []

n = int(input("Enter number of elements in the array: "))
print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))

last = arr[-1]
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = last

print("Array after rotating by one (clockwise):", arr)
arr = []

n = int(input("Enter number of elements in the array: "))

print("Enter", n, "elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

if arr[0] > arr[1]:
    max_val = arr[0]
    second = arr[1]
else:
    max_val = arr[1]
    second = arr[0]

for i in range(2, n):
    if arr[i] > max_val:
        second = max_val
        max_val = arr[i]
    elif arr[i] > second and arr[i] != max_val:
        second = arr[i]

print("The second largest element is:", second)

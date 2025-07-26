arr = []

n = int(input("Enter number of elements in the array: "))

print("Enter", n, "elements:")
for _ in range(n):
    num = int(input())
    arr.append(num)

print("Array before insertion:", arr)

element = int(input("Enter the element to insert at the end: "))
arr.append(element)

print("Array after insertion:", arr)

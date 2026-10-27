
def first_last(arr, target):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i

    return first, last

arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

first, last = first_last(arr, target)

print("First occurrence:", first)
print("Last occurrence:", last)
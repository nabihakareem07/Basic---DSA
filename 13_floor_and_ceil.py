
def floor_ceil(arr, x):
    floor = -1
    ceil = -1

    for element in arr:
        if element <= x:
            floor = element

        if element >= x:
            ceil = element
            break

    return floor, ceil

arr = list(map(int, input("Enter sorted array elements: ").split()))
x = int(input("Enter target: "))

floor, ceil = floor_ceil(arr, x)

print("Floor:", floor)
print("Ceiling:", ceil)
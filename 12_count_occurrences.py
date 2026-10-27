
def count_occurrences(arr, target):
    count = 0

    for element in arr:
        if element == target:
            count += 1

    return count

arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

print("Occurrences:", count_occurrences(arr, target))
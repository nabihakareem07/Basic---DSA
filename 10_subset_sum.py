
def subset_sum(arr, target):
    def solve(i, remaining):
        if remaining == 0:
            return True

        if i == len(arr) or remaining < 0:
            return False

        return (solve(i + 1, remaining - arr[i])
                or solve(i + 1, remaining))

    return solve(0, target)

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum: "))

if subset_sum(arr, target):
    print("Subset exists")
else:
    print("Subset does not exist")
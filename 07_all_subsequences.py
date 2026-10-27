
def subsequences(s, i, current):
    if i == len(s):
        print('"' + current + '"')
        return

    subsequences(s, i + 1, current + s[i])
    subsequences(s, i + 1, current)

s = input("Enter a string: ")
subsequences(s, 0, "")

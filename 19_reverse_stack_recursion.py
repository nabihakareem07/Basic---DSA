
def insert_at_bottom(stack, x):
    if not stack:
        stack.append(x)
        return

    temp = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(temp)

def reverse_stack(stack):
    if not stack:
        return

    x = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, x)

stack = list(map(int, input("Enter stack elements: ").split()))

reverse_stack(stack)

print("Reversed stack:", stack)
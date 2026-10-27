
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(
                min(x, self.min_stack[-1])
            )

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return

        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.stack:
            print("Stack is empty")
            return None

        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            print("Stack is empty")
            return None

        return self.min_stack[-1]

s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)

print("Minimum:", s.get_min())

s.pop()

print("Top:", s.top())
print("Minimum:", s.get_min())
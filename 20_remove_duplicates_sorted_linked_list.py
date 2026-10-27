
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    def remove_duplicates(self):
        temp = self.head

        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

ll = LinkedList()

arr = list(map(int, input("Enter sorted elements: ").split()))

for element in arr:
    ll.insert(element)

print("Original list:")
ll.display()

ll.remove_duplicates()

print("After removing duplicates:")
ll.display()
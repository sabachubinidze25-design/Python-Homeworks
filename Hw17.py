class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ამატებს ახალ ელემენტს სიის ბოლოში."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        """ამატებს ახალ ელემენტს სიის დასაწყისში."""
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def delete(self, data):
        """შლის პირველ ელემენტს, რომლის მნიშვნელობა უდრის data-ს."""

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:

            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def display(self):
        """ბეჭდავს Linked List-ს."""
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


l1 = LinkedList()

l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)

print("Original List:")
l1.display()

print()

l1.prepend(5)
print("After prepend(5):")
l1.display()

print()

l1.delete(30)
print("After delete(30):")
l1.display()

print()

l1.delete(5)
print("After delete(5):")
l1.display()

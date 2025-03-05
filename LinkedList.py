#OOP based linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next: #is not none
            last = last.next
        last.next = new_node

    def insert_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp == key and temp.data:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_print_recursive_call(self, node): #recursive function
        if node is None:
            return
        self.reverse_print_recursive_call(node.next)
        print(node.data, end=' ')

    def reverse_print(self): #method to be called
        self.reverse_print_recursive_call(self.head)
        print()

linkedlist = LinkedList()
linkedlist.insert_to_end(1)
linkedlist.insert_to_end(2)
linkedlist.insert_to_end(3)
linkedlist.display()

linkedlist.insert_to_start(0)
linkedlist.display()
linkedlist.reverse_print()

linkedlist.delete(2)
linkedlist.display()

print(linkedlist.search(3))
print(linkedlist.search(5))

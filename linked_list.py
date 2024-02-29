
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

my_list = LinkedList()

my_list.insert(5)
my_list.insert(10)
my_list.insert(15)
my_list.insert(20)
my_list.insert(25)

my_list.append(30)
my_list.append(35)
my_list.append(40)
my_list.append(45)
my_list.append(50)

my_list.push(55)
my_list.push(60)
my_list.push(65)
my_list.push(70)
my_list.push(75)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data):
        cur_node = self.head
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next
        if not cur_node:
            return
        prev.next = cur_node.next
        cur_node = None

    def append_middle(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(7)
    ll.delete(3)
    ll.append_middle(ll.head.next, 4)
    ll.print_list()
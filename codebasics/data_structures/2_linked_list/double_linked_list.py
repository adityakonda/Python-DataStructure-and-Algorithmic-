class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        if self.head is None:
            self.head = Node(None, data, None)
            return

        self.head.prev = Node(None, data, self.head)
        self.head = Node(None, data, self.head)

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(None, data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(itr, data, None)

    def print(self):

        if self.head is None:
            print("Empty Double List")
            return

        itr = self.head
        ddll_str = ''

        while itr:

            if itr.prev is not None:
                prev_data = itr.prev.data
            else:
                prev_data = 'Empty'

            if itr.next is not None:
                next_data = itr.next.data
            else:
                next_data = "Empty"

            ddll_str += "(" + str(prev_data) + ", " + str(itr.data) + ", " + str(next_data) + ")" + " --> "
            itr = itr.next

        print(ddll_str)

    def get_length(self):

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    #todo
    def remove_index(self):
        pass

    def insert_value(self, data_list):

        self.head = None
        for item in data_list:
            self.insert_at_end(item)

    def print_forward(self):

        if self.head is None:
            print("Empty Double List")
            return

        itr = self.head
        ddll_str = ''

        while itr:
            ddll_str += "(" + str(itr.data) + ")" + " --> "
            itr = itr.next

        print(ddll_str)

    def print_backward(self):

        if self.head is None:
            print("Empty Double List")
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        last_node = itr

        dll_str = ''
        while last_node:
            dll_str += "(" + str(last_node.data) + ")" + " --> "
            last_node = last_node.prev
        print(dll_str)


if __name__ == '__main__':

    dll = DoubleLinkedList()

    dll.insert_at_beginning("10")
    dll.insert_at_beginning("20")
    dll.insert_at_beginning("30")
    dll.insert_at_beginning("40")
    dll.insert_value(["banana", "mango", "grapes", "orange"])
    dll.print()
    dll.print_forward()
    dll.print_backward()
    print(dll.get_length())

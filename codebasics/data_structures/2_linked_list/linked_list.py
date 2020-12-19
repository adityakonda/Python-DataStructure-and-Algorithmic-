class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def inset_values(self, data_list):

        self.head = None
        for item in data_list:
            self.insert_at_end(item)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("Linked is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def remove_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:

            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_begining(data, None)
            return

        count = 0

        itr = self.head

        while itr:

            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            count += 1
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_end(100)
    ll.print()
    ll.insert_at(2,11)
    ll.insert_at(2, 12)
    ll.print()

    ll.remove_index(2)
    print("length is :", ll.get_length())
    ll.print()

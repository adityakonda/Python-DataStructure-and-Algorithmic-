class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        # Adding elements to left sub tree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        # Adding element to right sub tree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    #todo - did not understand this part
    def in_order_traversal(self):
        element = []

        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

        return element


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    number = [17,4,1,20,9,23,18,34]
    num_tree = build_tree(number)

    print(num_tree.in_order_traversal())


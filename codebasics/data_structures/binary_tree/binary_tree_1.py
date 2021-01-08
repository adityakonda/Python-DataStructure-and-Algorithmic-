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

    def in_order_traversal(self):
        element = []
        # LEFT TRAVERSE
        if self.left:
            element += self.left.in_order_traversal()

        # VISIT
        element.append(self.data)

        # RIGHT TRAVERSE
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def pre_order_traversal(self):
        element = []
        # Visit
        element.append(self.data)

        # Left
        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def post_order_traversal(self):
        element = []

        # Left
        if self.left:
            element += self.left.post_order_traversal()

        # Right
        if self.right:
            element += self.right.post_order_traversal()

        # Visit
        element.append(self.data)

        return element

    #todo - Debugging order_traversal
    def in_order_traversal_debug(self):
        element = []
        print("Default -->",element, "-->", self.data)
        if self.left:
            va = self.left.in_order_traversal()
            element += va
            print("$$$$ LEFT --> ", va )
            print("Left Element -->",element)

        element.append(self.data)
        print("--> Visit Element -->", self.data)

        if self.right:
            va = self.right.in_order_traversal()
            element += va

            print("$$$$ RIGHT --> ", va)
            print("Right Element -->", element)

        return element

    def search(self, val):
        if self.data == val:
            return True
        # search in left tree
        if val < self.data:
            if self.left:
                result = self.left.search(val)
                return result
            else:
                return False

        # search in right tree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # with recursion
    def find_min(self):

        if self.left:
            return self.left.find_min()
        else:
            return self.data

    # without recursion
    def find_min_test(self):

        if not self.left:
            return self.data

        node = self.left
        while node.left:
            node = node.left

        return node.data

    def find_max(self):

        if self.right:
            return self.right.find_max()
        else:
            return self.data

    #TODO - In - Progress
    def calculate_sum(self):

        pass


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    number = [17,4,1,20,9,23,18,34]
    num_tree = build_tree(number)

    print(num_tree.in_order_traversal_debug())

    print(num_tree.search(0))
    print("min",num_tree.find_min())
    print("max",num_tree.find_max())
    print("Pre order Traversal", num_tree.pre_order_traversal())
    print("Post order Traversal", num_tree.post_order_traversal())





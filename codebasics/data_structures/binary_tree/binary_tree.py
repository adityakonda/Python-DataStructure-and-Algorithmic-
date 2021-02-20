class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        # Ignoring duplicate values
        if data == self.data:
            return

        # Adding element to the left
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            pass

        # Adding elements to the right
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):

        if self.data == val:
            return True

        # Checking the left nodes
        if val < self.data:
            if self.left:
                return self.left.search(val)

        # Checking the right nodes
        if val > self.data:
            if self.right:
                return self.right.search(val)

        # If no match found then return False
        return False

    # Left Visit Right
    def in_order_traversal(self):
        elements = []

        # Traverse Left
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit
        elements.append(self.data)

        # Traverse Right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # Visit Left Right
    def pre_order_traversal(self):

        elements = []

        # Visit
        elements.append(self.data)

        # Left
        if self.left:
            elements += self.left.pre_order_traversal()

        # Right
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # Left Right Visit
    def post_order_traversal(self):

        elements = []

        # Left
        if self.left:
            elements += self.left.post_order_traversal()

        # Right
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # Assignment
    # def min(self):
    #     if self.left:
    #         return self.left.min()
    #     else:
    #         return self.data

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):

        total_sum = 0
        if self.left:
            total_sum += self.left.calculate_sum()

        total_sum += self.data

        if self.right:
            total_sum += self.right.calculate_sum()

        return total_sum

    def delete(self, val):

        # Searching left sub-tree
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        # Searching Right sub-tree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None

            # we have left Node but not Right
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def delete_approach_2(self, val):

        # Searching the left tree
        if val < self.data:
            if self.left:
                self.left = self.left.delete_approach_2(val)

        # Searching the right tree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_approach_2(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_approach_2(max_val)

        return self



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(elements)
    print(tree.search(91))
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    print(tree.find_max())
    print(tree.find_min())
    print(tree.calculate_sum())
    print(sum(elements))

    print(tree.in_order_traversal())

    # print(tree.delete(20))
    # print(tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(1)
    print("After deleting  4 ", numbers_tree.in_order_traversal())

    numbers_tree_2 = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree_2.delete_approach_2(20)
    print("After deleting 1", numbers_tree_2.in_order_traversal())


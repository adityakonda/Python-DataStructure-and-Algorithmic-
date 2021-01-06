class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):

        if level >= self.get_level():
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix, self.data)

            if self.children:
                for child in self.children:
                    child.print_tree(level)


def build_location_tree():

    gbl = TreeNode("Global")

    india = TreeNode("India")
    usa = TreeNode("USA")

    india_state_1 = TreeNode("Gujarat")
    india_state_2 = TreeNode("karnataka")

    usa_state_1 = TreeNode("New Jersey")
    usa_state_2 = TreeNode("California")

    india_state_1.add_child(TreeNode("Ahmedabad"))
    india_state_1.add_child(TreeNode("Baroda"))
    india_state_2.add_child(TreeNode("Bangluru"))
    india_state_2.add_child(TreeNode("Mysore"))

    usa_state_1.add_child(TreeNode("Princeton"))
    usa_state_1.add_child(TreeNode("Edision"))
    usa_state_2.add_child(TreeNode("San Francisco"))
    usa_state_2.add_child(TreeNode("Mountain View"))
    usa_state_2.add_child(TreeNode("Palo Alto"))

    india.add_child(india_state_1)
    india.add_child(india_state_2)

    usa.add_child(usa_state_1)
    usa.add_child(usa_state_2)

    gbl.add_child(india)
    gbl.add_child(usa)

    return gbl


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(2)
    pass


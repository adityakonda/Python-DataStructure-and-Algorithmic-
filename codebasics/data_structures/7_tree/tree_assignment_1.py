class TreeNode:

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, value):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if str(value).lower() == "name":
            print(prefix, self.name)
        elif str(value).lower() == "designation":
            print(prefix, self.designation)
        elif str(value).lower() == "both":
            print(prefix, self.name, " (" + self.designation + ")")
        else:
            return

        if self.children:
            for child in self.children:
                child.print_tree(value)


def build_management_tree():

    ceo = TreeNode("Alex","CEO")

    cto = TreeNode("Victor", "CTO")
    hr = TreeNode("Gel", "HR Head")

    infa_head = TreeNode("Sreeni", "Infrastructure Head")
    app_head = TreeNode("Sriram", "App Head")

    infa_head.add_child(TreeNode("Praveen", "Manager"))
    infa_head.add_child(TreeNode("aditya", "Tech Lead"))

    cto.add_child(infa_head)
    cto.add_child(app_head)

    hr.add_child(TreeNode("Peter", "Recruitment Head"))
    hr.add_child(TreeNode("Afroz", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy


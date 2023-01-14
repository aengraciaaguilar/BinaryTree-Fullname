# Laboratory Activity # 6
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def build_tree(elements):
        print("Building tree with these elements:", elements)
        root = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    fullname = ["A", "E", "N", "G", "R", "A", "C", "I", "A",
                "A", "M", "I", "L", "I", "C", "A", "Y",
                "A", "G", "U", "I", "L", "A", "R"]
    fullname_tree = build_tree(fullname)

    print("My fullname:",fullname)
    print("Min:",fullname_tree.find_min())
    print("Max:",fullname_tree.find_max())
    print("In order traversal:", fullname_tree.in_order_traversal())
    print("Pre order traversal:", fullname_tree.pre_order_traversal())
    print("Post order traversal:", fullname_tree.post_order_traversal())

    fullname_tree.delete("E")
    print("After deleting the letter E", fullname_tree.in_order_traversal())
    fullname_tree.delete("N")
    print("After deleting the letter N", fullname_tree.in_order_traversal())

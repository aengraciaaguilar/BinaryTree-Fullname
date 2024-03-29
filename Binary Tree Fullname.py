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

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

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

    print("Is the letter A on the list of my fullname? ", fullname_tree.search("A"))
    print("Is the letter Z on the list of my fullname? ", fullname_tree.search("Z"))
    print("====================================================================================================================================")

if __name__ == '__main__':

    phonenumber = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    ph_tree = build_tree(phonenumber)
    print("My phonenumber:", phonenumber)
    print("Sum:", ph_tree.calculate_sum())
    print("Min:", ph_tree.find_min())
    print("Max:", ph_tree.find_max())
    print("In order traversal:", ph_tree.in_order_traversal())
    print("Pre order traversal:", ph_tree.pre_order_traversal())
    print("Post order traversal:", ph_tree.post_order_traversal())

    ph_tree.delete(20)
    print("After deleting the number 20", ph_tree.in_order_traversal())
    ph_tree.delete(30)
    print("After deleting the number 30", ph_tree.in_order_traversal())

    print("Is the number 10 on the list of my phonenumber?", ph_tree.search(10))
    print("Is the number 19 on the list of my phonenumber?", ph_tree.search(19))

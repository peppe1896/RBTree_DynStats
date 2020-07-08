import sys
import Node as nd


class RedBlackTree():
    def __init__(self):
        self.TNIL = nd.Node(0)
        self.TNIL.color = 0
        self.TNIL.left = None
        self.TNIL.right = None
        self.root = self.TNIL

    def __in_order_helper(self, node):
        if node != self.TNIL:
            self.__in_order_helper(node.left)
            # sys.stdout.write(node.data + " ")
            print("data ", node.data, "; L:(", node.left.data, ") -R:(", node.right.data, ")-SZ: ", node.size, sep="")
            self.__in_order_helper(node.right)

    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def inorder(self):
        self.__in_order_helper(self.root)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        print("Pre-Left", x.size)
        y.size = x.size
        x.size = x.left.size + x.right.size + 1
        print("Post-Left", x.size)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        print("Pre-Right", x.size)
        y.size = x.size
        x.size = x.left.size + x.right.size + 1
        print("Post-Right", x.size)

    def insert(self, key):
        node = nd.Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNIL
        node.right = self.TNIL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.TNIL:
            y = x
            if node.data < x.data:
                x.size += 1
                x = x.left
            else:
                x.size += 1
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
            node.size += 1
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return
        node.size += 1
        self.__fix_insert(node)

    def OS_Select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return (self.OS_Select(x.left, i))
        else:
            return (self.OS_Select(x.right, i-r))

    def OS_Rank(self, x):
        r = x.left.size+1
        y = x
        while y is not self.TNIL:
            if y == y.parent.right:
                r += y.parent.left + 1
            y = y.parent
        return r

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def pretty_print(self):
        self.__in_order_helper(self.root)
        # self.__print_helper(self.root, "", True)

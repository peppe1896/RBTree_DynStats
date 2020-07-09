import Node as nd


class RedBlackTree():
    def __init__(self):
        self.TNIL = nd.Node(0)
        self.TNIL.color = 0
        self.TNIL.left = None
        self.TNIL.right = None
        self.TNIL.size = 0
        self.root = self.TNIL

    def in_order(self, node):
        if node != self.TNIL:
            self.in_order(node.left)
            # sys.stdout.write(node.data + " ")
            print("data ", node.data, "; L:(", node.left.data, ") -R:(", node.right.data, ")-SZ: ", node.size, sep="")
            self.in_order(node.right)

    def fix_node(self, k, withOS):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k, withOS)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent, withOS)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k, withOS)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent, withOS)
            if k == self.root:
                break
        self.root.color = 0

    def inorder(self):
        self.in_order(self.root)

    def left_rotate(self, x, withOS):
        # print("LR")
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
        if withOS:
            y.size = x.size
            x.size = x.left.size + x.right.size + 1

    def right_rotate(self, x, withOS):
        # print("RR")
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
        if withOS:
            y.size = x.size
            x.size = x.left.size + x.right.size + 1

    def insert(self, key, withOS=True):
        node = nd.Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNIL
        node.right = self.TNIL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        if withOS:
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
                self.root.size += 1

            elif node.data < y.data:
                y.left = node
            else:
                y.right = node

            if node.parent == self.root:
                node.size +=1

            if node.parent == None:
                node.color = 0
                return

            if node.parent.parent == None:
                return
            node.size += 1
        else:
            while x != self.TNIL:
                y = x
                if node.data < x.data:
                    x = x.left
                else:
                    x = x.right

            node.parent = y
            if y == None:
                self.root = node

            elif node.data < y.data:
                y.left = node
            else:
                y.right = node

            if node.parent == None:
                node.color = 0
                return

            if node.parent.parent == None:
                return
        self.fix_node(node, withOS)

    def OS_Select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.OS_Select(x.left, i)
        else:
            return self.OS_Select(x.right, i - r)

    def OS_Rank(self, x):
        r = x.left.size+1
        y = x
        while y is not self.root:
            if y == y.parent.right:
                r += y.parent.left.size + 1
            y = y.parent
        return r

    def print(self):
        self.in_order(self.root)

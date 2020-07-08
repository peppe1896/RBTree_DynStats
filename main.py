import Tree


if __name__ == "__main__":
    bst = Tree.RedBlackTree()
    j = 1
    for i in range(0, 20):
        j *= -1
        bst.insert(i*j)
    # bst.delete_node(25)
    bst.pretty_print()
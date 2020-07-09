class Node():

    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black
        self.size = 0

    def __str__(self):
        return str(self.data)


class NodeLinked:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.size = int(0)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __str__(self):
        return "Key " + str(self.data)

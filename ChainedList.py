import Node as nd


class linked_list:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def calc_size_ordered(self):
        current = self.head
        _size = 0
        while current != None:
            _size = _size + 1
            current.rank = _size
            current = current.getNext()

    def find_zero(self):
        current = self.head
        while current != None:
            if current.rank == 0:
                print(current.rank)
                return current

    def calc_size_unordered(self):
        list = []
        current = self.head
        while current != None:
            list.append(current.data)
            current = current.next
        rank = 1
        for i in list:
            current = self.head
            found = False
            while current != None and not found:
                if i == current.data:
                    current.rank = rank
                    rank = rank + 1
                    found = True
                current = current.next

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            current.size += 1
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add_unordered(self, item):
        temp = nd.NodeLinked(item)
        temp.next = self.head
        self.head = temp
        # print("Aggiunto", item)
        self.list_size += 1

    def add_ordered(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            # current.rank += 1
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = nd.NodeLinked(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.list_size += 1
        # self.calcSize()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def print(self):
        current = self.head
        while current is not None:
            print("size"+str(current.rank)+"-key:" + str(current.data), end="; ")
            current = current.next

    def list_select(self, i):
        if i <= self.list_size:
            current = self.head
            while current != None:
                if i == current.rank:
                    return current
                current = current.next
        else:
            print("Statistica d'ordine out of range")

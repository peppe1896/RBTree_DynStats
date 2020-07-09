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
            current.size = _size
            current = current.getNext()

    def calc_size_unordered(self):
        list = []
        current = self.head
        while current != None:
            list.append(current.data)
            current = current.next
        list.sort()
        for i in range(0, len(list)):
            temp = self.head
            assigned = False
            while temp != None and not assigned:
                if temp.data == list[i]:
                    if temp.size == 0:
                        j = i + 1
                        temp.size = j
                        assigned = True
                temp = temp.next

    def calc_size_unordered_old(self):
        rank = 1
        while rank <= self.list_size:
            current = self.head
            min = self.head
            while current != None:
                if current.data < min.data:
                    if current.size == 0:
                        min = current
                current = current.next
            min.size = rank
            rank += 1

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

    def delete(self, value):
        previous = self.head
        current = self.head
        while current != None:
            previous = current
            if value == current.data:
                break
            current = current.next
        if current == None:
            print("Nodo non presente.")
        else:
            previous.next = current.next

    def print(self):
        current = self.head
        while current is not None:
            print("size" + str(current.size) + "-key:" + str(current.data), end="; ")
            current = current.next

    def list_select(self, i):
        if i <= self.list_size:
            current = self.head
            while current != None:
                if i == current.size:
                    return current
                current = current.next
        else:
            print("Error: out of range")

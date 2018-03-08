class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext




class LinkedList(object):
    def __init__(self):
        self.head = None
        self.iter = 0
        self.current_iter = self.head

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        position = 0
        while current != None:
            if current.getData() == item:
                return position
            else:
                current = current.getNext()
                position += 1

    def getValue(self):
        current = self.head
        self.list_hold = []
        while current != None:
            self.list_hold.append(current.getData())
            #print current.getData()
            current = current.getNext()
        return  self.list_hold


list_one = LinkedList()
list_two = LinkedList()

list_one.add(3)
list_one.add(4)
list_one.add(2)

list_two.add(4)
list_two.add(6)
list_two.add(5)

list_three = LinkedList()
list_one.getValue()
print "\n"
list_two.getValue()
ll = list_one.getValue()
print ll
def add_lists(l1,l2):
    l1 = l1.getValue()
    l2 = l2.getValue()
    the_list_length = l1.length()
    for i in range(the_list_length):

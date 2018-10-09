"""Class of list's items"""


class Item():
    """Class of list's items"""
    next_item = None
    prev_item = None
    elem = None

    def __init__(self, next_item, prev_item, elem):
        self.next_item = next_item
        self.prev_item = prev_item
        self.elem = elem

    def get_next_item(self):
        """Getter"""
        return self.next_item

    def set_next_item(self, item):
        """Setter"""
        self.next_item = item

    def set_prev_item(self, item):
        """Setter"""
        self.prev_item = item

    def get_prev_item(self):
        """Getter"""
        return self.prev_item

    def get_elem(self):
        """Getter"""
        return self.elem


class DoubleLinkedList():
    """Class of Double Linked List"""
    mylist = []
    index = 0

    def __init__(self):
        self.mylist = []
        self.index = 0

    def get_list(self):
        """Getter"""
        return self.mylist

    def push(self, elem):
        """Method for adding new element to the end of list"""
        if self.index == 0:
            item = Item(None, None, elem)
            self.mylist.append(item)
            self.index += 1
        else:
            item = Item(None, self.mylist[self.index - 1], elem)
            self.mylist[self.index - 1].set_next_item(item)
            self.mylist.append(item)
            self.index += 1

    def pop(self):
        """Delete element from the end of the list"""
        if self.index == 0:
            raise Exception('Empty list')
        self.index -= 1
        self.mylist.pop()
        self.mylist[self.index - 1].set_next_item(None)

    def un_shift(self, elem):
        """Add element in the top of list"""
        if self.index != 0:
            item = Item(self.mylist[0], None, elem)
            self.mylist[0].set_prev_item(item)
            self.mylist.insert(0, item)
            self.index += 1
        else:
            item = Item(None, None, elem)
            self.mylist.append(item)
            self.index += 1

    def shift(self):
        """Delete element from the top of list"""
        if self.index == 0:
            raise Exception('Empty list')
        if self.index == 1:
            self.mylist.remove(self.mylist[0].get_elem())
        if self.index > 1:
            self.mylist[1].set_prev_item(None)
            del self.mylist[0]
            self.index -= 1

    def len(self):
        """Return count of list's elements"""
        return self.index

    def delete(self, elem):
        """Delete element from list"""
        if self.index == 0:
            raise Exception('Empty list')
        elem_list = []
        for i in self.mylist:
            elem_list.append(i.get_elem())
        if elem in elem_list:
            index_of_elem = elem_list.index(elem)
            if self.index == 1:
                self.mylist.remove()
                self.index -= 1
            elif index_of_elem == 0:
                self.shift()

            elif index_of_elem == self.index - 1:
                self.mylist.pop()
                self.index -= 1
            else:
                self.mylist[index_of_elem + 1].set_prev_item(self.mylist[index_of_elem - 1])
                self.mylist[index_of_elem - 1].set_next_item(self.mylist[index_of_elem + 1])

                del self.mylist[index_of_elem]
                self.index -= 1
        else:
            raise Exception('No this Element')

    def contains(self, elem):
        """To Check if element contains in list"""

        elem_list = []
        for i in self.mylist:
            elem_list.append(i.get_elem())
        return bool(elem in elem_list)

    def first(self):
        """Return first element in list"""
        if self.index == 0:
            raise Exception('Empty list')
        return self.mylist[0]

    def last(self):
        """Return last element in list"""
        if self.index == 0:
            raise Exception('Empty list')
        return self.mylist[-1]

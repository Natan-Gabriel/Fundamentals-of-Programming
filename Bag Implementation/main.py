class Bag:

    # creates a new, empty Bag
    # O(1)
    def __init__(self):
        self.__elems = []
        self.__freq = []

    # adds a new element to the Bag
    # O(n)-elem.unice
    def add(self, e):
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == e:
                self.__freq[i] += 1
                return
        self.__elems.append(e)
        self.__freq.append(1)

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    # O(n)-elem unice
    def remove(self, e):
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == e:
                self.__freq[i] -= 1
                if self.__freq[i] == 0:
                    self.__freq.pop(i)
                    self.__elems.pop(i)

                return True

        return False

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    # O(1)
    def search(self, e):
        return e in self.__elems

    # counts and returns the number of times the element e appears in the bag
    # O(n)-nr elem
    def nrOccurrences(self, e):
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == e:
                return self.__freq[i]
        return 0

    # returns the size of the Bag (the number of elements)
    # O(n)-frequencies
    def size(self):
        nr = 0
        for i in self.__freq:
            nr += i
        return nr

    # returns True if the Bag is empty, False otherwise
    # O(1)
    def isEmpty(self):
        return self.size() == 0

    # returns a BagIterator for the Bag
    def iterator(self):
        return BagIterator(self)


class BagIterator:

    # creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    # O(1)
    def __init__(self, b):
        self.__b = b
        self.__curr = 0

    # returns True if the iterator is valid
    # O(1)
    def valid(self):
        return self.__curr < self.__b.size()

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    # O(n)-nr de elem
    def getCurrent(self):
        if self.__curr == self.__b.size():
            raise ValueError
        i = 1
        length = 0
        for i in range(0, len(self.__b._Bag__freq)):
            if (length + self.__b._Bag__freq[i] <= self.__b.size()):
                length += self.__b._Bag__freq[i]
            else:
                return self.__b._Bag__elems[i]

        return self.__b._Bag__elems[i]

    # moves the iterator to the next element
    # throws ValueError if the iterator is not valid
    # O(1)
    def next(self):
        if self.__curr == self.__b.size():
            raise ValueError("No more elems")
        self.__curr += 1

    # sets the iterator to the first element from the Bag
    # O(1)
    def first(self):
        self.__curr = 0
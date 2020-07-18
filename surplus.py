class Multiset:

    def __init__(self):
        self.multiset = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.multiset.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        try:
            self.multiset.remove(val)
        except ValueError as e:
            pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if self.multiset.index(val):
            return True
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.multiset)


if __name__ == '__main__':
        m = Multiset()
        print(len(m))
        m.add(5)
        print(len(m))
        m.remove(4)
        print(len(m))





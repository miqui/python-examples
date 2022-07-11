class PriorityQueue(object):

    def __init__(self):
        self._items = []


    def add_item(self, new_item):
        """Add items into queue at correct place."""

        for i, item in enumerate(self._items):
            if new_item < item:
                self._items.insert(i, new_item)
                break
        else:
            self._items.append(new_item)


def main():
    pq = PriorityQueue()
    pq.add_item("yellow")
    pq.add_item("blue")
    pq.add_item("red")
    pq.add_item("green")

    print(pq._items)

if __name__ == '__main__':
    main()
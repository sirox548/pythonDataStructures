class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        return self.items.insert(0, item)

    def add_rear(self, item):
        return self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def peek_front(self):
        if self.items:
            return self.items[0]
        else:
            message = "There is no item in the front."
            return message

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        else:
            message = "There is no item in the rear."
            return message

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


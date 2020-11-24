"""
First in First Out => FIFO
Runtime or linear time O(n)

"""
class Queue:

    def __init__(self):
        self.items = []

    """
    Insert item at the front of the list/ initial position 0.
    """
    def enqueue(self, item):
        return self.items.insert(0, item)

    """
    removes and return the front-most item in the queue
    """
    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            message = "There is no item to remove from the queue."
            return message

    def peek(self):
        """"
        returns the last item in the list. ie: the front-most item
        in queue.
        """
        if self.items:
            return self.items[-1]
        else:
            message = "There is no item in queue."
            return message

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

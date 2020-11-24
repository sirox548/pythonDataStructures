"""
last in first out [LIFO]
runtime/time complexity => O(1)
"""



class Stack:

    def __init__(self):
        self.items = []

    """"
    Append new item to the to the end of the stack
    """
    def push(self, item):
        return self.items.append(item)

    """"
    Removes the last recorded item of the stack
    """
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            message = "No items or no more items remaining."
            return message

    """"
    Returns the last item recorded in the stack 
    """
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            message = "No last items."
            return message

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
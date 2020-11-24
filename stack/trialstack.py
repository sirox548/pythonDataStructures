class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []


def symbol_match(symbol_str):
    pairs = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }

    open_sym = pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]
        #
        if symbol in pairs:
            my_stack.push(symbol)

        # if the stack is completely empty
        else:
            if my_stack.is_empty():
                return False

            # if there are more items in the stack, check for mis-match
            else:
                top_item = my_stack.pop()
                if symbol != pairs[top_item]:
                    return False

        index += 1
    if my_stack.is_empty():
        return True
    # stack is not empty and symbols dont match.
    else:
        return False

# Testcase 1 => False
print(symbol_match('[(}})]'))

# Testcase 2 => True
print(symbol_match('{[()]}'))

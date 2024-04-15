'''
Module implementing a frequency stack.
'''

from collections import deque

class Node:
    '''
    Class representing a node
    of the sorted frequency queue
    '''

    def __init__(self, value: int, freq: int = 1, prev: 'Node' = None, nxt: 'Node' = None):
        '''
        Constructor for the Node class.
        '''
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = nxt


class FreqList:
    '''
    Class represented a frequency-sorted
    doubly linked list.
    '''
    def __init__(self):
        '''
        Constructor for the FreqList class.
        '''
        self.head = None
        self.tail = None
        self.values = set()


    def add(self, val: int):
        '''
        Adds a value to the list.
        '''
        if not self.head:
            self.head = self.tail = Node(val)
            self.values.add(val)
            return

        if not self.head.next:
            if self.head.value == val:

                self.head.freq += 1

            else:

                self.tail = Node(val, 1, self.head)
                self.head.next = self.tail

            self.values.add(val)

            return

        if val not in self.values:
            self.tail = Node(val, 1, self.tail)
            self.tail.prev.next = self.tail
            self.values.add(val)
            return

        cur_node = self.head

        while cur_node is not None:

            if cur_node.value == val:
                break

            cur_node = cur_node.next

        cur_node.freq += 1

        while cur_node.prev is not None and cur_node.freq > cur_node.prev.freq:
            cur_node.prev.value, cur_node.prev.freq, cur_node.value, cur_node.freq =\
                cur_node.value, cur_node.freq, cur_node.prev.value, cur_node.prev.freq
            cur_node = cur_node.prev


    def decrease(self, val: int):
        '''
        Decreases the frequency of a value.
        '''
        cur_node = self.head

        while cur_node is not None:

            if cur_node.value == val:
                break

            cur_node = cur_node.next

        if cur_node is None:
            raise ValueError(f'Value {val} not found in the list.')

        cur_node.freq -= 1

        if not cur_node.freq:

            self.values.remove(cur_node.value)

            if self.head.next is None:
                self.head = self.tail = None

            elif cur_node is self.head:
                self.head = cur_node.next
                self.head.prev = None

            elif cur_node is self.tail:
                self.tail = cur_node.prev
                self.tail.next = None

            else:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev

            return

        while cur_node.next is not None and cur_node.freq < cur_node.next.freq:
            cur_node.value, cur_node.freq, cur_node.next.value, cur_node.next.freq =\
                    cur_node.next.value, cur_node.next.freq, cur_node.value, cur_node.freq
            cur_node = cur_node.next


    def get_max(self)-> set[int]:
        '''
        Returns a set of value with the highest frequency.
        '''
        if self.head is None:
            return set()

        cur_node = self.head
        freq = cur_node.freq
        values = set()

        while cur_node is not None and cur_node.freq == freq:
            values.add(cur_node.value)
            cur_node = cur_node.next

        return values


    def __contains__(self, val: int)-> bool:
        '''
        Checks if a value is in the list.
        '''
        return val in self.values


    def __str__(self):
        '''
        Returns a string representation of the list.
        '''
        cur_node = self.head
        result = ''
        while cur_node is not None:
            result += f'{cur_node.value}({cur_node.freq}) -> '
            cur_node = cur_node.next
        return result + 'None'


class FreqStack:
    '''
    Class representing a frequency stack.
    '''

    def __init__(self):
        '''
        Constructor for the FreqStack class.
        '''
        self.stack = deque()
        self.value_list = FreqList()


    def push(self, val: int) -> None:
        '''
        Pushes a value to the frequency stack.
        '''
        self.stack.append(val)
        self.value_list.add(val)


    def pop(self) -> int:
        '''
        Pops the value with the highest frequency.
        '''
        if not bool(self.stack):
            return None

        values = self.value_list.get_max()

        val = None
        counter = 0

        while val not in values:
            val = self.stack[-1]
            self.stack.rotate(1)
            counter -= 1

        self.stack.popleft()
        self.stack.rotate(counter+1)
        self.value_list.decrease(val)

        return val

'''
Module that implements a stack
using queues.
'''

class Node:
    '''
    Class representing a single node of
    a linked list.
    '''
    def __init__(self, data: int, prev: 'Node' = None, nxt: 'Node' = None):
        '''
        Initialize the Node.
        '''
        self.data = data
        self.prev = prev
        self.next = nxt


class Queue:
    '''
    Class representing a queue,
    implemented using a linked list.
    '''

    def __init__(self):
        '''
        Initializes the queue.
        '''
        self.head = self.tail = None


    def push(self, value: int):
        '''
        Push a value to the top
        of the queue.
        '''
        if not self.head:

            self.head = self.tail = Node(value)
            return

        if self.head.next is None:

            self.head = self.tail.prev = Node(value, None, self.tail)
            return

        self.head.prev = self.head = Node(value, None, self.head)


    def peek(self)-> int:
        '''
        Get the bottom-most value of the queue
        without deleting it.
        '''
        return self.tail.data if self.tail is not None else None


    def pop(self)-> int:
        '''
        Get the bottom-most value of the queue
        and delete it.
        '''
        if self.tail is None:
            return None

        value = self.tail.data

        if self.head.next is None:

            self.head = self.tail = None
            return value

        self.tail.prev.next, self.tail = None, self.tail.prev

        return value

    def __len__(self)-> int:
        '''
        Get the size of the queue.
        '''
        cur_node = self.head
        counter = 0

        while cur_node:
            counter += 1
            cur_node = cur_node.next

        return counter

    def is_empty(self)-> bool:
        '''
        Check if the queue is empty.
        '''
        return self.tail is None


class MyStack:
    '''
    Custom stack class.
    '''

    def __init__(self):
        '''
        Initialize the stack.
        '''
        self.main = Queue()
        self.helper = Queue()


    def push(self, x: int) -> None:
        '''
        Push an element to the top of the stack.
        '''
        self.helper.push(x)

        while not self.main.is_empty():

            self.helper.push(self.main.pop())

        self.helper, self.main = self.main, self.helper

        print(self.top())


    def pop(self) -> int:
        '''
        Get an element from the top of the stack
        and delete it.
        '''
        return self.main.pop()


    def top(self) -> int:
        '''
        Get an element from the top of the stack
        without deleting it.
        '''
        return self.main.peek()


    def empty(self) -> bool:
        '''
        Check if the stack is empty.
        '''
        return self.main.is_empty()

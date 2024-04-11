'''
Module that implements a queue
using stacks.
'''

class Node:
    '''
    Class representing a single node of
    a linked list.
    '''
    def __init__(self, data: int, nxt: 'Node' = None):
        '''
        Initialize the Node.
        '''
        self.data = data
        self.next = nxt


class Stack:
    '''
    Class representing a stack,
    implemented using a linked list.
    '''

    def __init__(self):
        '''
        Initializes the stack.
        '''
        self.head = None

    def push(self, value: int):
        '''
        Push a value to the top
        of the stack.
        '''
        self.head = Node(value, self.head)

    def peek(self)-> int:
        '''
        Get the top-most value of the stack
        without deleting it.
        '''
        return self.head.data if self.head is not None else None

    def pop(self)-> int:
        '''
        Get the top-most value of the stack
        and delete it.
        '''
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        return value

    def __len__(self)-> int:
        '''
        Get the size of the stack.
        '''
        cur_node = self.head
        counter = 0

        while cur_node:
            counter += 1
            cur_node = cur_node.next

        return counter

    def is_empty(self)-> bool:
        '''
        Check if the stack is empty.
        '''
        return self.head is None


class MyQueue:
    '''
    Custom queue class.
    '''

    def __init__(self):
        '''
        Initialize the queue.
        '''
        self.main = Stack()
        self.helper = Stack()


    def push(self, x: int) -> None:
        '''
        Push an element to the top of the queue.
        '''
        while not self.main.is_empty():

            self.helper.push(self.main.pop())

        self.main.push(x)

        while not self.helper.is_empty():

            self.main.push(self.helper.pop())


    def pop(self) -> int:
        '''
        Get an element from the bottom of the queue
        and delete it.
        '''
        return self.main.pop()


    def peek(self) -> int:
        '''
        Get an element from the bottom of the queue
        without deleting it.
        '''
        return self.main.peek()


    def empty(self) -> bool:
        '''
        Check if the queue is empty.
        '''
        return self.main.is_empty()

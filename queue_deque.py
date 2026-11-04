from linked_list import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        removed = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed.data

    def peek(self):
        if self.front is None:
            return None

        return self.front.data

    def to_list(self):
        values = []
        current = self.front

        while current:
            values.append(current.data)
            current = current.next

        return values


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_front(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def add_rear(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.front is None:
            return None

        removed = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed.data

    def remove_rear(self):
        if self.rear is None:
            return None

        removed = self.rear

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            current = self.front

            while current.next != self.rear:
                current = current.next

            self.rear = current
            self.rear.next = None

        return removed.data

    def to_list(self):
        values = []
        current = self.front

        while current:
            values.append(current.data)
            current = current.next

        return values

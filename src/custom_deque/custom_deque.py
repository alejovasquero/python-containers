class Element:
    def __init__(self, value, next_element=None, parent_element=None):
        self.value = value
        self.next: Element = next_element
        self.parent = parent_element


class CustomDeque:

    def __init__(self):
        self.front: Element = None
        self.rear: Element = None

    def append_left(self, value):
        element = Element(value)

        if self.front is None and self.rear is None:
            self.rear = element
            self.front = element
            return

        element.next = self.front
        self.front.parent = element
        self.front = element

    def append_right(self, value):
        element = Element(value)

        if self.front is None and self.rear is None:
            self.rear = element
            self.front = element
            return

        self.rear.next = element
        element.parent = self.rear
        self.rear = element

    def remove_front(self):
        element = None
        if self.front is not None:
            element = self.front.value
            self.front = self.front.next
            if self.front is not None:
                self.front.parent = None

        if self.front is None:
            self.rear = None

        return element

    def remove_rear(self):
        element = None
        if self.rear is not None:
            element = self.rear.value
            self.rear = self.rear.parent
            if self.rear is not None:
                self.front.next = None

        if self.rear is None:
            self.front = None

        return element

    def __str__(self):
        return self.to_list().__str__()

    def to_list(self):
        head = self.front
        ans = []
        while head is not None:
            ans.append(head.value)
            head = head.next

        return ans

    def __len__(self):
        return len(self.to_list())

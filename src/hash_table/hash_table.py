class ItemElement:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"


class LinkedList:

    def __init__(self):
        self.value: ItemElement = None
        self.next: LinkedList = None


class HashTable:

    def __init__(self, size=200, hash_func=hash):
        self.max_size = size
        self.capacity = 0
        self.hash_func = hash_func
        self.array: [ItemElement] = [None] * self.max_size
        self.chains: [LinkedList] = [None] * self.max_size
        self.collisions = 0

    def __getitem__(self, item):
        index = self.hash_func(item) % self.max_size
        element: ItemElement = self.array[index]
        if element is None:
            return None
        else:
            if item == element.key:
                return element.value

            head: LinkedList = self.chains[index]

            while head is not None and head.value.key != item:
                head = head.next

            if head is not None:
                return head.value.value

            return None

    def __setitem__(self, key, value):
        index = self.hash_func(key) % self.max_size
        element: ItemElement = self.array[index]

        if element is None:
            self.array[index] = ItemElement(key, value)
            self.capacity += 1
        else:
            if element.key == key:
                self.array[index].value = value
            else:
                self.collisions += 1
                self.capacity += 1
                self.handle_collision(index, ItemElement(key, value))

    def handle_collision(self, index, element: ItemElement):
        chain_head: LinkedList = self.chains[index]

        if chain_head is None:
            head: LinkedList = LinkedList()
            head.value = element
            head.next = None
            self.chains[index] = head
        else:
            parent: LinkedList = None
            current_list: LinkedList = chain_head
            while current_list is not None:
                parent = current_list
                current_list = current_list.next

            append_element = LinkedList()
            append_element.next = None
            append_element.value = element

            parent.next = append_element

    def __delitem__(self, instance):
        index = self.hash_func(instance) % self.max_size
        element: ItemElement = self.array[index]

        if element is not None:
            if element.key == instance:
                self.array[index] = None
                del element
                self.move_head_chain_to_top(index)
                self.capacity -= 1
                return

            parent: LinkedList = None
            current_element: LinkedList = self.chains[index]

            while current_element.value.key != instance and current_element is not None:
                parent = current_element
                current_element = current_element.next

            if parent is None and current_element is not None:
                self.chains[index] = current_element.next
                current_element.next = None
                del current_element.value
                del current_element
                self.capacity -= 1
                return

            if current_element is not None:
                parent.next = current_element.next
                current_element.next = None
                self.capacity -= 1
                del current_element

    def move_head_chain_to_top(self, index):
        element: LinkedList = self.chains[index]

        if element is not None:
            self.array[index] = element.value
            self.chains[index] = element.next

    def __str__(self):
        ans = []
        for i in self.array:
            if i is not None:
                ans.append(str(i))
        return ans.__str__()

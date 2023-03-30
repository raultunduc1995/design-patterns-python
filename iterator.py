class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, head) -> None:
        self.head = head
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            value = self.current.value
            self.current = self.current.next
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    headNode = ListNode(1)
    headNode.next = ListNode(2)
    headNode.next.next = ListNode(3)
    linkedList = LinkedList(headNode)
    for nodeValue in linkedList:
        print(f'This is the node value: {nodeValue}')

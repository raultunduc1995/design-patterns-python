class Array:

    def __init__(self) -> None:
        self.capacity = 2
        self.length = 0
        self.array = [0] * self.capacity  # Array of capacity 2

    def add(self, value):
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = value
        self.length += 1

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for index in range(self.length):
            new_array[index] = self.array[index]
        self.array = new_array

    def remove(self, element) -> bool:
        if self.length == 0:
            return False
        try:
            self.array.remove(element)
            return True
        except ValueError:
            print(f'Opps! {element} is not in array')
            return False


if __name__ == '__main__':
    my_array = Array()
    my_array.add(1)
    my_array.add(2)
    my_array.add(3)
    my_array.add(3)
    my_array.add(3)
    my_array.remove(4)
    my_array.remove(3)
    print(f'My array {my_array.array}')

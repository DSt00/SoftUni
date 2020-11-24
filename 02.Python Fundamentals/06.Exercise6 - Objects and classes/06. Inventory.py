class Inventory:
    items = []

    def __init__(self, capacity):
        self.__capacity = capacity
        self.capacity_left = capacity

    def add_item(self, item):
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(item)
            self.capacity_left -= 1
        else:
            return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {self.capacity_left}"

class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result = [i for i in self.products if i[0] == first_letter]
        return result

    def __repr__(self):
        self.products.sort()
        result = ""
        result += f'Items in the {self.name} catalogue:\n'
        for item in range(len(self.products)):
            result += f'{self.products[item]}\n'
        return result

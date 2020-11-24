class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        Catalogue.products.append(product)

    def get_by_letter(self, first_letter):
        result = []
        result = [i for i in Catalogue.products if i[0] == first_letter]
        return result

    def __repr__(self):
        Catalogue.products.sort()
        result = ""
        result += f'Items in the {self.name} catalogue:\n'
        for item in range(len(Catalogue.products)):
            result += f'{Catalogue.products[item]}\n'
        return result


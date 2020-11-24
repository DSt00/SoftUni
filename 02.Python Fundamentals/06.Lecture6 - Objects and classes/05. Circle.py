class Circle:
    __pi = 3.14

    def __init__(self, d):
        self.diameter = d

    def calculate_circumference(self):
        return self.diameter * Circle.__pi

    def calculate_area(self):
        r = self.diameter / 2
        return Circle.__pi * (r * r)

    def calculate_area_of_sector(self, angle):
        r = self.diameter / 2
        return r ** 2 * (angle / 360) * Circle.__pi

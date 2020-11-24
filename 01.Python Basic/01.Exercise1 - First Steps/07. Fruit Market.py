price_strawberry = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())

price_raspberry = price_strawberry * 0.5
price_oranges = price_raspberry * 0.6
price_bananas = price_raspberry * 0.2

total_sum = price_strawberry * quantity_strawberry + price_bananas * quantity_bananas + price_oranges * quantity_oranges + price_raspberry * quantity_raspberry
print(total_sum)
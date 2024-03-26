class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    print("Product added successfully")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("product removed successfully")
                return

    def display_inventory(self):
        for product in self.products:
            print(product)


manager = Inventory()
manager.add_product(Product("Laptop", "Its gaming laptop", 1200, 10))
manager.add_product(Product("Mouse", "Its bluetooth mouse", 110, 5))
manager.display_inventory()
manager.remove_product(Product("Mouse"))
manager.display_inventory()
class Item:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

# Información precargada para el inventario
inventory = [
    Item(1, 'Mantequilla de cacahuate', 150),
    Item(2, 'Mostaza amarilla Heinz', 200),
    Item(3, 'Fusili Barilla', 80)
]
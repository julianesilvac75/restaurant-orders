class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []
        self.updated_inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, customer, order, day):
        ingredients = self.INGREDIENTS[order]
        for item in ingredients:
            if self.updated_inventory[item] == 0:
                return False

            self.updated_inventory[item] -= 1

        self.orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        buy_list = {}

        for item in self.updated_inventory:
            buy_list[item] = (
                self.MINIMUM_INVENTORY[item] - self.updated_inventory[item]
            )

        return buy_list

    def get_available_dishes(self):
        all_dishes = set(self.INGREDIENTS.keys())
        ingredients_available = {
            ingredient for ingredient
            in self.updated_inventory
            if self.updated_inventory[ingredient] > 0
        }
        dishes_available = set()

        for dish in all_dishes:
            if (
                set(self.INGREDIENTS[dish])
                .issubset(set(ingredients_available))
            ):
                dishes_available.add(dish)

        return dishes_available

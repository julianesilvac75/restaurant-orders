class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_total_dishes_ordered_per_customer(self, customer):
        counter = {}

        for order in self.orders:
            if order[0] == customer:
                if order[1] not in counter:
                    counter[order[1]] = 1
                else:
                    counter[order[1]] += 1

        return counter

    def get_quantity_by_order(self, order, customer):
        counter = self.get_total_dishes_ordered_per_customer(customer)

        return counter[order]

    def get_most_ordered_dish_per_customer(self, customer):
        counter = self.get_total_dishes_ordered_per_customer(customer)
        product = max(counter.items(), key=lambda x: x[1])[0]

        return product

    def get_never_ordered_per_customer(self, customer):
        total_orders = self.get_total_dishes_ordered_per_customer(customer)
        all_orders = set()
        for order in self.orders:
            all_orders.add(order[1])

        never_ordered = all_orders.difference(total_orders)
        return never_ordered

    def get_days_visited_per_customer(self, customer):
        days = set()

        for order in self.orders:
            if order[0] == customer:
                days.add(order[2])

        return days

    def get_days_never_visited_per_customer(self, customer):
        customer_days = self.get_days_visited_per_customer(customer)
        all_days = set()
        for order in self.orders:
            all_days.add(order[2])

        days_visited = all_days.difference(customer_days)
        return days_visited

    def get_customers_quantity_by_day(self):
        counter = {}

        for order in self.orders:
            if order[2] not in counter:
                counter[order[2]] = 1
            else:
                counter[order[2]] += 1

        return counter

    def get_busiest_day(self):
        counter = self.get_customers_quantity_by_day()
        day = max(counter.items(), key=lambda x: x[1])[0]

        return day

    def get_least_busy_day(self):
        counter = self.get_customers_quantity_by_day()
        day = min(counter.items(), key=lambda x: x[1])[0]

        return day

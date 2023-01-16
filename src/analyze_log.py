import csv


def get_logs(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as file:
            reader = csv.reader(file)
            return [line for line in reader]

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def orders_by_client(orders, client):
    counter = {}

    for order in orders:
        if order[0] == client:
            if order[1] not in counter:
                counter[order[1]] = 1
            else:
                counter[order[1]] += 1

    return counter


def product_quantity_by_client(orders, client, product):
    count = orders_by_client(orders, client)

    return count[product]


def most_ordered_by_client(orders, client):
    count = orders_by_client(orders, client)
    product = max(count.items(), key=lambda x: x[1])[0]

    return product


def get_products_list(orders):
    products = set()

    for order in orders:
        products.add(order[1])

    return products


def days_by_client(orders, client):
    counter = {}

    for order in orders:
        if order[0] == client:
            if order[2] not in counter:
                counter[order[2]] = 1
            else:
                counter[order[2]] += 1

    return counter


def get_all_days(orders):
    days = set()

    for order in orders:
        days.add(order[2])

    return days


def analyze_log(path_to_file):
    orders = get_logs(path_to_file)

    orders_maria = most_ordered_by_client(orders, "maria")
    burgers_arnaldo = (
        product_quantity_by_client(orders, "arnaldo", "hamburguer")
    )
    not_ordered_joao = (
        get_products_list(orders)
        .difference(orders_by_client(orders, "joao").keys())
    )
    days_not_went_joao = (
        get_all_days(orders)
        .difference(days_by_client(orders, "joao"))
    )

    print(days_not_went_joao)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{orders_maria}\n"
            f"{burgers_arnaldo}\n"
            f"{not_ordered_joao}\n"
            f"{days_not_went_joao}"
        )

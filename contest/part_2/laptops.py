class Laptop:
    def __init__(self, price, quality):
        self.price = price
        self.quality = quality


def get_laptops():
    laptops_count = int(input())
    laptops = []

    for i in range(laptops_count):
        [price, quality] = [int(val) for val in input().split()]
        laptops.append(Laptop(price, quality))

    return laptops


def better_laptop(laptops):
    sorted_by_price = sorted(laptops, key=lambda laptop: laptop.price)

    for index, laptop in enumerate(sorted_by_price):
        if index == 0:
            continue

        if laptop.quality < sorted_by_price[index - 1].quality:
            return "Happy Alex"

    return "Poor Alex"


laptops = get_laptops()
print(better_laptop(laptops))

assert (
    better_laptop([Laptop(100, 50), Laptop(120, 110), Laptop(80, 70)]) == "Happy Alex"
)

assert (
    better_laptop([Laptop(300, 200), Laptop(200, 100), Laptop(100, 90)]) == "Poor Alex"
)
assert (
    better_laptop(
        [
            Laptop(100, 100),
            Laptop(80, 89),
            Laptop(100, 120),
            Laptop(500, 430),
            Laptop(70, 90),
        ]
    )
    == "Happy Alex"
)

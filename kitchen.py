class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit, converter):
        return self

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, unit, converter):
        left_amount = converter.convert(self.left, unit)
        right_amount = converter.convert(self.right, unit)
        return Quantity(left_amount + right_amount, unit)


class Converter:
    def __init__(self):
        self.rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        self.rates[(from_unit, to_unit)] = rate

    def convert(self, quantity, to_unit):
        if quantity.unit == to_unit:
            return quantity.amount
        rate = self.rates[(quantity.unit, to_unit)]
        return quantity.amount * rate

    def reduce(self, source, unit):
        return source.reduce(unit, self)
      
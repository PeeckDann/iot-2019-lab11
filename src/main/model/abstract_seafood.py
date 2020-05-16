from src.main.model.product_condition import ProductCondition


class AbstractSeafood:

    def __init__(self, price_in_uah=0, producer='default_producer', species='default_species',
                 product_condition=ProductCondition(2)):
        self.price_in_uah = price_in_uah
        self.producer = producer
        self.species = species
        self.product_condition = product_condition

    def __str__(self):
        return "Price: {}, Producer: {}, Species: {}, Product condition: {}"\
            .format(self.price_in_uah, self.producer, self.species, self.product_condition)

    def __repr__(self):
        return "(Price: {}, Species: {})".format(self.price_in_uah, self.species)

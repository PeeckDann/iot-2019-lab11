from src.main.model.abstract_seafood import AbstractSeafood
from src.main.model.product_condition import ProductCondition


class Fish(AbstractSeafood):

    def __init__(self, price_in_uah=0, producer='default_producer', species='default_species',
                 product_condition=ProductCondition(2), product_category='default_product_category'):
        super().__init__(price_in_uah, producer, species, product_condition)
        self.product_category = product_category

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

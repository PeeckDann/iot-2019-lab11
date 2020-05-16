from abc import ABC
from src.main.model.product_condition import ProductCondition


class AbstractSeafood(ABC):

    def __init__(self, price_in_uah=0, producer='default_producer', species='default_species',
                 product_condition=ProductCondition(2)):
        self.price_in_uah = price_in_uah
        self.producer = producer
        self.species = species
        self.product_condition = product_condition

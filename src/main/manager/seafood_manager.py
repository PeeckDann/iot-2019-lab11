from src.main.model.product_condition import ProductCondition
from src.main.model.fish import Fish


class SeafoodManager:

    def __init__(self, seafood_list):
        self.seafood_list = seafood_list

    def add_seafood(self, seafood_list):
        self.seafood_list.extend(seafood_list)

    def find_seafood(self, species, product_condition):
        """
        Testing search method
        >>> seafood_manager.find_seafood("tuna", ProductCondition(2))
        [(Price: 10, Species: tuna), (Price: 20, Species: tuna)]
        """
        result_list = []
        for seafood in self.seafood_list:
            if seafood.species == species and seafood.product_condition == product_condition:
                result_list.append(seafood)
        return result_list


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, extraglobs={
        'seafood_manager': SeafoodManager(seafood_list=[Fish(10, "aaaaa", "tuna", ProductCondition(2),
                                                             "fillet"),
                                                        Fish(20, "bbbbb", "tuna", ProductCondition(2),
                                                             "fillet"),
                                                        Fish(30, "ccccc", "netuna", ProductCondition(2),
                                                             "fillet")])})

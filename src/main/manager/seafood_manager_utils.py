from src.main.model.sort_type import SortType
from src.main.model.fish import Fish


class SeafoodManagerUtils:

    @staticmethod
    def sort_by_price_in_uah(seafood_list, sort_type):
        """
        Testing sorting by price
        >>> fish_list = [Fish(30, "ccccc"), Fish(10, "aaaaa"), Fish(20, "bbbbb")]
        >>> SeafoodManagerUtils.sort_by_price_in_uah(fish_list, SortType(1))
        >>> print(fish_list[0].price_in_uah)
        10
        >>> print(fish_list[1].price_in_uah)
        20
        >>> print(fish_list[2].price_in_uah)
        30
        """
        if sort_type == SortType(1):
            seafood_list.sort(key=lambda seafood: seafood.price_in_uah)
        elif sort_type == SortType(2):
            seafood_list.sort(key=lambda seafood: seafood.price_in_uah, reverse=True)
        else:
            print("Can't sort")

    @staticmethod
    def sort_by_producer(seafood_list, sort_type):
        """
        Testing sorting by price
        >>> fish_list = [Fish(30, "ccccc"), Fish(10, "aaaaa"), Fish(20, "bbbbb")]
        >>> SeafoodManagerUtils.sort_by_producer(fish_list, SortType(1))
        >>> print(fish_list[0].producer)
        aaaaa
        >>> print(fish_list[1].producer)
        bbbbb
        >>> print(fish_list[2].producer)
        ccccc
        """
        if sort_type == SortType(1):
            seafood_list.sort(key=lambda seafood: seafood.producer)
        elif sort_type == SortType(2):
            seafood_list.sort(key=lambda seafood: seafood.producer, reverse=True)
        else:
            print("Can't sort")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

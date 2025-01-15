from abc import ABC, abstractmethod

class Game:

    def __init__(self, nb_max_turn):
        self.__nb_max_turn = nb_max_turn # dunder => double underscore ?
        self.__current_turn = 0

    @property
    def nb_max_turn(self):
        return self.__nb_max_turn

class GameBoard:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__content = [[]]
 
class Player(ABC):

    def __init__(self, pseudo : str):
        self.__pseudo = pseudo

    @property
    def pseudo(self):
        return self.__pseudo

    @abstractmethod
    def field_distance(self):
        pass


class Wolf(Player):

    def __init__(self, pseudo):
        super().__init__(pseudo)
        self.__field_distance = 2

    def field_distance(self):
        return self.__field_distance

class Villager(Player):
    def __init__(self, pseudo):
        super().__init__(pseudo)
        self.__field_distance = 1

    def field_distance(self):
        return self.__field_distance
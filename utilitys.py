from models import Card, Deck


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


class Iterator:
    """
    This class is Iterator of list cards (Object)
    and use from return element from list by
    him index
    """
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0

    def current(self):
        """
        This method return a current index
        :return: int
        """
        return self._current

    def set(self, index):
        """
        This method set a current index
        :param index: int
        """
        if self.is_done(index):
            self.current_item().visible = False
            self._current = index

    def current_item(self):
        """
        This method return cuurent card by card index in
        _current
        :return: None or Object of models.Card
        """
        if self._current is None:
            return None
        return self._list[self._current]

    def is_done(self, index):
        """
        This method check if index done from list
        :param index: int
        :return: bool
        """
        last_index = len(self._list) - 1
        return 0 <= index <= last_index

    def next(self):
        """
        This method a next element of list where
        card is not close another return None
        :return: None or Object of models.Card
        """
        current = self._current
        self.current_item().visible = False
        while True:
            self._current += 1
            if not self.is_done(self._current):
                self._current = 0
            if self.current_item().close is False:
                break
            if self._current == current:
                break
        if self._current == current:
            self._current = None
            return None
        self.current_item().visible = True
        return self.current_item()

    def get_item(self, index):
        """
        This method return a item by item index
        if index is not done then raise indexerror
        :exception: IndexError
        :param index: int
        :return: Object of models.Card
        """
        if not self.is_done(index):
            raise IndexError('Нет элемента с индексом: %d' % index)
        return self._list[index]


class LevelOne:
    """
    This is strategy pattern from get level
    """
    @staticmethod
    def getlevel():
        """
        Static method return a level data
        :return: dict
        """
        return {"cards": 52, "suit": False}


class LevelTwo:
    """
    This is strategy pattern from get level
    """
    @staticmethod
    def getlevel():
        """
        Static method return a level data
        :return: dict
        """
        return {"cards": 104, "suit": False}


class LevelThree:
    """
    This is strategy pattern from get level
    """
    @staticmethod
    def getlevel():
        """
        Static method return a level data
        :return: dict
        """
        return {"cards": 52, "suit": True}


class LevelFour:
    """
    This is strategy pattern from get level
    """
    @staticmethod
    def getlevel():
        """
        Static method return a level data
        :return: dict
        """
        return {"cards": 104, "suit": True}


class Generator:
    """
    This class generates a deck of cards by level
    """
    def __init__(self):
        """
        The method that creates the base variables
        in the class when the class is initialized
        """
        self.__class = object
        self.__data = {}
        self.__deck = []
        self.__cards = []

    def get(self):
        """
        This method return a dict data elements
        :return: dict
        """
        return {"deck": self.__deck, "suit": self.__data["suit"]}

    def set(self, level):
        """
        This method set and generate deck by level
        :param level: int 1..4
        :exception ValueError
        """
        if type(level) is int:
            if level == 1:
                self.__class = LevelOne
            elif level == 2:
                self.__class = LevelTwo
            elif level == 3:
                self.__class = LevelThree
            elif level == 4:
                self.__class = LevelFour
            else:
                raise ValueError("Level or 1 or 2 or 3 or 4")
            self.__data = self.__class.getlevel()
            for i in range(int(self.__data["cards"] / Card.data['card_in_deck'])):
                for j in range(1, int(Card.data['card_in_deck'] / 4) + 1):
                    self.__cards.append(Card(j, "diamonds"))
                    self.__cards.append(Card(j, "hearts"))
                    self.__cards.append(Card(j, "spades"))
                    self.__cards.append(Card(j, "clubs"))
                self.__deck.append(Deck(self.__cards))
                self.__cards = []
        else:
            raise ValueError("Level not integer value")

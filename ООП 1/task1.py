class HolidayObject:
    def __init__(self, name: str, importance: int) -> None:
        """
        :param name: Название объекта
        :param importance: Важность объекта по шкале от 1 до 10
        :raises ValueError: Если важность не входит в допустимый диапазон
        """
        if importance < 1 or importance > 10:
            raise ValueError("Важность должна быть в диапазоне от 1 до 10.")

        self.name = name
        self.importance = importance

    def celebrate(self) -> None:
        """
        Проаздование.

        Пример:
        >>> obj = HolidayObject("Party", 5)
        >>> obj.celebrate()
        """
        ...

    def prepare(self) -> None:
        """
        Подготовка к празднику.

        Пример:
        >>> obj = HolidayObject("Party", 5)
        >>> obj.prepare()
        """
        ...


class NewYearTree(HolidayObject):
    def __init__(self, name: str, importance: int, height: float) -> None:
        """
        :param name: Название ёлки
        :param importance: Важность ёлки по шкале от 1 до 10
        :param height: Высота ёлки в метрах
        :raises ValueError: Если высота отрицательная
        """
        super().__init__(name, importance)
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self.height = height

    def decorate(self) -> None:
        """
        Украшение ёлки.

        Пример:
        >>> tree = NewYearTree("Christmas Tree", 8, 2.5)
        >>> tree.decorate()
        """
        ...

    def light(self) -> None:
        """
        Зажигание огней на ёлке.

        Пример:
        >>> tree = NewYearTree("Christmas Tree", 8, 2.5)
        >>> tree.light()
        """
        ...


class SantaClaus(HolidayObject):
    def __init__(self, name: str, importance: int, speed: float) -> None:
        """
        :param name: Название
        :param importance: Важность по шкале от 1 до 10
        :param speed: Скорость передвижения персонажа
        :raises ValueError: Если скорость отрицательная
        """
        super().__init__(name, importance)
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом.")

        self.speed = speed

    def deliver_presents(self) -> None:
        """
        Доставка подарков.

        Пример:
        >>> santa = SantaClaus("Santa", 10, 1200.0)
        >>> santa.deliver_presents()
        """
        ...

    def ho_ho_ho(self) -> None:
        """
        Говорит "Ho Ho Ho".

        Пример:
        >>> santa = SantaClaus("Santa", 10, 1200.0)
        >>> santa.ho_ho_ho()
        """
        ...


class Snowman(HolidayObject):
    def __init__(self, name: str, importance: int, snow_amount: float) -> None:
        """
        :param name: Имя снеговика
        :param importance: Важность снеговика по шкале от 1 до 10
        :param snow_amount: Количество снега потребуется
        :raises ValueError: Если количество снега отрицательно
        """
        super().__init__(name, importance)
        if snow_amount <= 0:
            raise ValueError("Количество снега должно быть положительным числом.")

        self.snow_amount = snow_amount

    def build(self) -> None:
        """
        Постройка снеговика.

        Пример:
        >>> snowman = Snowman("Frosty", 6, 50.0)
        >>> snowman.build()
        """
        ...

    def melt(self) -> None:
        """
        Таять.

        Пример:
        >>> snowman = Snowman("Frosty", 6, 50.0)
        >>> snowman.melt()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# - `S - single responsibility` - принцип единственной ответственности.
#  Каждый класс должен решать одну задачу
# - `O - open/closed principle` - принцип открытости/закрытости.
# Программные сущности(классы, модули, функции) должны быть открыты для расширения, но не для модификации
# - `L - liskov substitution principle` - принцип подстановки Лисков.
# Не стоит изменять функционал наследника так, чтобы его использование вместо родителя приводило к ошибкам или не очевидному поведению
# - `I - interface segregation principle` - принцип разделения интерфейса.
#  Создавать детализированные интерфейсы, специфичные для конкретного клиента
# - `D - dependency inversion principle` - принцип инверсии зависимостей.
# Не нужно создавать зависимости в классе(зависеть от абстракций а не от реализации)
from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0 and not isinstance(value, (int, float)):
            raise ValueError("Значение радиуса должно быть положительным числом")
        self._radius = value
        return f"Значение радиуса изменено"

    def area(self):
        s = pi * (self._radius**2)
        return s

    def perimetr(self):
        p = 2 * pi * self._radius
        return p

    @classmethod
    def make_circle(cls, diametr: int):
        return cls(diametr / 2)

    def __str__(self):
        return f"Объект: {self.__class__.__name__}, его радиус - {self._radius}"


class Rectangle(Shape):
    def __init__(self, a_lenght: int, b_lenght: int):
        self._a_lenght = a_lenght
        self._b_lenght = b_lenght

    @property
    def a_lenght(self):
        return self._a_lenght

    @a_lenght.setter
    def a_lenght(self, value):
        if value <= 0 and not isinstance(value, (int, float)):
            raise ValueError("Значение длины должно быть целым положительным числом")
        self._a_lenght = value

    @property
    def b_lenght(self):
        return self._b_lenght

    @b_lenght.setter
    def b_lenght(self, value):
        if value <= 0 and not isinstance(value, (int, float)):
            raise ValueError("Значение длины должно быть целым положительным числом")
        self._b_lenght = value

    def area(self):
        s = self.a_lenght * self._b_lenght
        return s

    def perimetr(self):
        p = 2 * (self.a_lenght + self._b_lenght)
        return p

    @staticmethod
    def diagonal(a: int, b: int):
        return round(sqrt(a**2 + b**2), 2)

    def __str__(self):
        return f"Объект: {self.__class__.__name__}, длина его сторон - {self.a_lenght} и {self._b_lenght}"


class FiguresList:
    def __init__(self):
        self.list_figures = []

    def add_figure(self, figure: Shape):
        if not isinstance(figure, Shape):
            raise ValueError("Передан неправильный тип")
        self.list_figures.append(figure)
        return f"Фигура добавлена в список"

    def add_more_figures(self, *figures):
        for elem in figures:
            if not isinstance(elem, Shape):
                raise ValueError("Передан неправильный тип")
            self.list_figures.append(elem)

    def summary_area(self):
        result = 0
        for element in self.list_figures:
            result += element.area()
        return f"Общая площадь фигур в списке составляет - {result}"

    def __str__(self):
        return "\n".join(str(figure) for figure in self.list_figures)


circle1 = Circle(5)
circle2 = Circle(15)
# print(circle1.radius)
# circle1.radius = 11
# print(circle1.radius)
# print(circle1)
# print(circle1.area())
# print(circle2.area())
# print(circle1.perimetr())

rect1 = Rectangle(4, 7)
print("jopa")
print(Rectangle.diagonal(3, 5))
# print(rect1)
# print(rect1.a_lenght)
# print(rect1.b_lenght)
# rect1.b_lenght = 10
# print(rect1.b_lenght)
# print(rect1.area())
# print(rect1.perimetr())

fig_l = FiguresList()
fig_l.add_figure(circle1)
print(fig_l)

# fig_l.add_more_figures(circle2, rect1)
# print(fig_l)
# print(fig_l.summary_area())
lst = [Circle(51), Rectangle(4, 5), Rectangle(7, 8)]
fig_l.add_more_figures(*lst)
print(fig_l)
print(fig_l.summary_area())

print(Circle.make_circle(100))

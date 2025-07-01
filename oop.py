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
from math import pi


class Shape:

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        s = pi * (self.radius**2)
        return f"Площадь круга - {s}"

    def perimetr(self):
        p = 2 * pi * self.radius
        return f"Периметр круга - {p}"

    def __str__(self):
        return f"Объект: {self.__class__.__name__}, его радиус - {self.radius}"


class Rectangle(Shape):
    def __init__(self, a_lenght: int, b_lenght: int):
        self.a_lenght = a_lenght
        self.b_lenght = b_lenght

    def area(self):
        s = self.a_lenght * self.b_lenght
        return f"Площадь прямоугольника - {s}"

    def perimetr(self):
        p = 2 * (self.a_lenght + self.b_lenght)
        return f"Периметр прямоугольника - {p}"

    def __str__(self):
        return f"Объект: {self.__class__.__name__}, длина его сторон - {self.a_lenght} и {self.b_lenght}"


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
        return f"Все фигуры добавлены в список"

    def __str__(self):
        return "\n".join([str(figure) for figure in self.list_figures])


circle1 = Circle(5)
circle2 = Circle(15)
print(circle1)
print(circle1.area())
print(circle1.perimetr())

rect1 = Rectangle(4, 7)
print(rect1)
print(rect1.area())
print(rect1.perimetr())

fig_l = FiguresList()
fig_l.add_figure(circle1)
print(fig_l)
print("---")
fig_l.add_more_figures(circle2, rect1)
print(fig_l)

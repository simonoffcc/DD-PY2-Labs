"""
Идея: Реализация иерархии классов на примере сущностей "Задачи" и "Бага" в системе управления IT-проектами.
Суперкласс: Задача
Подкласс: Баг
"""""

from enum import unique, Enum


class TaskStatuses(Enum):
    """
    Класс-перечисление для удобной реализации валидации значения статуса задачи.
    Класс удобен тем, что позволяет быстро и просто расширять функционал класса Task,
    создавая новые значения статуса.

    Имеет защищенный атрибут UNDEFINED, который является значением статуса по умолчанию.

    Класс использует наследование от Enum для реализации перечисления.

    Поля описаны с помощью словарей, чтобы обозначить следующие параметры:
    validation_value - значение, которое используется для валидации.
                       Сравнивает значение кортежа со значением переданного пользователем статуса.
    actual_title - реальное значение, которое присваивается к полю класса после валидации.
    symbol - символ, который ассоциируется с соответствующим значением.
             Нужен для расширенной визуальной информации командной строки пользовательского интерфейса.
    Параметры передаются прямиком в TaskStatuses.__init__() как единый аргумент.
    """
    UNDEFINED = {
        'validation_value': 'undefined',
        'title': 'Undefined',
        'symbol': '?'
    }
    BACKLOG = {
        'validation_value': 'backlog',
        'title': 'Backlog',
        'symbol': '0'
    }
    TODO = {
        'validation_value': 'todo',
        'title': 'To Do',
        'symbol': '#'
    }
    INPROGRESS = {
        'validation_value': 'inprogress',
        'title': 'In Progress',
        'symbol': '~'
    }
    TESTING = {
        'validation_value': 'testing',
        'title': 'Testing',
        'symbol': '*'
    }
    DONE = {
        'validation_value': 'done',
        'title': 'Done',
        'symbol': 'X'
    }

    def __init__(self, values):
        self.validation_value = values['validation_value']
        self.title = values['title']
        self.symbol = values['symbol']


class TaskPriorities(Enum):
    """
    Класс-перечисление для удобной реализации валидации значения приоритета задачи.
    Класс удобен тем, что позволяет быстро и просто расширять функционал класса Task,
    создавая новые значения приоритета.

    Имеет защищенный атрибут UNDEFINED, который является значением приоритета по умолчанию.

    Класс использует наследование от Enum для реализации перечисления.

    Поля описаны с помощью словарей, чтобы обозначить следующие параметры:
    validation_value - значение, которое используется для валидации.
                       Сравнивает значение кортежа со значением переданного пользователем приоритета.
    actual_title - реальное значение, которое присваивается к полю класса после валидации.
    id - идентификатор приоритета, который ассоциируется с соответствующим значением.
         Нужен для предоставления расширенной визуальной информации пользовательскому интерфейсу командной строки.
    Параметры передаются прямиком в TaskPriorities.__init__() как единственный аргумент.
    """

    UNDEFINED = {
        'validation_value': 'undefined',
        'title': 'Undefined',
        'id': -1
    }
    ROUTINE = {
        'validation_value': 'routine',
        'title': 'Routine',
        'id': 0,
    }
    LOW = {
        'validation_value': 'low',
        'title': 'Low',
        'id': 1,
    }
    MEDIUM = {
        'validation_value': 'medium',
        'title': 'Medium',
        'id': 2,
    }
    HIGH = {
        'validation_value': 'high',
        'title': 'High',
        'id': 3,
    }
    BLOCKING = {
        'validation_value': 'blocking',
        'title': 'Blocking',
        'id': 4,
    }

    def __init__(self, values):
        self.validation_value = values['validation_value']
        self.title = values['title']
        self.id = values['id']


class Task:
    """ Супер-класс 'Задача'. """

    def __init__(self, title: str, description: str, *, status: str = None, priority: str = None):
        """
        Инициализация объекта "Задача".

        В параметрах конструктора указан символ "*", который обязывает передавать параметры именованно все аргументы,
        стоящие справа от него. Это необходимо для предотвращения ошибок во время валидации данных
        при путанице в порядке передачи аргументов конструктора.

        Поля заголовка и описания задачи являются защищёнными (с одним подчёркиванием). Подразумевается, что
        пользователь не будет обращаться к ним напрямую, однако это не нарушит целостность и логику работы приложения,
        так как заголовок и описание не являются значениями со строгой валидацией.

        Поля статуса и приоритета являются приватными (с двумя подчёркиваниями). Так как они используют
        классы-перечисления со строгими значениями, они не должны изменяться пользователем извне. Для этой задачи
        реализован как сеттер, так и методы для установки нового значения статуса и приоритета. Оба способа используют
        метод валидации данных.

        Параметры статуса и приоритета имеют значение по умолчанию None, которое обрабатывается в методах валидации
        данных.

        :param title: Заголовок задачи
        :param description: Описание задачи
        :param status: Текущий статус задачи
        :param priority: Приоритет задачи
        """

        self._title = title
        self._description = description
        self.__status = self.is_valid_status(status)
        self.__priority = self.is_valid_priority(priority)

    def __str__(self):
        """
        Возвращает строковое представление объекта в виде форматированной строки.

        :returns: Строковое представление объекта
        :rtype: str
        """
        result_str = f"[{self.get_symbol_by_status()}] Задача: {self._title}\n" \
                     f"\tСтатус: {self.__status}\n" \
                     f"\tПриоритет: {self.__priority} ({self.get_id_by_priority()})\n" \
                     f"\tОписание: {self._description}"
        return result_str

    def __repr__(self):
        """
        Возвращает представление объекта в виде валидного выражения Python.

        :returns: Валидное выражение Python
        :rtype: str
        """
        return f"{self.__class__.__name__}(title={self._title!r}, description={self._description!r}, " \
               f"status={self.__status!r}, priority={self.__priority!r})"

    @staticmethod
    def keep_only_latin_letters(string: str) -> str:
        """
        Удаляет из строки все символы, кроме букв из латиницы и кириллицы.

        Первоначально, необходим для работы функций валидации значений статуса и приоритета.
        Является методом с декоратором @staticmethod, т.к. не использует атрибуты экземпляра класса.

        :param string: Строка

        :returns: Строка без лишних символов - только латинские буквы
        :rtype: str
        """
        return ''.join(char for char in string if char.isalpha() and
                       (char.isascii() or 'а' <= char <= 'я' or 'А' <= char <= 'Я'))

    def is_valid_status(self, status_value: str) -> str:
        """
        Валидация значения статуса задачи при создании и изменении экземпляра класса.

        Функция сначала проверяет принадлежность статуса к строке.
        Затем с помощью генератора списка строк возможных значений из класса-перечисления статусов
        сравнивается проверяемая строка, из которой предварительно удалены все НЕ латинские символы, пробелы и
        которая приведена к нижнему регистру, с константным значением валидации.

        При ошибке валидации значения статуса в блоке try с генератором,
        принудительно генерируется исключение, а также выведется список с возможными значениями приоритета.

        :param status_value: Значение статуса

        :returns: Статус задачи
        :rtype: str

        :raises ValueError: Неверное значение статуса задачи
        """
        if status_value is None:
            return TaskStatuses.UNDEFINED.title
        if not isinstance(status_value, str):
            raise TypeError("Приоритет задачи должен быть строкой.")
        try:
            status_title = [status.title for status in TaskStatuses
                            if self.keep_only_latin_letters(status_value).replace(' ', '').lower()
                            == status.validation_value].pop()
        except IndexError:
            available_statuses = [status.title for status in TaskStatuses]
            raise ValueError("Неверное значение статуса задачи.\n"
                             f"Передано: {status_value!r}\n"
                             f"Поддерживаемые значения статуса: {available_statuses}.")
        else:
            return status_title

    def is_valid_priority(self, priority_value: str) -> str:
        """
        Валидация значения приоритета задачи при создании и изменении экземпляра класса.

        Функция сначала проверяет принадлежность приоритета к строке.
        Затем с помощью генератора списка строк возможных значений из класса-перечисления приоритетов
        сравнивается проверяемая строка, из которой предварительно удалены все НЕ латинские символы, пробелы и
        которая приведена к нижнему регистру, с константным значением для валидации.

        При ошибке валидации значения приоритета в блоке try с генератором,
        принудительно генерируется исключение, а также выведется список с возможными значениями приоритета.

        :param priority_value: Значение приоритета

        :returns: Приоритет задачи
        :rtype: str

        :raises ValueError: Неверное значение приоритета задачи
        """
        if priority_value is None:
            return TaskPriorities.UNDEFINED.title
        if not isinstance(priority_value, str):
            raise TypeError("Приоритет задачи должен быть строкой.")
        try:
            priority_title = [priority.title for priority in TaskPriorities
                              if self.keep_only_latin_letters(priority_value).replace(' ', '').lower()
                              == priority.validation_value].pop()
        except IndexError:
            available_priorities = [priority.title for priority in TaskPriorities]
            raise ValueError("Неверное значение приоритета задачи.\n"
                             f"Передано: {priority_value}\n"
                             f"Поддерживаемые значения приоритета: {available_priorities}.")
        else:
            return priority_title

    def get_symbol_by_status(self) -> str:
        """
        Возвращает ассоциативный символ, который отражает сущность текущего статуса.

        Необходим для методов, которые предоставляют информацию о задаче пользователю.

        :returns: Строковый символ
        :rtype: str

        :raises ValueError: Непредвиденная маловероятная ошибка при получение символа по статусу.
        """
        try:
            symbol = [status.symbol for status in TaskStatuses
                      if self.__status == status.title].pop()
        except IndexError as e:
            raise ValueError(f"Can't return symbol by status. Cause: {e}")
        else:
            return symbol

    def get_id_by_priority(self) -> int:
        """
        Возвращает ассоциативный идентификатор, который отражает сущность текущего приоритета.

        Необходим для методов, которые предоставляют информацию о задаче пользователю.

        :returns: Целочисленный идентификатор
        :rtype: int

        :raises ValueError: Непредвиденная маловероятная ошибка при получение идентификатора по приоритету.
        """
        try:
            id_ = [priority.id for priority in TaskPriorities
                   if self.__priority == priority.title].pop()
        except IndexError as e:
            raise ValueError(f"Can't return id by priority. Cause: {e}")
        else:
            return id_

    @property
    def status(self) -> str:
        """ Геттер статуса задачи. """
        return self.__status

    @status.setter
    def status(self, new_status: str) -> None:
        """ Сеттер статус задачи. """
        self.__status = self.is_valid_status(new_status)

    def set_status(self, new_status: str) -> None:
        """
        Меняет статус задачи.

        :param new_status: Новый статус задачи
        """
        self.__status = self.is_valid_status(new_status)

    @property
    def priority(self) -> str:
        """ Геттер приоритета задачи. """
        return self.__priority

    @priority.setter
    def priority(self, new_priority: str) -> None:
        """ Сеттер приоритета задачи. """
        self.__priority = self.is_valid_priority(new_priority)

    def set_priority(self, new_priority: str) -> None:
        """
        Устанавливает новый приоритет для задачи.

        :param new_priority: Новый приоритет для задачи
        """
        self.__priority = self.is_valid_priority(new_priority)

    def display_info(self, *, line_break: bool = True) -> None:
        """
        Выводит информацию о задаче.

        :param line_break: Параметр переноса строки. Если False, переноса строки после вывода информации нет.
        :type line_break: bool
        """
        task_info = f"[{self.get_symbol_by_status()}] " \
                    f"{self._title} " \
                    f"| Статус: {self.__status} " \
                    f"| Приоритет: {self.__priority} " \
                    f"\n\t> {self._description}"
        ending = '\n' if line_break else ''
        print(f"{task_info}{ending}")


class Bug(Task):
    """ Подкласс задачи - сущность Бага. """

    def __init__(self, title: str, description: str, *, status: str = None, priority: str = None,
                 category: str = None, responsible: str = None):
        """
        Инициализирует объект бага.

        Параметры категории и ответственного имеют значение по умолчанию None. Представленная реализация делает эти
        параметры необязательными при создании объекта, однако в теории эти данные должны обрабатываться методами
        валидации и принимать какие-либо осмысленные значения по умолчанию.

        :param title: Заголовок бага
        :param description: Описание бага
        :param status: Текущий статус бага
        :param priority: Приоритет устранения бага
        :param category: Категория бага (например, "функциональный", "синтаксический", "дизайн")
        :param responsible: Разработчик, список разработчиков или команда, ответственные за устранение бага
        """
        super().__init__(title, description, status=status, priority=priority)
        self._category = category
        self._responsible = responsible

    def __str__(self):
        """
        Возвращает строковое представление объекта в виде форматированной строки.

        Перегружен с использованием родительского метода __str__.

        :returns: Строковое представление объекта
        :rtype: str
        """
        result_str = f"{super().__str__()}\n" \
                     f"\tКатегория: {self._category}\n" \
                     f"\tОтветственный разработчик(и): {self._responsible}"
        return result_str

    def __repr__(self):
        """
        Возвращает представление объекта в виде валидного выражения Python.

        Перегружен с использованием родительского метода __repr__.

        :returns: Валидное выражение Python
        :rtype: str
        """
        return f"{super().__repr__()[:-1]}, category={self._category!r}, responsible={self._responsible!r})"

    @property
    def category(self) -> str:
        """ Геттер категории бага. """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """ Сеттер категории бага. """
        self._category = category

    def set_category(self, new_category: str) -> None:
        """
        Устанавливает значение категории бага.

        :param new_category: Новое значение категории
        """
        self._category = new_category

    @property
    def responsible(self) -> str:
        """ Геттер ответственного(ых) за устранение бага. """
        return self._responsible

    @responsible.setter
    def responsible(self, responsible: str) -> None:
        self._responsible = responsible

    def assign_new_responsible(self, new_responsible: str) -> None:
        """
        Назначает ещё одного(их) ответственного(ых) за устранение бага.

        :param new_responsible: Имя/имена ответственного(ых) ответственного
        """
        self._responsible += f", {new_responsible}"

    def change_responsible(self, new_responsible: str) -> None:
        """
        Переназначает ответственного(ых) за устранение бага.

        :param new_responsible: Имя/имена ответственного(ых) ответственного
        """
        self._responsible = new_responsible

    def display_info(self, line_break: bool = True) -> None:
        """
        Выводит информацию о задаче-баге.
        Расширение реализации метода отображения информации из родительского класса задачи.

        :param line_break: Параметр переноса строки. Если False, переноса строки после вывода информации нет.
        :type line_break: bool
        """
        super().display_info(line_break=False)
        bug_info = f"\tКатегория: {self._category} " \
                   f"| Ответственный разработчик: {self._responsible}"
        ending = '\n' if line_break else ''
        print(f"{bug_info}{ending}")


def test():
    try:
        task1 = Task('Новая фича', 'Идея на будущее для создания новой классной фичи', status='backlog', priority='medfdum')
    except Exception as e:
        print(e, end='\n\n')

    task2 = Task('Новая фича 2', 'Нужно добавить 2 новую классную фичу в приложение', status='to-do', priority='ro-utine')
    print(task2, end='\n\n')

    task3 = Task('Тестирование новой фичи', 'Написать тесты для новой фичи', priority='medium')
    print(task3, end='\n\n')
    task3.set_status('testing')
    print(task3, end='\n\n')
    task3.status = 'done'
    print(task3, end='\n\n')
    task3.display_info()

    task4 = Task('Новая фича 4', 'Нужно добавить новую классную фичу в приложение', status='to do')
    print(task4, end='\n\n')
    task4.display_info()
    task4.set_priority('medium')
    print(repr(task4), end='\n\n')
    task4.display_info(line_break=False)
    task4_2 = Task(title='Новая фича', description='Нужно добавить новую классную фичу в приложение', status='To Do', priority='Undefined')
    print(task4_2, end='\n\n')

    bug1 = Bug('Какой-то баг', 'Пофиксить баг в панели управления', status='to do', priority='high',
               category='interface',
               responsible='@simonoffcc')
    print(str(bug1), end='\n\n')
    print(repr(bug1), end='\n\n')
    bug1.display_info()
    bug1.set_category('интерфейс')
    bug1.assign_new_responsible('@jarko')
    print(bug1, end='\n\n')
    bug1.change_responsible("@pavel_durov")
    bug1.display_info()


if __name__ == '__main__':
    test()
    print('End of the test.')

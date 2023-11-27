import doctest


class Artist:
    """Сущность исполнителя"""

    def __init__(self, name: str, genre: str, country: str):
        """
        Создание и подготовка к работе объекта "Исполнитель"

        :param name: Имя исполнителя
        :param genre: Жанр музыки исполнителя
        :param country: Страна исполнителя

        При этом создаётся пустой список albums, который будет хранить альбомы исполнителя

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США") # инициализация экземпляра класса
        """
        self.name = name
        self.genre = genre
        self.country = country
        self.albums = []

    def add_album(self, album: 'Album') -> None:
        """
        Добавление альбома исполнителю

        :param album: Альбом

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> album1 = Album("Come Over When You're Sober, Pt. 1", artist1, 2017)
        >>> artist1.add_album(album1) # добавление исполнителю пустого альбома
        """
        if not isinstance(album, Album):
            raise TypeError("Альбомом может быть только объект класса \"Альбом\"")
        ...

    def get_country(self) -> str:
        """
        Получение страны исполнителя

        :return: Страна
        :rtype: str

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> country = artist1.get_country() # получение страны исполнителя
        """
        ...


class Album:
    """Сущность альбома"""

    def __init__(self, title: str, artist: 'Artist', release_year: int):
        """
        Создание и подготовка к работе объекта "Альбом"

        :param title: Название альбома
        :param artist: Исполнитель, которому принадлежит альбом
        :param release_year: Дата релиза альбома

        При этом создаётся пустой список songs, который будет хранить треки альбома

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США") # при инициализации альбома необходим объект исполнителя
        >>> album1 = Album("Come Over When You're Sober, Pt. 1", artist1, 2017) # инициализация экземпляра класса
        """
        if not isinstance(artist, Artist):
            raise TypeError("Исполнителем может быть только объект класса \"Исполнитель\"")
        self.artist = artist
        if not isinstance(release_year, int):
            raise TypeError("Дата выпуска альбома должна быть типа int")
        if release_year < 1878:
            raise ValueError("Дата выпуска альбома не может быть раньше, чем 1878 год")
        self.release_year = release_year
        self.title = title
        self.songs = []

    def add_song(self, song: 'Song') -> None:
        """
        Добавление трека в альбом

        :param song: Трек, который нужно добавить в альбом

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США") # при инициализации альбома необходим объект исполнителя
        >>> album1 = Album("Come Over When You're Sober, Pt. 1", artist1, 2017) # инициализация экземпляра класса
        >>> song1 = Song("Awful Things", artist1, 3.34) # создание объектов треков
        >>> album1.add_song(song1) # добавление трека в альбом
        """
        ...

    def get_size(self) -> int:
        """
        Получения кол-ва треков в альбоме

        :return: Кол-во треков в альбоме

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США") # при инициализации альбома необходим объект исполнителя
        >>> album1 = Album("Come Over When You're Sober, Pt. 1", artist1, 2017) # инициализация экземпляра класса
        >>> album1.get_size() # Получение кол-ва треков в альбоме (альбом пустой)

        >>> song1 = Song("Awful Things", artist1, 3.34) # создание объектов треков
        >>> album1.add_song(song1) # Добавление трека в альбом
        >>> album1.get_size() # Получение кол-ва треков в альбоме (1 трек в альбоме)
        """
        ...


class Song:
    """Сущность трека"""

    def __init__(self, title: str, artist: 'Artist', duration: float, lyrics: str = None):
        """
        Создание и подготовка к работе объекта "Трек"

        :param title: Название трека
        :param artist: Исполнитель, которому принадлежит трек
        :param duration: Продолжительность трека
        :param lyrics: Текст песни

        При этом создаётся атрибут album, по умолчанию равный None, который будет ссылаться на альбом

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> song1 = Song("Better Off (Dying)", artist1, 2.35) # инициализация экземпляра класса
        """
        self.title = title
        if not isinstance(artist, Artist):
            raise TypeError("Исполнителем может быть только объект класса \"Исполнитель\"")
        self.artist = artist
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность трека должна быть типа int или float")
        if duration <= 0:
            raise ValueError("Продолжительность трека должна быть положительным числом")
        self.duration = duration
        self.lyrics = lyrics
        self.album = None

    def set_album(self, album: 'Album') -> None:
        """
        Прикрепление трека к альбому

        :param album: Альбом

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> song1 = Song("U Said", artist1, 3.44)
        >>> album1 = Album("Come Over When You're Sober, Pt. 1", artist1, 2017)
        >>> song1.set_album(album1) # установка треку альбома
        """
        if not isinstance(album, Album):
            raise TypeError("Исполнителем может быть только объект класса \"Исполнитель\"")
        ...

    def play(self) -> None:
        """
        Проигрывание трека

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> song1 = Song("U Said", artist1, 3.44)
        >>> song1.play() # проигрывание трека
        """
        ...

    def get_duration_in_minutes_and_seconds(self) -> float:
        """
        Возвращает продолжительность трека в минутах и секундах

        :return: Продолжительность трека
        :rtype: float

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> song1 = Song("U Said", artist1, 3.44)
        >>> duration = song1.get_duration_in_minutes_and_seconds() # получение продолжительности трека
        """
        ...

    def add_lyrics(self, text: str) -> None:
        """
        Добавляет текст песни в объект трека

        Примеры:
        >>> artist1 = Artist("Lil Peep", "Эмо-рэп", "США")
        >>> song1 = Song("U Said", artist1, 3.44)
        >>> lyrics = "Runnin' away from you takes time and pain\\nAnd I don't even want to..."
        >>> song1.add_lyrics(lyrics)
        """
        ...


if __name__ == '__main__':
    doctest.testmod()  # тестирование примеров, которые находятся в документации

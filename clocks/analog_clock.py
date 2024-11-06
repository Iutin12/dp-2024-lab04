from interfaces.base_analog_clock import BaseAnalogClock
from consts.date_consts import DayNightDivision

class AnalogClock(BaseAnalogClock):
    def __init__(self) -> None:
        """
        Инициализирует экземпляр аналоговых часов с начальным значением для года, месяца, дня, углов стрелок
        и разделения на AM/PM

        :param year: Начальное значение года
        :param month: Начальное значение месяца
        :param day: Начальное значение дня месяца
        :param hour_angle: Начальный угол для стрелки часов
        :param minute_angle: Начальный угол для стрелки минут 
        :param second_angle: Начальный угол для стрелки секунд
        :param day_night_division: Начальное разделение на AM/PM 
        """
        self.year: int = 0
        self.month: int = 0
        self.day: int = 0
        self.hour_angle: float = 0.0
        self.minute_angle: float = 0.0
        self.second_angle: float = 0.0
        self.day_night_division: DayNightDivision = DayNightDivision.AM

    def set_date_time(self, year: int, month: int, day: int, hour_angle: float, minute_angle: float,
                      second_angle: float, day_night_division: DayNightDivision) -> None:
        """
        Устанавливает дату и время на аналоговых часах, включая углы для стрелок и деление на AM/PM

        :param year: Год, который нужно установить
        :param month: Месяц, который нужно установить
        :param day: День месяца, который нужно установить
        :param hour_angle: Угол для стрелки часов, который нужно установить
        :param minute_angle: Угол для стрелки минут, который нужно установить
        :param second_angle: Угол для стрелки секунд, который нужно установить
        :param day_night_division: Формат времени AM или PM
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        """
        Возвращает угол для стрелки часов
        """
        return self.hour_angle

    def get_minute_angle(self) -> float:
        """
        Возвращает угол для стрелки минут
        """
        return self.minute_angle

    def get_second_angle(self) -> float:
        """
        Возвращает угол для стрелки секунд
        """
        return self.second_angle

    def get_year(self) -> int:
        """
        Возвращает текущий год
        """
        return self.year

    def get_month(self) -> int:
        """
        Возвращает текущий месяц
        """
        return self.month

    def get_day(self) -> int:
        """
        Возвращает текущий день месяца
        """
        return self.day

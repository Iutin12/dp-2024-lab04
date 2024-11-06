from datetime import datetime
from consts.date_consts import DayNightDivision
from interfaces.base_analog_clock import BaseAnalogClock
from interfaces.base_digital_clock import BaseDigitalClock
from consts.translate import ClockConstants

class AnalogClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock: BaseAnalogClock) -> None:
        """
        Инициализирует адаптер для аналоговых часов.

        analog_clock - Экземпляр класса, реализующего интерфейс BaseAnalogClock
        """
        self.analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает дату и время на аналоговых часах

        date - Дата и время в формате datetime
        """

        year, month, day = date.year, date.month, date.day
        hour_angle, minute_angle, second_angle = self._calculate_time_angles(date)
        day_night_division = DayNightDivision.AM if date.hour < 12 else DayNightDivision.PM

        self.analog_clock.set_date_time(year, month, day, hour_angle, minute_angle, second_angle, day_night_division)

    def get_date_time(self) -> datetime:
        """
        Получает текущее время с аналоговых часов
        """

        year = self.analog_clock.get_year()
        month = self.analog_clock.get_month()
        day = self.analog_clock.get_day()


        hour_angle = self.analog_clock.get_hour_angle()
        minute_angle = self.analog_clock.get_minute_angle()
        second_angle = self.analog_clock.get_second_angle()

        hour, minute, second = self._calculate_time_from_angles(hour_angle, minute_angle, second_angle)

        return datetime(year, month, day, hour, minute, second)

    def _calculate_time_angles(self, date: datetime) -> tuple[float, float, float]:
        """
        Вычисляет углы для часов, минут и секунд на основе текущего времени

        date - Дата и время в формате datetime

        """
        hour_angle = (date.hour % 12) * ClockConstants.HOUR_ANGLE_PER_HOUR + (date.minute / 60) * ClockConstants.HOUR_ANGLE_PER_HOUR
        minute_angle = date.minute * ClockConstants.MINUTE_ANGLE_PER_MINUTE
        second_angle = date.second * ClockConstants.SECOND_ANGLE_PER_SECOND
        return hour_angle, minute_angle, second_angle

    def _calculate_time_from_angles(self, hour_angle: float, minute_angle: float, second_angle: float) -> tuple[int, int, int]:
        """
        Вычисление времени на основе углов

        hour_angle - Угол для часов
        minute_angle - Угол для минут
        second_angle - Угол для секунд
        """
        hour = int(hour_angle // ClockConstants.HOUR_ANGLE_PER_HOUR) % 12
        minute = int(minute_angle // ClockConstants.MINUTE_ANGLE_PER_MINUTE)
        second = int(second_angle // ClockConstants.SECOND_ANGLE_PER_SECOND)

        if self.analog_clock.day_night_division == DayNightDivision.PM and hour != 12:
            hour += 12
        elif self.analog_clock.day_night_division == DayNightDivision.AM and hour == 12:
            hour = 0

        return hour, minute, second
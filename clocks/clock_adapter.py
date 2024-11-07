from datetime import datetime
from consts.date_consts import DayNightDivision
from interfaces.base_analog_clock import BaseAnalogClock
from interfaces.base_digital_clock import BaseDigitalClock
from consts.translate import ClockConstants
from clocks.helper import ClockTimeHelper


class AnalogClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock: BaseAnalogClock) -> None:
        """
        Инициализирует адаптер для аналоговых часов.

        :param analog_clock: Экземпляр класса, реализующего интерфейс BaseAnalogClock, который будет адаптирован для использования как цифровые часы.
        """
        self._analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает дату и время на аналоговых часах, преобразуя их в углы для
        часов, минут и секунд, а также определяя AM/PM для правильного отображения.

        :param date: Дата и время, которые нужно установить на аналоговых часах
        """
        
        year, month, day = date.year, date.month, date.day

        time_angles = ClockTimeHelper.calculate_time_angles(date)

        day_night_division = DayNightDivision.AM if date.hour < ClockConstants.HOURS_IN_HALF_DAY else DayNightDivision.PM

        self._analog_clock.set_date_time(
            year, month, day,
            time_angles.hour_angle,
            time_angles.minute_angle,
            time_angles.second_angle,
            day_night_division
        )

    def get_date_time(self) -> datetime:
        """
        Получает текущее время с аналоговых часов, преобразуя углы времени в
        часы, минуты и секунды, и возвращает их в формате datetime.
        """

        year = self._analog_clock.get_year()
        month = self._analog_clock.get_month()
        day = self._analog_clock.get_day()

        hour_angle = self._analog_clock.get_hour_angle()
        minute_angle = self._analog_clock.get_minute_angle()
        second_angle = self._analog_clock.get_second_angle()

        clock_time = ClockTimeHelper.calculate_time_from_angles(hour_angle, minute_angle, second_angle)

        hour = ClockTimeHelper.adjust_for_day_night(clock_time.hour, self._analog_clock.day_night_division)

        return datetime(year, month, day, hour, clock_time.minute, clock_time.second)



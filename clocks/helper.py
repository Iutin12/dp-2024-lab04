from datetime import datetime
from consts.date_consts import DayNightDivision
from consts.translate import ClockConstants

class ClockTimeHelper:
    """
    Класс-хелпер для выполнения операций перевода углов стрелок в время и наоборот
    """

    @staticmethod
    def calculate_time_angles(date: datetime) -> tuple[float, float, float]:
        """
        Вычисляет углы для часов, минут и секунд на основе текущего времени

        :param date: Дата и время, на основе которых вычисляются углы
        """

        hour_angle = (date.hour % ClockConstants.HOURS_IN_HALF_DAY) * ClockConstants.HOUR_ANGLE_PER_HOUR + \
                     (date.minute / ClockConstants.MINUTES_IN_HOUR) * ClockConstants.HOUR_ANGLE_PER_HOUR
        minute_angle = date.minute * ClockConstants.MINUTE_ANGLE_PER_MINUTE
        second_angle = date.second * ClockConstants.SECOND_ANGLE_PER_SECOND
        return hour_angle, minute_angle, second_angle

    @staticmethod
    def calculate_time_from_angles(hour_angle: float, minute_angle: float, second_angle: float) -> tuple[int, int, int]:
        """
        Вычисляет время на основе углов для часов, минут и секунд

        :param hour_angle: Угол для часов
        :param minute_angle: Угол для минут
        :param second_angle: Угол для секунд
        """
        hour = int(hour_angle // ClockConstants.HOUR_ANGLE_PER_HOUR) % ClockConstants.HOURS_IN_HALF_DAY
        minute = int(minute_angle // ClockConstants.MINUTE_ANGLE_PER_MINUTE)
        second = int(second_angle // ClockConstants.SECOND_ANGLE_PER_SECOND)

        return hour, minute, second

    @staticmethod
    def adjust_for_day_night(hour: int, day_night_division: int) -> int:
        """
        Корректирует час для формата AM/PM

        :param hour: Час в 24-часовом формате
        :param day_night_division: Формат AM/PM
        """
        if day_night_division == DayNightDivision.PM and hour != ClockConstants.HOURS_IN_HALF_DAY:
            hour += ClockConstants.HOURS_IN_HALF_DAY
        elif day_night_division == DayNightDivision.AM and hour == ClockConstants.HOURS_IN_HALF_DAY:
            hour = 0

        return hour


class ClockConstants:
    """
    Класс для хранения констант, связанных с часами
    """
    # Время
    HOURS_IN_DAY = 24
    HOURS_IN_HALF_DAY = 12  # Часы в половине суток (AM/PM)
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60

    # Углы
    HOUR_ANGLE_PER_HOUR = 360 / HOURS_IN_HALF_DAY  # Угол для одного часа
    MINUTE_ANGLE_PER_MINUTE = 360 / SECONDS_IN_MINUTE  # Угол для одной минуты
    SECOND_ANGLE_PER_SECOND = 360 / SECONDS_IN_MINUTE  # Угол для одной секунды

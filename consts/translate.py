
class ClockConstants:
    """
    Класс для хранения констант, связанных с часами
    """
    # Время
    HOURS_IN_DAY = 24
    HOURS_IN_HALF_DAY = 12  # Часы в половине суток (AM/PM)
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    DEGREES = 360 # Всего градусов

    # Углы
    HOUR_ANGLE_PER_HOUR = DEGREES / HOURS_IN_HALF_DAY  # Угол для одного часа
    MINUTE_ANGLE_PER_MINUTE = DEGREES / SECONDS_IN_MINUTE  # Угол для одной минуты
    SECOND_ANGLE_PER_SECOND = DEGREES / SECONDS_IN_MINUTE  # Угол для одной секунды

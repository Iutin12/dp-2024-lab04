from dataclasses import dataclass

@dataclass
class TimeAngles:
    """
    Датакласс для хранения углов для часов, минут и секунд.
    """
    hour_angle: float
    minute_angle: float
    second_angle: float

@dataclass
class ClockTime:
    """
    Датакласс для хранения времени в формате (часы, минуты, секунды).
    """
    hour: int
    minute: int
    second: int
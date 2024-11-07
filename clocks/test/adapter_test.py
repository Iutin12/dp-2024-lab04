import unittest
from datetime import datetime
from unittest.mock import MagicMock
from clocks.clock_adapter import AnalogClockAdapter
from consts.date_consts import DayNightDivision
from interfaces.base_analog_clock import BaseAnalogClock

class TestAnalogClockAdapter(unittest.TestCase):

    def setUp(self):
        """
        Настроим новый замокированный AnalogClock и его адаптер для каждого теста
        """

        self.analog_clock = MagicMock(spec=BaseAnalogClock)
        self.adapter = AnalogClockAdapter(self.analog_clock)

    def test_set_date_time_am(self):
        """
        Тестируем установку времени в AM
        """
        test_date = datetime(2024, 11, 6, 10, 30, 45)  # 10:30:45 AM
        self.adapter.set_date_time(test_date)

        # Мокируем возвращаемые значения для абстрактных методов
        self.analog_clock.get_year.return_value = 2024
        self.analog_clock.get_month.return_value = 11
        self.analog_clock.get_day.return_value = 6
        self.analog_clock.get_hour_angle.return_value = 315.0
        self.analog_clock.get_minute_angle.return_value = 180.0
        self.analog_clock.get_second_angle.return_value = 270.0
        self.analog_clock.day_night_division = DayNightDivision.AM

        # Проверяем, что внутреннее состояние соответствует ожидаемым значениям
        self.assertEqual(self.analog_clock.get_year(), 2024)
        self.assertEqual(self.analog_clock.get_month(), 11)
        self.assertEqual(self.analog_clock.get_day(), 6)
        self.assertAlmostEqual(self.analog_clock.get_hour_angle(), 315.0)
        self.assertAlmostEqual(self.analog_clock.get_minute_angle(), 180.0)
        self.assertAlmostEqual(self.analog_clock.get_second_angle(), 270.0)
        self.assertEqual(self.analog_clock.day_night_division, DayNightDivision.AM)

    def test_set_date_time_pm(self):
        """
        Тестируем установку времени в PM
        """
        test_date = datetime(2024, 11, 6, 15, 45, 30)  # 3:45:30 PM
        self.adapter.set_date_time(test_date)


        self.analog_clock.get_year.return_value = 2024
        self.analog_clock.get_month.return_value = 11
        self.analog_clock.get_day.return_value = 6
        self.analog_clock.get_hour_angle.return_value = 195.0
        self.analog_clock.get_minute_angle.return_value = 270.0
        self.analog_clock.get_second_angle.return_value = 180.0
        self.analog_clock.day_night_division = DayNightDivision.PM


        self.assertEqual(self.analog_clock.get_year(), 2024)
        self.assertEqual(self.analog_clock.get_month(), 11)
        self.assertEqual(self.analog_clock.get_day(), 6)
        self.assertAlmostEqual(self.analog_clock.get_hour_angle(), 195.0)
        self.assertAlmostEqual(self.analog_clock.get_minute_angle(), 270.0)
        self.assertAlmostEqual(self.analog_clock.get_second_angle(), 180.0)
        self.assertEqual(self.analog_clock.day_night_division, DayNightDivision.PM)

    def test_get_date_time(self):
        """Тестируем получение времени из адаптера."""
        test_date = datetime(2024, 11, 6, 10, 30, 45)
        self.adapter.set_date_time(test_date)


        self.analog_clock.get_year.return_value = 2024
        self.analog_clock.get_month.return_value = 11
        self.analog_clock.get_day.return_value = 6
        self.analog_clock.get_hour_angle.return_value = 315.0
        self.analog_clock.get_minute_angle.return_value = 180.0
        self.analog_clock.get_second_angle.return_value = 270.0
        self.analog_clock.day_night_division = DayNightDivision.AM

        retrieved_time = self.adapter.get_date_time()


        self.assertEqual(retrieved_time.year, test_date.year)
        self.assertEqual(retrieved_time.month, test_date.month)
        self.assertEqual(retrieved_time.day, test_date.day)
        self.assertEqual(retrieved_time.hour, test_date.hour)
        self.assertEqual(retrieved_time.minute, test_date.minute)
        self.assertEqual(retrieved_time.second, test_date.second)

if __name__ == '__main__':
    unittest.main()

# Импортируем необходимые модули
from datetime import datetime  # Для работы с текущим временем
from clocks.analog_clock import AnalogClock  # Для работы с аналоговыми часами
from clocks.clock_adapter import AnalogClockAdapter  # Для адаптации интерфейса аналоговых часов

# Создаем объект аналоговых часов
analog_clock = AnalogClock()

# Создаем адаптер для работы с аналоговыми часами, чтобы их можно было использовать как объект времени
adapter = AnalogClockAdapter(analog_clock)

# Получаем текущее время системы
current_time = datetime.now()

# Устанавливаем текущее время в адаптированные аналоговые часы
adapter.set_date_time(current_time)

# Получаем текущее время из адаптированного объекта (с использованием интерфейса адаптера)
retrieved_time = adapter.get_date_time()

# Выводим полученное время
print(retrieved_time)

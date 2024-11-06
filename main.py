from datetime import datetime
from clocks.analog_clock import AnalogClock
from clocks.clock_adapter import AnalogClockAdapter

# Create an instance of AnalogClock
analog_clock = AnalogClock()

# Create an adapter for the analog clock
adapter = AnalogClockAdapter(analog_clock)

# Set date and time using a datetime object
current_time = datetime.now()
adapter.set_date_time(current_time)

# Get the current date and time as a datetime object
retrieved_time = adapter.get_date_time()
print(retrieved_time)

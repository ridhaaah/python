class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour      # private
        self.__minute = minute  # private
        self.__second = second  # private

    # Display function (optional)
    def show(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

    # Overload + operator
    def __add__(self, other):
        # Add seconds
        total_seconds = self.__second + other.__second
        carry_min = total_seconds // 60
        seconds = total_seconds % 60

        # Add minutes
        total_minutes = self.__minute + other.__minute + carry_min
        carry_hr = total_minutes // 60
        minutes = total_minutes % 60

        # Add hours
        hours = (self.__hour + other.__hour + carry_hr) % 24

        return Time(hours, minutes, seconds)


# Example usage
t1 = Time(5, 45, 30)
t2 = Time(3, 30, 45)

t3 = t1 + t2   # uses overloaded + operator

t3.show()

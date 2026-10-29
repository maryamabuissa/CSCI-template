class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        return s 

    def time_to_seconds(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def seconds_to_time(seconds):
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return Time(hour, minute, second)

    def add_time(self, hours, minutes, seconds):
        duration = Time(hours, minutes, seconds)
        seconds = self.time_to_seconds() + duration.time_to_seconds()
        return Time.seconds_to_time(seconds)


""" Some code to use Time"""

def main():
    now = Time(9, 4, 10)
    print(now.hour)
    end_of_class = now.add_time(0, 45, 51)
    print(f"Class will end at {end_of_class}")


if __name__ == "__main__":
    main()


```python
'''
Created on Nov 21, 2016

@author: simon.park
'''
def seconds_difference(time_1, time_2):
    return (time_2 - time_1)


def hours_difference(time_1, time_2):
    return (time_2 - time_1) /3600.0


def to_float_hours(hours, minutes, seconds):
    return (hours + minutes/60 + seconds/3600)


def to_24_hour_clock(hours):
    return (hours % 24)


def get_hours(seconds):
    return (seconds//3600)


def get_minutes(seconds):
    return (seconds//60)%60

def get_seconds(seconds):
    return seconds % 60


def time_to_utc(utc_offset, time):
    return (time - utc_offset) % 24


def time_from_utc(utc_offset, time):
    return (time + utc_offset) % 24



```

import math


def convert_millis(millis):
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = math.floor((millis / (1000 * 60 * 60)) % 24)
    return {
        'hours': str(hours).rjust(2, '0'),
        'minutes': str(minutes).rjust(2, '0'),
        'seconds': str(seconds).rjust(2, '0')
    }


def convert_to_secs(hours, minutes, seconds):
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

import math


def convertMillis(millis):
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

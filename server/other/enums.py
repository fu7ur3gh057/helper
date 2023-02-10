from enum import Enum


class Cities(Enum):
    BAKU = "Baku"
    SUMQAYIT = "Sumqayıt"
    GENCE = "Gəncə"
    QUBA = "Quba"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class AdvertisingTimeType(Enum):
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class OrderStatus(Enum):
    APPROVED = "Approved"
    CONSIDERED = "Considered"
    DENIED = "Denied"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class TimeInterval(Enum):
    five_sec = '5 sec'
    thirty_sec = '30 sec'
    one_min = '1 min'
    three_min = '3 mins'
    five_min = '5 mins'
    ten_min = '10 mins'
    thirty_min = '30 mins'
    one_hour = '1 hour'
    one_day = '1 day'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class TaskStatus(Enum):
    active = 'Active'
    disabled = 'Disabled'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

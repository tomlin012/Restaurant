import datetime


def utcnow() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)
import datetime
from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse


class DefinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text: str, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def is_due(self):
        if self.date <= datetime.datetime.now():
            return True
        return False

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

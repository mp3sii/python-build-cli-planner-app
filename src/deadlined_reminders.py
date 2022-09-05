import datetime
from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True


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

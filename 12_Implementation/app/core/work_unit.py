from dataclasses import dataclass

from .lesson_category import LessonCategory


@dataclass
class WorkUnit:
    subject: str
    topic: str
    category: LessonCategory

    @property
    def minimum_time(self):
        return self.category.duration_range[0]

    @property
    def maximum_time(self):
        return self.category.duration_range[1]

    @property
    def expected_time(self):
        return self.category.expected_duration
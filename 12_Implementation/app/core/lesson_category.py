from enum import Enum


class LessonCategory(Enum):
    BASIC = "Basic"
    MEDIUM = "Medium"
    HEAVY = "Heavy"
    PROJECT = "Project"

    @property
    def duration_range(self):
        return {
            LessonCategory.BASIC: (20, 35),
            LessonCategory.MEDIUM: (35, 60),
            LessonCategory.HEAVY: (75, 120),
            LessonCategory.PROJECT: (120, 180),
        }[self]

    @property
    def expected_duration(self):
        minimum, maximum = self.duration_range
        return (minimum + maximum) // 2
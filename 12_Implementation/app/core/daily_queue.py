class DailyQueue:

    def __init__(self):

        self.lessons = []
        self.completed = []
        self.deferred = []

    def load(self, timetable):

        self.lessons = list(timetable)
        self.completed = []
        self.deferred = []

    def current(self):

        if not self.lessons:
            return None

        return self.lessons[0]

    def complete_current(self):

        if not self.lessons:
            return None

        lesson = self.lessons.pop(0)
        self.completed.append(lesson)

        return lesson

    def defer_current(self):

        if not self.lessons:
            return None

        lesson = self.lessons.pop(0)
        self.deferred.append(lesson)

        return lesson

    def remaining(self):

        return list(self.lessons)

    def has_lessons(self):

        return len(self.lessons) > 0

    def summary(self):

        return {
            "completed": len(self.completed),
            "remaining": len(self.lessons),
            "deferred": len(self.deferred),
        }
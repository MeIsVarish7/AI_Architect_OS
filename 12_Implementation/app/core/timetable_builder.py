from app.core.progress_tracker import ProgressTracker


class TimetableBuilder:

    def __init__(self):

        self.progress = ProgressTracker()

    def build(self, work_units):

        timetable = []

        subjects = {}

        # Group all lessons by subject
        for lesson in work_units:

            subjects.setdefault(
                lesson.subject,
                []
            ).append(lesson)

        # Pick the current lesson for each subject
        for subject, lessons in subjects.items():

            index = self.progress.current_index(
                subject
            )

            if index >= len(lessons):
                continue

            timetable.append(
                lessons[index]
            )

        return timetable
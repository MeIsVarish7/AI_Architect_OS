from app.core.lesson_engine import LessonEngine
from app.core.progress_tracker import ProgressTracker


class SessionController:

    def __init__(self):

        self.engine = LessonEngine()
        self.progress = ProgressTracker()

    def run(self, queue):

        while queue.has_lessons():

            lesson = queue.current()

            result = self.engine.run(lesson)

            status = result["status"]

            if status == "completed":

                queue.complete_current()

                self.progress.advance(
                    lesson.subject
                )

                print(
                    f"\nLesson Completed "
                    f"({result['elapsed']})"
                )

                continue

            if status == "quit":

                print("\nSession Ended.")

                break

        print("\nToday's Session Summary")

        summary = queue.summary()

        print(
            f"Completed : "
            f"{summary['completed']}"
        )

        print(
            f"Remaining : "
            f"{summary['remaining']}"
        )

        print(
            f"Deferred  : "
            f"{summary['deferred']}"
        )
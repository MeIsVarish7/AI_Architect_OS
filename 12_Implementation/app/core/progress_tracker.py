import json
from pathlib import Path


class ProgressTracker:

    def __init__(self):

        self.file = (
            Path(__file__).parent.parent
            / "data"
            / "progress.json"
        )

        self.progress = {}

        self.load()

    def load(self):

        if self.file.exists():

            with open(self.file, "r", encoding="utf-8") as f:

                self.progress = json.load(f)

        else:

            self.progress = {}

            self.save()

    def save(self):

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            self.file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                self.progress,
                f,
                indent=4,
            )

    def current_index(self, subject):

        return self.progress.get(subject, 0)

    def next_lesson(self, subject):

        return self.current_index(subject)

    def advance(self, subject):

        current = self.current_index(subject)

        self.progress[subject] = current + 1

        self.save()

    def reset(self):

        self.progress = {}

        self.save()

    def set_progress(self, subject, index):

        self.progress[subject] = index

        self.save()

    def subject_completed(
        self,
        subject,
        total_lessons,
    ):

        return (
            self.current_index(subject)
            >= total_lessons
        )

    def all_progress(self):

        return dict(self.progress)
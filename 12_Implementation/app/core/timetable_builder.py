from app.core.focus_strategy import FocusStrategy


class TimetableBuilder:

    BUFFER_MINUTES = 15
    OVERSHOOT_TOLERANCE = 30

    def build(self, work_units, runtime):

        planning_target = max(
            0,
            runtime["available_minutes"] - self.BUFFER_MINUTES,
        )

        focus_blocks = (
            FocusStrategy()
            .create_focus_blocks(
                planning_target,
                runtime["energy"],
                runtime["weekday"],
            )
        )

        grouped = {}

        for lesson in work_units:
            grouped.setdefault(
                lesson.subject.strip(),
                []
            ).append(lesson)

        timetable = []
        planned_minutes = 0

        for block in focus_blocks:

            subject = block["subject"].strip()
            block_time = block["minutes"]

            if subject not in grouped:
                continue

            spent = 0

            for lesson in grouped[subject]:

                expected = (
                    lesson.minimum_time
                    + lesson.maximum_time
                ) // 2

                overshoot = (
                    spent + expected
                    - block_time
                )

                if (
                    spent != 0
                    and overshoot > self.OVERSHOOT_TOLERANCE
                ):
                    break

                timetable.append(
                    {
                        "lesson": lesson,
                        "expected_time": expected,
                        "priority": block["priority"],
                    }
                )

                spent += expected
                planned_minutes += expected

        return {
            "timetable": timetable,
            "planned_minutes": planned_minutes,
            "buffer_minutes": self.BUFFER_MINUTES,
        }
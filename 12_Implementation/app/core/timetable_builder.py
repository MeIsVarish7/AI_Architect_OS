from app.core.focus_strategy import FocusStrategy


class TimetableBuilder:

    BUFFER_MINUTES = 15
    OVERSHOOT_TOLERANCE = 30

    def build(self, work_units, available_minutes):

        planning_target = max(
            0,
            available_minutes - self.BUFFER_MINUTES,
        )

        focus_blocks = (
            FocusStrategy()
            .create_focus_blocks(planning_target)
        )

        grouped = {}

        for lesson in work_units:
            grouped.setdefault(
                lesson.subject,
                []
            ).append(lesson)

        timetable = []
        planned_minutes = 0

        for subject, block_time in focus_blocks.items():

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
                    }
                )

                spent += expected
                planned_minutes += expected

        return {
            "timetable": timetable,
            "planned_minutes": planned_minutes,
            "buffer_minutes": self.BUFFER_MINUTES,
        }
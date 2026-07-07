class TimetableBuilder:

    BUFFER_MINUTES = 15

    def build(self, work_units, available_minutes):

        planning_target = max(
            0,
            available_minutes - self.BUFFER_MINUTES
        )

        timetable = []
        planned_minutes = 0

        for unit in work_units:

            estimated_time = (
                unit.minimum_time + unit.maximum_time
            ) // 2

            if planned_minutes + estimated_time <= planning_target:

                timetable.append(
                    {
                        "lesson": unit,
                        "expected_time": estimated_time,
                    }
                )

                planned_minutes += estimated_time

        return {
            "timetable": timetable,
            "planned_minutes": planned_minutes,
            "buffer_minutes": self.BUFFER_MINUTES,
        }
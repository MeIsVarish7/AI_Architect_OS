class TimetableBuilder:

    def build(self, work_units, available_minutes):

        timetable = []

        used_minutes = 0

        for unit in work_units:

            if used_minutes + unit.minimum_time <= available_minutes:

                timetable.append(unit)
                used_minutes += unit.minimum_time

        return timetable
class PlanEditor:

    def choose_lesson(self, timetable):

        print("\n===== Edit Today's Plan =====\n")

        for index, item in enumerate(timetable, start=1):

            lesson = item["lesson"]

            print(f"[{index}] {lesson.subject} - {lesson.topic}")

        print("[0] Cancel")

        while True:

            try:

                choice = int(input("\nSelect lesson to replace: "))

                if 0 <= choice <= len(timetable):
                    return choice

            except ValueError:
                pass

            print("Invalid choice.")

    def choose_replacement(self, timetable, all_work_units):

        todays_topics = {
            item["lesson"].topic
            for item in timetable
        }

        subjects = []

        for unit in all_work_units:

            if (
                unit.subject not in subjects
                and unit.topic not in todays_topics
            ):
                subjects.append(unit.subject)

        print("\n===== Select Subject =====\n")

        for index, subject in enumerate(subjects, start=1):
            print(f"[{index}] {subject}")

        print("[0] Cancel")

        while True:

            try:

                choice = int(input("\nChoose subject: "))

                if choice == 0:
                    return None

                if 1 <= choice <= len(subjects):
                    selected_subject = subjects[choice - 1]
                    break

            except ValueError:
                pass

            print("Invalid choice.")

        available = []

        for unit in all_work_units:

            if (
                unit.subject == selected_subject
                and unit.topic not in todays_topics
            ):
                available.append(unit)

        print(f"\n===== {selected_subject} Lessons =====\n")

        for index, lesson in enumerate(available, start=1):
            print(f"[{index}] {lesson.topic}")

        print("[0] Cancel")

        while True:

            try:

                choice = int(input("\nChoose lesson: "))

                if choice == 0:
                    return None

                if 1 <= choice <= len(available):
                    return available[choice - 1]

            except ValueError:
                pass

            print("Invalid choice.")

    def replace(self, timetable, lesson_index, replacement):

        if lesson_index == 0:
            return timetable

        timetable[lesson_index - 1]["lesson"] = replacement

        timetable[lesson_index - 1]["expected_time"] = (
            replacement.minimum_time
            + replacement.maximum_time
        ) // 2

        return timetable
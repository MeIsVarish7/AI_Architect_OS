from app.core.menu import Menu
from app.core.plan_editor import PlanEditor


class SessionController:

    def display(self, session):

        print("\n========================================")
        print("Today's Plan")
        print("========================================\n")

        for index, item in enumerate(session["timetable"], start=1):

            lesson = item["lesson"]

            print(f"{index}. {lesson.subject}")
            print(f"   {lesson.topic}")
            print(f"   Expected: {item['expected_time']} min\n")

        planned = session["planned_minutes"]

        hours = planned // 60
        minutes = planned % 60

        print("----------------------------------------")
        print(f"Planned Study Time : {hours}h {minutes}m")
        print(f"Reserved Buffer    : {session['buffer_minutes']}m")
        print("----------------------------------------")

    def run(self, session, work_units):

        while True:

            self.display(session)

            choice = Menu().show()

            if choice == "S":

                print("\n========================================")
                print("Session Started")
                print("========================================\n")

                lesson = session["timetable"][0]["lesson"]

                print(f"Subject : {lesson.subject}")
                print(f"Topic   : {lesson.topic}")
                print(
                    f"Estimated Time : "
                    f"{session['timetable'][0]['expected_time']} min"
                )

                return

            if choice == "E":

                editor = PlanEditor()

                lesson = editor.choose_lesson(
                    session["timetable"]
                )

                if lesson == 0:
                    continue

                replacement = editor.choose_replacement(
                    session["timetable"],
                    work_units,
                )

                if replacement is None:
                    continue

                editor.replace(
                    session["timetable"],
                    lesson,
                    replacement,
                )

                print("\nPlan Updated.\n")

                continue

            if choice == "Q":

                print("\nSession Closed.")
                print("See you tomorrow.\n")

                return
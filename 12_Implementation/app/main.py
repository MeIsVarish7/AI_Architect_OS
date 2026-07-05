"""
AI Architect OS
Reference Implementation v1

Author: Varish Talekar
"""

from pathlib import Path

from app.core.health_check import HealthCheck
from app.core.context_engine import ContextEngine
from app.core.os_context import OSContext
from app.core.runtime_input import RuntimeInput
from app.core.curriculum_loader import CurriculumLoader
from app.core.timetable_builder import TimetableBuilder


class AIArchitectOS:

    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent

    def boot(self):

        print("=" * 50)
        print("        AI Architect OS")
        print("     Reference Implementation")
        print("=" * 50)
        print()

        HealthCheck(self.root).run()

        kernel = ContextEngine(self.root.parent).load_kernel()

        OSContext(kernel)

        runtime = RuntimeInput().get_runtime()

        available_minutes = runtime["available_time"] * 60

        work_units = CurriculumLoader().load()

        timetable = TimetableBuilder().build(
            work_units,
            available_minutes,
        )

        print("\n===== Today's Timetable =====\n")

        for index, lesson in enumerate(timetable, start=1):

            print(f"{index}. {lesson}")

        print("\nOperating System Ready.")


def main():
    AIArchitectOS().boot()


if __name__ == "__main__":
    main()
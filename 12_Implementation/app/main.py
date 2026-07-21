"""
AI Architect OS
Reference Implementation v1

Author: Varish Talekar
"""

from pathlib import Path

from app.core.context_engine import ContextEngine
from app.core.curriculum_loader import CurriculumLoader
from app.core.health_check import HealthCheck
from app.core.os_context import OSContext
from app.core.runtime_input import RuntimeInput
from app.core.session_controller import SessionController
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

        work_units = CurriculumLoader().load()

        session = TimetableBuilder().build(
            work_units,
            runtime,
        )

        SessionController().run(
            session,
            work_units,
        )


def main():

    AIArchitectOS().boot()


if __name__ == "__main__":
    main()
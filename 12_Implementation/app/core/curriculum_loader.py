from app.core.work_unit import WorkUnit


class CurriculumLoader:

    def load(self):

        return [

            WorkUnit(
                subject="Programming",
                topic="Python Functions",
                minimum_time=45,
                maximum_time=75,
            ),

            WorkUnit(
                subject="Mathematics",
                topic="Linear Algebra",
                minimum_time=60,
                maximum_time=90,
            ),

            WorkUnit(
                subject="DSA",
                topic="Arrays",
                minimum_time=45,
                maximum_time=60,
            ),

        ]
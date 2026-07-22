from app.core.lesson_category import LessonCategory
from app.core.work_unit import WorkUnit


class CurriculumLoader:

    def load(self):

        work_units = []

        programming = [
            ("Python Variables", LessonCategory.BASIC),
            ("Data Types", LessonCategory.BASIC),
            ("Operators", LessonCategory.BASIC),
            ("Conditional Statements", LessonCategory.MEDIUM),
            ("Loops", LessonCategory.MEDIUM),
            ("Functions", LessonCategory.MEDIUM),
            ("Modules & Packages", LessonCategory.MEDIUM),
            ("File Handling", LessonCategory.MEDIUM),
            ("Object Oriented Programming", LessonCategory.HEAVY),
            ("Exception Handling", LessonCategory.MEDIUM),
        ]

        dsa = [
            ("Arrays", LessonCategory.MEDIUM),
            ("Strings", LessonCategory.MEDIUM),
            ("Searching", LessonCategory.MEDIUM),
            ("Sorting", LessonCategory.HEAVY),
            ("Recursion", LessonCategory.HEAVY),
            ("Linked Lists", LessonCategory.HEAVY),
            ("Stacks", LessonCategory.MEDIUM),
            ("Queues", LessonCategory.MEDIUM),
            ("Trees", LessonCategory.HEAVY),
            ("Graphs", LessonCategory.HEAVY),
        ]

        mathematics = [
            ("Algebra", LessonCategory.MEDIUM),
            ("Functions", LessonCategory.MEDIUM),
            ("Matrices", LessonCategory.HEAVY),
            ("Linear Algebra", LessonCategory.HEAVY),
            ("Probability", LessonCategory.MEDIUM),
            ("Statistics", LessonCategory.MEDIUM),
            ("Calculus", LessonCategory.HEAVY),
            ("Optimization", LessonCategory.HEAVY),
        ]

        computer_science = [
            ("Computer Organization", LessonCategory.MEDIUM),
            ("Operating Systems", LessonCategory.HEAVY),
            ("Computer Networks", LessonCategory.HEAVY),
            ("DBMS", LessonCategory.HEAVY),
            ("System Design Basics", LessonCategory.HEAVY),
            ("Distributed Systems", LessonCategory.HEAVY),
            ("Compilers", LessonCategory.HEAVY),
            ("Concurrency", LessonCategory.HEAVY),
        ]

        ai = [
            ("Python for AI", LessonCategory.MEDIUM),
            ("NumPy", LessonCategory.MEDIUM),
            ("Pandas", LessonCategory.MEDIUM),
            ("Data Visualization", LessonCategory.MEDIUM),
            ("Machine Learning Basics", LessonCategory.HEAVY),
            ("Supervised Learning", LessonCategory.HEAVY),
            ("Neural Networks", LessonCategory.HEAVY),
            ("Deep Learning", LessonCategory.HEAVY),
            ("Transformers", LessonCategory.HEAVY),
            ("LLMs", LessonCategory.HEAVY),
        ]

        systems_engineering = [
            ("Linux Basics", LessonCategory.MEDIUM),
            ("Git", LessonCategory.BASIC),
            ("GitHub", LessonCategory.BASIC),
            ("Docker", LessonCategory.HEAVY),
            ("Cloud Fundamentals", LessonCategory.HEAVY),
            ("CI/CD", LessonCategory.HEAVY),
        ]

        projects = [
            ("Project Planning", LessonCategory.MEDIUM),
            ("Requirement Analysis", LessonCategory.MEDIUM),
            ("Architecture Design", LessonCategory.HEAVY),
            ("Implementation", LessonCategory.HEAVY),
            ("Testing", LessonCategory.MEDIUM),
            ("Deployment", LessonCategory.MEDIUM),
        ]

        research = [
            ("Reading Research Papers", LessonCategory.MEDIUM),
            ("Paper Summarization", LessonCategory.MEDIUM),
            ("Literature Review", LessonCategory.HEAVY),
            ("Research Methodology", LessonCategory.HEAVY),
            ("Experiment Design", LessonCategory.HEAVY),
            ("Writing Research Notes", LessonCategory.MEDIUM),
        ]

        communication = [
            ("Technical Writing", LessonCategory.MEDIUM),
            ("Presentation Skills", LessonCategory.MEDIUM),
            ("Documentation", LessonCategory.MEDIUM),
            ("Interview Communication", LessonCategory.MEDIUM),
            ("Resume Building", LessonCategory.MEDIUM),
        ]

        industry = [
            ("Open Source", LessonCategory.MEDIUM),
            ("GitHub Portfolio", LessonCategory.MEDIUM),
            ("System Design Interviews", LessonCategory.HEAVY),
            ("Behavioral Interviews", LessonCategory.MEDIUM),
            ("Resume Review", LessonCategory.MEDIUM),
        ]

        life = [
            ("Productivity", LessonCategory.BASIC),
            ("Time Management", LessonCategory.BASIC),
            ("Health & Fitness", LessonCategory.MEDIUM),
            ("Deep Work", LessonCategory.MEDIUM),
            ("Reflection", LessonCategory.BASIC),
        ]

        subject_map = {
            "Programming": programming,
            "DSA": dsa,
            "Mathematics": mathematics,
            "Computer Science": computer_science,
            "AI": ai,
            "Systems Engineering": systems_engineering,
            "Projects": projects,
            "Research": research,
            "Communication": communication,
            "Industry": industry,
            "Life": life,
        }

        for subject, lessons in subject_map.items():
            for topic, category in lessons:
                work_units.append(
                    WorkUnit(
                        subject=subject,
                        topic=topic,
                        category=category,
                    )
                )

        return work_units
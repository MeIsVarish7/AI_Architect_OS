from app.core.work_unit import WorkUnit


class CurriculumLoader:

    def load(self):

        work_units = []

        programming = [
            ("Python Variables", 30, 45),
            ("Data Types", 30, 45),
            ("Operators", 30, 45),
            ("Conditional Statements", 45, 60),
            ("Loops", 45, 60),
            ("Functions", 45, 75),
            ("Modules & Packages", 45, 60),
            ("File Handling", 45, 60),
            ("Object Oriented Programming", 60, 90),
            ("Exception Handling", 45, 60),
        ]

        dsa = [
            ("Arrays", 45, 60),
            ("Strings", 45, 60),
            ("Searching", 45, 60),
            ("Sorting", 60, 90),
            ("Recursion", 60, 90),
            ("Linked Lists", 60, 90),
            ("Stacks", 45, 60),
            ("Queues", 45, 60),
            ("Trees", 60, 90),
            ("Graphs", 60, 90),
        ]

        mathematics = [
            ("Algebra", 45, 60),
            ("Functions", 45, 60),
            ("Matrices", 60, 90),
            ("Linear Algebra", 60, 90),
            ("Probability", 45, 75),
            ("Statistics", 45, 75),
            ("Calculus", 60, 90),
            ("Optimization", 60, 90),
        ]

        computer_science = [
            ("Computer Organization", 45, 60),
            ("Operating Systems", 60, 90),
            ("Computer Networks", 60, 90),
            ("DBMS", 60, 90),
            ("System Design Basics", 60, 90),
            ("Distributed Systems", 60, 90),
            ("Compilers", 60, 90),
            ("Concurrency", 60, 90),
        ]

        ai = [
            ("Python for AI", 45, 60),
            ("NumPy", 45, 60),
            ("Pandas", 45, 60),
            ("Data Visualization", 45, 60),
            ("Machine Learning Basics", 60, 90),
            ("Supervised Learning", 60, 90),
            ("Neural Networks", 60, 90),
            ("Deep Learning", 60, 90),
            ("Transformers", 60, 90),
            ("LLMs", 60, 90),
        ]

        for topic, mn, mx in programming:
            work_units.append(
                WorkUnit(
                    subject="Programming",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in dsa:
            work_units.append(
                WorkUnit(
                    subject="DSA",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in mathematics:
            work_units.append(
                WorkUnit(
                    subject="Mathematics",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in computer_science:
            work_units.append(
                WorkUnit(
                    subject="Computer Science",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in ai:
            work_units.append(
                WorkUnit(
                    subject="AI",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        # ----- PART 2 CONTINUES HERE -----
        systems_engineering = [
            ("Linux Basics", 45, 60),
            ("Git", 30, 45),
            ("GitHub", 30, 45),
            ("Docker", 60, 90),
            ("Cloud Fundamentals", 60, 90),
            ("CI/CD", 60, 90),
        ]

        projects = [
            ("Project Planning", 45, 60),
            ("Requirement Analysis", 45, 60),
            ("Architecture Design", 60, 90),
            ("Implementation", 60, 90),
            ("Testing", 45, 60),
            ("Deployment", 45, 60),
        ]

        research = [
            ("Reading Research Papers", 45, 60),
            ("Paper Summarization", 45, 60),
            ("Literature Review", 60, 90),
            ("Research Methodology", 60, 90),
            ("Experiment Design", 60, 90),
            ("Writing Research Notes", 45, 60),
        ]

        communication = [
            ("Technical Writing", 45, 60),
            ("Presentation Skills", 45, 60),
            ("Documentation", 45, 60),
            ("Interview Communication", 45, 60),
            ("Resume Building", 45, 60),
        ]

        industry = [
            ("Open Source", 45, 60),
            ("GitHub Portfolio", 45, 60),
            ("System Design Interviews", 60, 90),
            ("Behavioral Interviews", 45, 60),
            ("Resume Review", 45, 60),
        ]

        life = [
            ("Productivity", 30, 45),
            ("Time Management", 30, 45),
            ("Health & Fitness", 45, 60),
            ("Deep Work", 45, 60),
            ("Reflection", 30, 45),
        ]

        for topic, mn, mx in systems_engineering:
            work_units.append(
                WorkUnit(
                    subject="Systems Engineering",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in projects:
            work_units.append(
                WorkUnit(
                    subject="Projects",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in research:
            work_units.append(
                WorkUnit(
                    subject="Research",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in communication:
            work_units.append(
                WorkUnit(
                    subject="Communication",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in industry:
            work_units.append(
                WorkUnit(
                    subject="Industry",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        for topic, mn, mx in life:
            work_units.append(
                WorkUnit(
                    subject="Life",
                    topic=topic,
                    minimum_time=mn,
                    maximum_time=mx,
                )
            )

        return work_units
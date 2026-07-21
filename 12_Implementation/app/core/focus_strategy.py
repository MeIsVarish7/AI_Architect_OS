class FocusStrategy:

    CORE_SUBJECTS = [
        "Programming",
        "DSA",
        "AI",
        "Mathematics",
    ]

    SECONDARY_SUBJECTS = [
        "Computer Science",
        "Projects",
        "Research",
        "Systems Engineering",
        "Communication",
        "Industry",
    ]

    def create_focus_blocks(
        self,
        available_minutes,
        energy,
        weekday,
    ):

        weekday = weekday.lower()

        weekend = weekday in [
            "friday",
            "saturday",
            "sunday",
        ]

        energy = energy.lower()

        if energy == "low":
            subject_count = 2

        elif energy == "medium":
            subject_count = 3

        else:
            subject_count = 4 if available_minutes >= 330 else 3

        subjects = self._select_subjects(
            weekend,
            subject_count,
            weekday,
        )

        weights = self._weights(len(subjects))

        blocks = []

        for subject, weight in zip(subjects, weights):

            blocks.append(
                {
                    "subject": subject,
                    "minutes": int(
                        available_minutes * weight
                    ),
                    "priority": (
                        "core"
                        if subject in self.CORE_SUBJECTS
                        else "secondary"
                    ),
                }
            )

        allocated = sum(
            block["minutes"]
            for block in blocks
        )

        difference = available_minutes - allocated

        if difference > 0:
            blocks[0]["minutes"] += difference

        return blocks

    def _select_subjects(
        self,
        weekend,
        subject_count,
        weekday,
    ):

        if weekend:

            rotation = {
                "friday": [
                    "Programming",
                    "Projects",
                    "Communication",
                    "Research",
                ],
                "saturday": [
                    "DSA",
                    "AI",
                    "Industry",
                    "Computer Science",
                ],
                "sunday": [
                    "Programming",
                    "Research",
                    "Systems Engineering",
                    "Mathematics",
                ],
            }

        else:

            rotation = {
                "monday": [
                    "Programming",
                    "DSA",
                    "AI",
                    "Research",
                ],
                "tuesday": [
                    "Programming",
                    "AI",
                    "Mathematics",
                    "Projects",
                ],
                "wednesday": [
                    "DSA",
                    "AI",
                    "Research",
                    "Programming",
                ],
                "thursday": [
                    "Programming",
                    "Mathematics",
                    "DSA",
                    "Communication",
                ],
            }

        return rotation.get(
            weekday,
            rotation[list(rotation.keys())[0]],
        )[:subject_count]

    def _weights(
        self,
        count,
    ):

        if count == 2:
            return [
                0.60,
                0.40,
            ]

        if count == 3:
            return [
                0.45,
                0.35,
                0.20,
            ]

        return [
            0.35,
            0.30,
            0.20,
            0.15,
        ]
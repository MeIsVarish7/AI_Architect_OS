class FocusStrategy:

    def create_focus_blocks(self, available_minutes):

        if available_minutes <= 120:

            return {
                "Programming": available_minutes,
            }

        if available_minutes <= 300:

            programming = int(available_minutes * 0.60)
            dsa = available_minutes - programming

            return {
                "Programming": programming,
                "DSA": dsa,
            }

        programming = int(available_minutes * 0.45)
        dsa = int(available_minutes * 0.35)
        mathematics = (
            available_minutes
            - programming
            - dsa
        )

        return {
            "Programming": programming,
            "DSA": dsa,
            "Mathematics": mathematics,
        }
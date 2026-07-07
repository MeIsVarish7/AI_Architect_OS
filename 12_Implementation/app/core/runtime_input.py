class RuntimeInput:

    MINUTE_OPTIONS = {
        "0": 0,
        "1": 15,
        "2": 30,
        "3": 45,
    }

    ENERGY_OPTIONS = {
        "L": "Low",
        "M": "Medium",
        "H": "High",
    }

    def get_runtime(self):

        print("\n===== Runtime Information =====\n")

        while True:

            try:

                hours = int(input("Hours : "))

                if hours < 0:
                    print("Hours cannot be negative.\n")
                    continue

                break

            except ValueError:
                print("Please enter a valid whole number.\n")

        print("\nMinutes")
        print("[0] 00")
        print("[1] 15")
        print("[2] 30")
        print("[3] 45")

        while True:

            minute_choice = input("\n> ").strip()

            if minute_choice in self.MINUTE_OPTIONS:
                break

            print("Choose 0, 1, 2 or 3.")

        available_minutes = (
            hours * 60
            + self.MINUTE_OPTIONS[minute_choice]
        )

        print("\nEnergy")
        print("[L] Low")
        print("[M] Medium")
        print("[H] High")

        while True:

            energy = input("\n> ").strip().upper()

            if energy in self.ENERGY_OPTIONS:
                break

            print("Choose L, M or H.")

        return {
            "available_minutes": available_minutes,
            "energy": self.ENERGY_OPTIONS[energy],
        }
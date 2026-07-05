class RuntimeInput:

    def get_runtime(self):

        print("\n===== Runtime Information =====\n")

        while True:

            try:
                available_time = float(
                    input("Available study time (hours): ")
                )

                if available_time <= 0:
                    print("Enter a value greater than 0.\n")
                    continue

                break

            except ValueError:
                print("Enter a valid number.\n")

        energy = input(
            "Energy Level (High / Medium / Low): "
        ).strip().capitalize()

        constraints = input(
            "Any constraints today? (Press Enter if none): "
        ).strip()

        return {
            "available_time": available_time,
            "energy": energy,
            "constraints": constraints,
        }
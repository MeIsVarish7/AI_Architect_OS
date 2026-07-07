class Menu:

    def show(self):

        while True:

            print("[S] Start Session")
            print("[E] Edit Today's Plan")
            print("[Q] Quit")

            choice = input("\n> ").strip().upper()

            if choice in ("S", "E", "Q"):
                return choice

            print("\nInvalid option.\n")
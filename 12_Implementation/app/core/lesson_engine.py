from app.core.timer import Timer
from app.core.prompt_generator import PromptGenerator


class LessonEngine:

    def __init__(self):

        self.timer = Timer()
        self.prompt_generator = PromptGenerator()

    def run(self, lesson):

        prompt = self.prompt_generator.generate(
            lesson
        )

        print("\n========================================")
        print("Lesson Started")
        print("========================================\n")

        print(f"Subject : {lesson.subject}")
        print(f"Lesson  : {lesson.topic}")
        print(f"Category: {lesson.category.name}")

        print("\n========================================")
        print("AI Prompt")
        print("========================================\n")

        print(prompt)

        print("\n========================================")
        print("Lesson Controls")
        print("========================================")

        print("[S] Start Timer")
        print("[P] Pause")
        print("[R] Resume")
        print("[F] Finish Lesson")
        print("[Q] Quit Lesson")

        started = False

        while True:

            choice = input("\n> ").strip().upper()

            if choice == "S":

                if not started:

                    self.timer.start()
                    started = True

                    print("\nTimer Started.")

                else:

                    print("\nTimer already running.")

                continue

            if choice == "P":

                self.timer.pause()

                print(
                    f"\nPaused at "
                    f"{self.timer.formatted_time()}"
                )

                continue

            if choice == "R":

                self.timer.resume()

                print("\nTimer Resumed.")

                continue

            if choice == "F":

                elapsed = self.timer.stop()

                return {
                    "status": "completed",
                    "elapsed_seconds": elapsed,
                    "elapsed": self.timer.formatted_time(),
                    "prompt": prompt,
                }

            if choice == "Q":

                elapsed = self.timer.stop()

                return {
                    "status": "quit",
                    "elapsed_seconds": elapsed,
                    "elapsed": self.timer.formatted_time(),
                    "prompt": prompt,
                }

            print("Invalid option.")
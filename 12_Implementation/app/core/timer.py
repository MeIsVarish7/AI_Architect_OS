import time


class Timer:

    def __init__(self):

        self.start_time = None
        self.pause_start = None
        self.paused_time = 0
        self.running = False
        self.paused = False

    def start(self):

        self.start_time = time.time()
        self.paused_time = 0
        self.running = True
        self.paused = False

    def pause(self):

        if self.running and not self.paused:

            self.pause_start = time.time()
            self.paused = True

    def resume(self):

        if self.running and self.paused:

            self.paused_time += (
                time.time() - self.pause_start
            )

            self.paused = False

    def stop(self):

        if not self.running:
            return 0

        elapsed = self.elapsed_seconds()

        self.running = False
        self.paused = False

        return elapsed

    def elapsed_seconds(self):

        if not self.running:
            return 0

        current = (
            self.pause_start
            if self.paused
            else time.time()
        )

        return int(
            current
            - self.start_time
            - self.paused_time
        )

    def formatted_time(self):

        seconds = self.elapsed_seconds()

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        return (
            f"{hours:02d}:"
            f"{minutes:02d}:"
            f"{secs:02d}"
        )
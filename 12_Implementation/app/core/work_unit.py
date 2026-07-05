class WorkUnit:

    def __init__(
        self,
        subject,
        topic,
        minimum_time,
        maximum_time,
    ):
        self.subject = subject
        self.topic = topic
        self.minimum_time = minimum_time
        self.maximum_time = maximum_time

    def __str__(self):
        return (
            f"{self.subject} | "
            f"{self.topic} | "
            f"{self.minimum_time}-{self.maximum_time} min"
        )
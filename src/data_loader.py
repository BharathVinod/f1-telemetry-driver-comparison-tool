import fastf1


class F1SessionConfig:
    def __init__(self, year, event, session_type):

        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")

        if not event:
            raise ValueError("Event cannot be empty.")

        if not session_type:
            raise ValueError("Session type cannot be empty.")

        self.year = year
        self.event = event
        self.session_type = session_type

    def display_info(self):
        print(f"Year: {self.year}")
        print(f"Event: {self.event}")
        print(f"Session: {self.session_type}")

    def load_session(self):
        session = fastf1.get_session(
            self.year,
            self.event,
            self.session_type
        )

        session.load()

        return session
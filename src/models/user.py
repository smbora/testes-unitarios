
class User:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.name == other.name and self.job == other.job
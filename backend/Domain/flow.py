from typing import List

from Domain.step import Step


class Flow:
    def __init__(self, name, user, steps: List[Step]):
        self.id = "ultimo id +1"
        self.name = name
        self.user = user
        self.steps = steps

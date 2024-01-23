from typing import Protocol

#Returns starting text could be anything random
class Generator(Protocol):
    def get_new_text(self, difficulty: int = 0) -> str:
        ...
        
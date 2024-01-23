from .gen import Generator

class SetGen(Generator):
    def get_new_text(self, difficulty: int = 0) -> str:
        return "the cat was in the house".lower()
    
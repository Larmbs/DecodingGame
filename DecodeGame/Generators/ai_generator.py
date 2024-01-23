from .gen import Generator

#GPT Engineer
#Uses OpenAi Api to generate text of varying length
class AIGen(Generator):
    def get_new_text(self, difficulty: int = 0) -> str:
        ...
        
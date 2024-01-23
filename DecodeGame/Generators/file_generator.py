from .gen import Generator
import random

#takes a file finds some random text and returns it
class FileGen(Generator):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        with open(file_name, "r") as f:
            self.lines = f.readlines()
        
    def get_new_text(self, difficulty: int = 0) -> str:
        rand_index = random.randint(0, len(self.lines)-2)  
        sentences = self.lines[rand_index].split(".")
        
        return sentences[0].lower()
        
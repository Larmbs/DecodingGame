from abc import ABC, abstractmethod

class Generator(ABC):
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def get_new_text(self, difficulty: int = 0) -> str:
        ...
        
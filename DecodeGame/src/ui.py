from typing import Protocol, TypeAlias
from .game_data import GameData


Table: TypeAlias = list[tuple[str, int]]

#Displays games current status
class UI(Protocol):  
    def set_game_data(self, game_data: GameData)  -> None:
        ... 
    #Returns response after game gets input from user
    def render(self, current_text: str, warning_message: str) -> str:
        ...
    
    def quit(self) -> None:
        ...
        
    def win(self) -> None:
        ...
        
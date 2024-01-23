from dataclasses import dataclass
from typing import TypeAlias, Protocol


Table: TypeAlias = list[tuple[str, int]]
Mapping: TypeAlias = dict[str, int]

@dataclass
class GameData(Protocol):
    original_text: str
    scrambled_text: str
    player_text: str
    
    occurences: Table
    
    scramble_mapping: Mapping
    current_player_mapping: Mapping
    
    guesses: int
    
    warning_message: str
    
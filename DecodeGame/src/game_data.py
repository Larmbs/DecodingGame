from .gen import Generator
from dataclasses import dataclass
from .scramble import scramble, create_default_mapping, get_occurences, apply_mapping
from typing import TypeAlias


Table: TypeAlias = list[tuple[str, int]]
Mapping: TypeAlias = dict[str, int]

#Structures game data
@dataclass
class GameData:
    original_text: str
    scrambled_text: str
    player_text: str
    
    occurences: Table
    
    scramble_mapping: Mapping
    current_player_mapping: Mapping
    
    guesses: int
    
    warning_message: str = ""
    
    def check_win(self) -> bool:
        return self.player_text == self.original_text
    
    #Takes in list of tuples signifying changes
    #Function takes tuple and changes player mapping to match the new ones
    def update_user_mapping(self, new_mappings = list[tuple[str, str]]) -> None:
        for key, value in new_mappings:
            self.current_player_mapping[key] = value
        self.guesses += 1
                
    def update_player_text(self) -> None:
        self.player_text = apply_mapping(self.scrambled_text, self.current_player_mapping)

#Creates new game data
def new_game(gen: Generator) -> GameData:
    original_text = gen.get_new_text()
    scrambled_text, scramble_mapping = scramble(original_text)
    
    player_text = scrambled_text
    occurences = get_occurences(scrambled_text)
    current_player_mapping = create_default_mapping()
    
    return GameData(
        original_text,
        scrambled_text,
        player_text,
        occurences,
        scramble_mapping,
        current_player_mapping,
        guesses=0,
    )

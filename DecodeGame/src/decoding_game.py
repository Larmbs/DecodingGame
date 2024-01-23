from .input_parser import parse_input
from .result import Result, State
from .game_data import GameData, new_game
from .ui import UI
from .gen import Generator
import sys


Instructions = \
"""To Reasign a letter do a > b, to string multiple reasignments seperate them with a ,"""

class DecodingGame:
    def __init__(self, gen: Generator, ui: UI):
        self.is_running = True
        self.gen = gen
        self.ui = ui
        
        #Creating a game data instance
        self.game_data: GameData = new_game(self.gen)
        
        #Updating UI text with game values
        self.ui.set_game_data(self.game_data)
        
        self.game_data.warning_message: str = "No Warning"
        
    def handle_input(self, user_input: str):
        #If an input is quit breakout instantly
        if user_input == "quit": return self.quit()
        
        results:list[Result] = parse_input(user_input)
        
        #Checks To see that all inputs are valid
        for res in results: 
            if res.state is State.Err: 
                self.game_data.warning_message = res.value
                return
        
        #From here on we know all inputed args are valid
        self.game_data.warning_message = "No Warning"
        #Removing the result type
        list_args = [item.value for item in results]
        
        self.game_data.update_user_mapping(list_args)
        self.game_data.update_player_text()

    def run(self):
        while self.is_running:
            self.handle_input(self.ui.render())
            if self.game_data.check_win(): self.win()
            
    def quit(self) -> None:
        self.is_running = False
        self.ui.quit()
        sys.exit()
        
    def win(self) -> None:
        self.is_running = False
        self.ui.win()
        sys.exit()
        
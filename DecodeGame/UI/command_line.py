from os import system, name
from colorama import Fore
from .game_data import GameData

Green = Fore.LIGHTGREEN_EX
Reset = Fore.RESET

def highlight_text(text: str) -> str:
    return Green+text+Reset

def underline_correct_parts(refrence_text: str, base_text: str) -> str:
    result = ""
    for i, char in enumerate(list(base_text)):
        if refrence_text[i] != char:
            result += char
        else:
            result += highlight_text(char)
    return result

def clear_terminal() -> None:
    if name == 'nt':  _ = system('cls') #Only for windows
    else: _ = system('clear') #Mac and Linux Clear
    
class CommandLineUI:    
    def set_game_data(self, game_data: GameData)  -> None:
        self.game_data = game_data 
                
    def display_table(self) -> None:
        print("Occur Percentages")
        index = 1
        for char, val in self.game_data.occurences:
            print(f"| {char} : {val}%".ljust(9) + "|", end="")
            if (index) % 5 == 0:
                print()
            index += 1
        print()

    #Returns response after game gets input from user
    def render(self) -> str:
        clear_terminal()
        print("Scrambled Text:\n"+self.game_data.scrambled_text, end="\n\n")
        
        self.display_table()
        print()
        
        print("Current Proggress:\n" + underline_correct_parts(self.game_data.original_text, self.game_data.player_text), end="\n\n")
        print(f"You have used {self.game_data.guesses}")
        print(self.game_data.warning_message + "\nEnter your next list of replacments:")
        return input()
    
    def win(self) -> None:
        clear_terminal()
        print("Correct Text:")
        print(Green+self.game_data.original_text)
        print(Green+"Great Work You Won!!!")
    
    def quit(self) -> None:
        clear_terminal()
        print("Quiting...")
        
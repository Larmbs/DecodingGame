from UI.command_line import CommandLineUI
from src.decoding_game import DecodingGame
from Generators.set_generator import SetGen
from Generators.file_generator import FileGen

#Config 
UI_TYPE = "CL" #Command Line = CD

def main():
    #gen = TestGen()
    gen = FileGen("test_file.txt")
    ui = CommandLineUI() if UI_TYPE == "CL" else None
    app = DecodingGame(gen, ui)
    
    app.run()

if __name__ == '__main__':
    main()
    
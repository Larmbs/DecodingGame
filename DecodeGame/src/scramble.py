import copy
import random
from typing import TypeAlias


LETTERS = list("abcdefghijklmnopqrstuvwxyz")

Table: TypeAlias = list[tuple[str, int]]
Mapping: TypeAlias = dict[str, int]


#Takes Normal text scrambles it then returns the unscramble keys and scrambled text
def scramble(text: str) -> tuple[str, Mapping]:
    mixup = create_mapping_dict()
    scrambled_text = apply_mapping(text, mixup)
    return (scrambled_text, mixup)

def create_mapping_dict() -> Mapping:
    scrambled_letters = copy.copy(LETTERS)
    random.shuffle(scrambled_letters)
    return dict(zip(LETTERS, scrambled_letters))

def apply_mapping(text: str, mixup: Mapping) -> str:
    translation_table = str.maketrans(mixup)
    return text.translate(translation_table)
    
def create_default_mapping() -> Mapping:
    normal_letters = copy.copy(LETTERS)
    return dict(zip(normal_letters, normal_letters))

#Returns a list of tuples containing charecters and their count sorted 
#refactor this it has errors
def get_occurences(text: str) -> Table:
    keys = list(text)
    d = dict.fromkeys(keys)
    to_pop = " ./"
    
    for char in list(to_pop):
        d.pop(char, None)
        
    total = len(keys)
    
    for char in d.keys():
        d[char] = int((text.count(char)/total)*100)
        
    l = list(d.items())
    l.sort(key=lambda x: x[1], reverse=True)
    return l

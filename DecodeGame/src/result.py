from dataclasses import dataclass
from enum import Enum, auto

DOC = """_summary_
    Helper data type inspired by rust Result<>
    Type has two states each storing its message
    If somthing failes return a Err message else a Ok message
    
    Returns:
        _type_: _description_
    """

class State(Enum):
    Ok = auto()
    Err = auto()

@dataclass
class Result:
    value: object
    state: State
    @staticmethod
    def Ok(value:str) -> "Result":
        return Result(value, State.Ok)
    @staticmethod
    def Err(value:str) -> "Result":
        return Result(value, State.Err)
    def __str__(self) -> str:
        return "Ok" if self.state is State.Ok else "Err"
    def __repr__(self) -> str:
        return ("Ok" if self.state is State.Ok else "Err") + f"({self.value})"
    
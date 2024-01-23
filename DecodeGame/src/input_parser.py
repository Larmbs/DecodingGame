from .result import Result

def is_valid(parsed_single_arg: tuple[str]) -> Result:
    if len(parsed_single_arg) != 2: return Result.Err("Inputed Argument was Invalid")
    
    for arg in parsed_single_arg:
        if len(arg) != 1: return Result.Err("Inputed Argument was Invalid")
        
    return Result.Ok(parsed_single_arg)
    
def parse_single(single_arg: str) -> Result:
    tup = tuple(single_arg.strip().split(">"))
    return is_valid((tup[0].strip(), tup[1].strip()))

def parse_input(raw_input: str) -> list[Result]:
    if not raw_input:
        return [Result.Err("Nothing was inputed")]
    split_input = raw_input.lower().split(",")
    result = []
    for arg in split_input:
        result.append(parse_single(arg))
    return result
        
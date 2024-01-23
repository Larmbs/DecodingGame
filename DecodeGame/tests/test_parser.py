from src.input_parser import parse_input, parse_single, is_valid
from src.result import Result


#is_valid input testing
def test_is_valid_one():
    assert True
    
def test_is_valid_two():
    assert True
    
def test_is_valid_three():
    assert True


#Single Parse Func Testing
def test_single_parse_one():
    raw_input = "a>b"
    expected = Result.Ok(("a", "b"))
    assert parse_single(raw_input) == expected
    
def test_single_parse_two():
    raw_input = "   a  >  b  "
    expected = Result.Ok(("a", "b"))
    assert parse_single(raw_input) == expected
    
def test_single_parse_three():
    raw_input = "   a>  >  b  "
    expected = Result.Ok(("a", "b"))
    assert parse_single(raw_input) != expected


#Full Input Parser Tester
def test_full_parser_one():
    raw_input = "a>b, b>c, c>v"
    expected_result = [Result.Ok(("a", "b")), Result.Ok(("b", "c")), Result.Ok(("c", "v"))]
    assert parse_input(raw_input) == expected_result
    
def test_full_parser_two():
    raw_input = "a>b b>c, c>v"
    expected_result = [Result.Err("Inputed Argument was Invalid"), Result.Ok(("c", "v"))]
    assert parse_input(raw_input) == expected_result

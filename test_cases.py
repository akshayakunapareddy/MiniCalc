from lexer import Lexer
from parser import Parser
from evaluator import evaluate

def test(expression, expected_result):
    tokens = Lexer(expression).get_tokens()
    ast = Parser(tokens).parse()
    result = evaluate(ast)
    assert result == expected_result, f"Test failed for: {expression}"
    print(f"✅ Passed: {expression} = {result}")

if __name__ == "__main__":
    test("3 + 5", 8)
    test("10 - 2", 8)
    test("3 + 5 * 2", 13)
    test("3 * (2 + 4)", 18)
    test("(10 - 2) / 2", 4)
    print("All tests passed! 🎉")

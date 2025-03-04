from lexer import Lexer
from parser import Parser
from evaluator import evaluate

def run(code):
    """Run the toy compiler on an input expression."""
    tokens = Lexer(code).get_tokens()
    ast = Parser(tokens).parse()
    result = evaluate(ast)

    print(f"Input: {code}")
    print(f"Tokens: {tokens}")
    print(f"AST: {ast}")
    print(f"Result: {result}")

if __name__ == "__main__":
    while True:
        code = input("MiniCalc > ")
        if code.lower() in ["exit", "quit"]:
            break
        run(code)

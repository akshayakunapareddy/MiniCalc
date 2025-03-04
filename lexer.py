import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        for match in re.finditer(TOKEN_REGEX, self.code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'SKIP':
                self.tokens.append((kind, value))

    def get_tokens(self):
        return self.tokens

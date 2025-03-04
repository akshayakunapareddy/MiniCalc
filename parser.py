class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0  

    def peek(self):
        """Return the current token without consuming it."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def consume(self, expected_type):
        """Consume a token if it matches the expected type, else raise an error."""
        token = self.peek()
        if token[0] == expected_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {expected_type}, got {token}")

    def factor(self):
        """factor → NUMBER | '(' expr ')'"""
        token = self.peek()
        if token[0] == 'NUMBER':
            return self.consume('NUMBER')
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            node = self.expr()
            self.consume('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def term(self):
        """term → factor ( ('*' | '/') factor )*"""
        node = self.factor()
        while self.peek()[0] in ('MUL', 'DIV'):
            op = self.consume(self.peek()[0])
            right = self.factor()
            node = (op, node, right)
        return node

    def expr(self):
        """expr → term ( ('+' | '-') term )*"""
        node = self.term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op = self.consume(self.peek()[0])
            right = self.term()
            node = (op, node, right)
        return node

    def parse(self):
        """Parse the full expression and return the AST."""
        return self.expr()

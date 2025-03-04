def evaluate(node):
    """Evaluate the AST recursively."""
    if isinstance(node, tuple):  # It's an operation
        op, left, right = node
        left_val = evaluate(left)
        right_val = evaluate(right)

        if op[0] == 'PLUS': return left_val + right_val
        if op[0] == 'MINUS': return left_val - right_val
        if op[0] == 'MUL': return left_val * right_val
        if op[0] == 'DIV': return left_val / right_val
    else:
        return int(node[1])  # It's a number token

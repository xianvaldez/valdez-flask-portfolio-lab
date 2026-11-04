import re


def infix_to_postfix(expression):
    tokens = re.findall(
        r'\d+(?:\.\d+)?|[A-Za-z_]\w*|[()+\-*/^]',
        expression
    )

    if ''.join(tokens).replace(' ', '') != expression.replace(' ', ''):
        raise ValueError("Invalid characters in expression.")

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    output = []
    operators = []

    for token in tokens:
        if re.fullmatch(r'\d+(?:\.\d+)?|[A-Za-z_]\w*', token):
            output.append(token)

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())

            if not operators:
                raise ValueError("Mismatched parentheses.")

            operators.pop()

        else:
            while (
                operators
                and operators[-1] != '('
                and (
                    precedence[operators[-1]] > precedence[token]
                    or (
                        precedence[operators[-1]] == precedence[token]
                        and token != '^'
                    )
                )
            ):
                output.append(operators.pop())

            operators.append(token)

    if '(' in operators:
        raise ValueError("Mismatched parentheses.")

    while operators:
        output.append(operators.pop())

    return ' '.join(output)

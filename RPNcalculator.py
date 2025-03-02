def evaluate_rpn(expression, stack=None):
    if stack is None:
        stack = []

    if not expression:
        return stack[0] if stack else None

    current = expression.pop(0)

    if current.isdigit() or (current[0] == '-' and current[1:].isdigit()):
        stack.append(int(current))
    else:
        second = stack.pop()
        first = stack.pop()

        if current == '+':
            stack.append(first + second)
        elif current == '-':
            stack.append(first - second)
        elif current == '*':
            stack.append(first * second)
        elif current == '/':
            stack.append(int(first / second))

    return evaluate_rpn(expression, stack)

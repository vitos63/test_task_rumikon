def from_infix_to_postfix(expression: str) -> list[str] | str:
    """Функция, которая переводит выражение из инфиксной записи в постфиксную"""
    answer = ["0"]
    stack = []

    for i in range(len(expression)):
        symbol = expression[i]

        if symbol == " ":
            if expression[i - 1].isdigit() and i + 1 < len(expression) and expression[i + 1].isdigit():
                return "Недопустимое выражение"
            continue

        elif symbol.isdigit():
            if answer[-1] == "0":
                if i - 1 >= 0 and expression[i - 1] == "-":
                    answer.append(symbol)
                else:
                    answer[-1] = symbol

            elif answer and expression[i - 1].isdigit():
                answer[-1] += symbol
                continue

            else:
                answer.append(symbol)

        elif symbol in ["x", "y", "z"]:
            if answer[-1] == "0":
                if i - 1 >= 0 and expression[i - 1] == "-":
                    answer.append(symbol)
                else:
                    answer[-1] = symbol
            else:
                answer.append(symbol)

        elif symbol in ["+", "-"]:
            while stack and stack[-1] in ["+", "-", "*"]:
                answer.append(stack.pop())

            stack.append(symbol)

        elif symbol == "*":
            while stack and stack[-1] == "*":
                answer.append(stack.pop())

            stack.append(symbol)

        elif symbol == "(":
            stack.append("(")
            if answer[-1] != "0":
                answer.append("0")

        elif symbol == ")":
            while stack and stack[-1] != "(":
                answer.append(stack.pop())

            if not stack:
                return "Недопустимое выражение"

            stack.pop()

        else:
            return "Недопустимое выражение"

    while stack:
        answer.append(stack.pop())

    return answer

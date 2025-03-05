from from_infix_to_postfix import from_infix_to_postfix
from operations_with_letters import operations_with_letters


def simplify_the_expression(expression: str) -> str:
    """Функция, которая получает выражение и упрощает его"""
    postfix_expression = from_infix_to_postfix(expression)
    result = []
    if "(" in postfix_expression or ")" in postfix_expression:
        return "Недопустимое выражение"

    try:
        for symbol in postfix_expression:
            if symbol.isdigit() or symbol.isalpha():
                result.append(symbol)

            elif symbol == "-":
                try:
                    result[-2] = str(int(result[-2]) - int(result[-1]))

                except ValueError:
                    result[-2] = operations_with_letters(result[-1], result[-2], "-")

                result.pop()

            elif symbol == "+":
                try:
                    result[-2] = str(int(result[-2]) + int(result[-1]))

                except ValueError:
                    result[-2] = operations_with_letters(result[-1], result[-2], "+")

                result.pop()
            elif symbol == "*":
                try:
                    result[-2] = str(int(result[-2]) * int(result[-1]))

                except ValueError:
                    result[-2] = operations_with_letters(result[-1], result[-2], "*")

                result.pop()
        result = "".join(result)
        return result if result else "0"

    except:
        return "Недопустимое выражение"

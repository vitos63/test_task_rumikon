def operations_with_letters(expression_1: str, expression_2: str, operation: str) -> str:
    """Функция, которая выполняет различные операции с выражениями, содержащими буквы"""
    expression_1_as_dict = convert_expression(expression_1)
    expression_2_as_dict = convert_expression(expression_2)
    result_dict = {}
    answer = []

    if operation == "+":
        for key in expression_1_as_dict:
            result_dict[key] = expression_1_as_dict[key] + expression_2_as_dict.get(key, 0)

        for key in expression_2_as_dict:
            if key not in result_dict:
                result_dict[key] = expression_2_as_dict[key]

    elif operation == "-":
        for key in expression_1_as_dict:
            result_dict[key] = expression_2_as_dict.get(key, 0) - expression_1_as_dict[key]

        for key in expression_2_as_dict:
            if key not in result_dict:
                result_dict[key] = expression_2_as_dict[key]

    elif operation == "*":
        for key_1 in expression_1_as_dict:
            for key_2 in expression_2_as_dict:
                if key_1 == "digits":
                    result_dict[key_2] = (result_dict.get(key_2, 0)
                        + expression_1_as_dict[key_1] * expression_2_as_dict[key_2]
                        )

                elif key_2 == "digits":
                    result_dict[key_1] = (result_dict.get(key_1, 0)
                        + expression_1_as_dict[key_1] * expression_2_as_dict[key_2]
                        )

                else:
                    result_dict[key_1 + key_2] = (result_dict.get(key_1 + key_2, 0)
                        + expression_1_as_dict[key_1] * expression_2_as_dict[key_2]
                        )

    for key in result_dict:
        if result_dict[key] == 0:
            continue

        else:
            if key != "digits":
                if not answer and result_dict[key] > 0:
                    if result_dict[key] != 1:
                        answer.append(f"{result_dict[key]}*")
                        answer[-1] += "*".join(key)
                    else:
                        answer.append("*".join(key))

                elif result_dict[key] > 0:
                    answer.append("+")
                    if result_dict[key] != 1:
                        answer.append(f"{result_dict[key]}*")
                        answer[-1] += "*".join(key)
                    else:
                        answer.append("*".join(key))

                else:
                    if result_dict[key] == -1:
                        answer.append("-")
                        answer[-1] += "*".join(key)

                    elif result_dict[key] != 1:
                        answer.append(f"{result_dict[key]}*")
                        answer[-1] += "*".join(key)

                    else:
                        answer.append("*".join(key))
            else:
                if not answer or result_dict[key] < 0:
                    answer.append(str(result_dict[key]))

                elif result_dict[key] > 0:
                    answer.append("+")
                    answer.append(str(result_dict[key]))

    return " ".join(answer)


def convert_expression(expression: str) -> dict:
    """Функция, которая конвертирует выражение из строки в словарь, для дальнейшего упрощения"""
    expression_as_dict = {}
    cur_digit = ""
    cur_letters = ""
    negative = True if expression[0] == "-" else False

    for symbol in expression:
        if symbol.isdigit():
            cur_digit += symbol

        elif symbol.isalpha():
            cur_letters += symbol

        elif symbol == "*" or symbol == " ":
            continue

        elif symbol == "-":
            negative = True

        else:
            if not cur_digit:
                cur_digit = "1"
            if cur_letters:
                cur_letters = "".join(sorted(cur_letters))
                if negative:
                    expression_as_dict[cur_letters] = expression_as_dict.get(cur_letters, 0) - int(cur_digit)

                else:
                    expression_as_dict[cur_letters] = expression_as_dict.get(cur_letters, 0) + int(cur_digit)

            else:
                if negative:
                    expression_as_dict["digits"] = expression_as_dict.get("digits", 0) - int(cur_digit)

                else:
                    expression_as_dict["digits"] = expression_as_dict.get("digits", 0) + int(cur_digit)

            cur_letters = cur_digit = ""
            negative = False

    if cur_letters:
        if not cur_digit:
            cur_digit = "1"
        cur_letters = "".join(sorted(cur_letters))
        if negative:
            expression_as_dict[cur_letters] = expression_as_dict.get(cur_letters, 0) - int(cur_digit)

        else:
            expression_as_dict[cur_letters] = expression_as_dict.get(cur_letters, 0) + int(cur_digit)

    elif cur_digit:
        if negative:
            expression_as_dict["digits"] = expression_as_dict.get("digits", 0) - int(cur_digit)

        else:
            expression_as_dict["digits"] = expression_as_dict.get("digits", 0) + int(cur_digit)

    return expression_as_dict

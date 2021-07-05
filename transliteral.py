def transliteration(string):  # блок транслитерации

    class_lexeme = list(range(0, len(string)))

    for i in range(0, len(string)):

        if ord('a') <= ord(string[i]) <= ord('z'):
            class_lexeme[i] = (string[i], "буква")

        elif ord('A') <= ord(string[i]) <= ord('Z'):
            class_lexeme[i] = (string[i], "буква")

        elif ord('0') <= ord(string[i]) <= ord('9'):
            class_lexeme[i] = (string[i], "цифра")

        elif string[i] == ":":
            class_lexeme[i] = (string[i], "двоеточие")

        elif string[i] == "=":
            class_lexeme[i] = (string[i], "равно")

        elif string[i] == " ":
            class_lexeme[i] = (string[i], "пробел")

        elif string[i] == "-" or string[i] == "+" or string[i] == "*":
            class_lexeme[i] = (string[i], "знак")

        elif string[i] == "(":
            class_lexeme[i] = (string[i], "скобка1")

        elif string[i] == ")":
            class_lexeme[i] = (string[i], "скобка2")

        elif string[i] == "[":
            class_lexeme[i] = (string[i], "квскобка1")

        elif string[i] == "]":
            class_lexeme[i] = (string[i], "квскобка2")

        elif string[i] == ",":
            class_lexeme[i] = (string[i], "запятая")

        elif string[i] == ";":
            class_lexeme[i] = (string[i], "тчкзпт")
            break
        else:
            class_lexeme[i] = (string[i], "ошибка")
            print("runtime error : unexpected symbol")
            # result_of_string = "REJECT"
            sys.exit()

    return class_lexeme


string = input()
print(transliteration(string))

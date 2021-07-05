""" блок чтения цепочек из файла(ввод данных) и запись результата в файл(вывод данных)
result - переменная, содержащая в себе результат: ACCEPT если цепочка соответствует и REJECT если не соответствует"""


def enter():
    with open("input.txt", "r") as f:
    input_str = f.read()
    return input_str


def derive(result, error_type):
    with open("output.txt", "w") as f:
    print(result, file=f)
    print(error_type, file=f)
    return print("The program is completed successfully!")



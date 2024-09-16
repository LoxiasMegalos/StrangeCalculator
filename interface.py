# Linguagem de programação
#
# um, dois, tres, quatro, cinco, seis, sete, oito, nove [0-9]
#
# @ - atribuicao
# x - multiplicação
# ! - divisão
# ? - soma
# ~ - subtração
#
# , - ;
#
# 69 - parênteses
#
# 6 um;um {} dois 9 x tres = nove;tres

reserved_words = [
    "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "@", "x", "!", "?", "~", ".", "6", "9", ";"
]

numbers = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]

ops = ["x", "!", "?", "~"]

memory_variables = {}


def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "("}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack


def verify_input(some_input):
    if not some_input.endswith("."):
        print("Error - todas as entradas devem finalizar com .")
        return

    splited_input = some_input.split(" ")

    if len(splited_input) <= 1:
        print("Error - invalid entry.")
        return

    if splited_input[0] in reserved_words and splited_input[1] == "@":
        print("Error - attribuição não pode começar com uma palavra reservada")
        return

    elements_input = some_input[:-1].split("@")

    if len(elements_input) == 2:
        verification = verify_math_expression(elements_input[1])

        if "error" in verification:
            print(verification)
            return

        memory_variables[elements_input[0].strip()] = resolve_math_expression(verification)

        print(f"Variavel {elements_input[0].strip()} salva com sucesso na memória com o valor da conta solicitada")

    elif len(elements_input) == 1:
        verification = verify_math_expression(elements_input[0])

        if "error" in verification:
            print(verification)
            return

        resolution = resolve_math_expression(verification)

        int_check = float(resolution).is_integer()

        if int_check:
            resolution = int(resolution)
        else:
            resolution = round(resolution, 3)

        print("Resultado Linguagem convencional: " + str(resolution) + " | Resultado Gramática definida: " +
              str(resolution).replace("1", "um").replace("0", "zero").replace("1", "um").replace("2", "dois")
              .replace("3", "tres").replace("4", "quatro").replace("5", "cinco").replace("6", "seis")
              .replace("7", "sete").replace("8", "oito").replace("9", "nove").replace(".", ";").replace("-", "~"))
    else:
        print("Error - atribuição não pode começar com uma palavra reservada")
        return


def verify_math_expression(expression):

    used_variables = []

    expression = expression.replace("?", " ? ").replace("~", " ~ ").replace("!", " ! ").replace("x", " x ")\
        .replace("6", " 6 ").replace("9", " 9 ").replace("6", "(").replace("9", ")")\
        .replace(";", ".").replace("um", "1").replace("dois", "2") \
        .replace("tres", "3").replace("quatro", "4").replace("cinco", "5").replace("seis", "6").replace("sete", "7") \
        .replace("oito", "8").replace("nove", "9").replace("zero", "0").replace("  ", " ")

    for element in expression.split():

        if element.count("(") == len(element) or element.count(")") == len(element):
            continue

        if element not in reserved_words and not element.replace('.', '', 1).replace('-', '', 1).isdigit():
            if element not in memory_variables:
                return f"error - {element} invalid in expression"
            used_variables.append(element)

    expression = expression.replace("  ", " ").replace("?", "+").replace("~", "-").replace("!", "/").replace("x", "*")

    for var in list(set(used_variables)):
        expression = expression.replace(var, str(memory_variables[var]))

    valid = is_valid(expression)

    if not valid:
        return "error - not balanced parentheses"

    return expression


def resolve_math_expression(math_expression):
    return eval(math_expression)


print("************************************************************")
print("Gramática um dois tres - pode começar a usar a calculadora: ")
print("************************************************************")

while True:
    user_input = input()
    if user_input == "0":
        print("Obrigado por usar a calculadora um dois tres")
        break

    verify_input(user_input)

from testing import test

def get_multiple(equation, variable):
    index = equation.index(variable)
    number = ''
    if not index == 0 :
        side = -1 if equation[index - 1].isdigit() else 1
    else:
        return 1
    index += side
    while equation[index].isdigit() and index >= 0:
        number += equation[index]
        index += side
    return int(number[::-1])

def clean_equation(dirty_equation):
    variable = '+x' if dirty_equation[0].isalpha() else ''
    clean_equation = dirty_equation
    if variable == '':
        for i, j in enumerate(dirty_equation):
            if j.isalpha():
                variable = dirty_equation[i-1] + j
                clean_equation = dirty_equation[:i-1] + dirty_equation[i+1:]
    if clean_equation == dirty_equation:
        clean_equation = dirty_equation[2:]
    clean_equation = clean_equation.split("=")
    clean_equation[0] = str(eval(clean_equation[0]))
    clean_equation[0] += variable
    return '='.join(clean_equation)


def solve(equation):
    split_eqn = equation.split("=")
    variable = ("+" + equation[0]) if (equation[0] == '+' or equation[0] == '-') else ""
    for i, j in enumerate(equation):
        if j.isalpha():
            variable = equation[i - 1] + equation[i]
            split_eqn[0] = split_eqn[0].replace(variable, '')
    eqn_int = [int(i) for i in split_eqn]
    eqn_int[0] *= -1
    return sum(eqn_int) if (variable[0] == '+') else (-1 * sum(eqn_int))

test(get_multiple('x+34=98', 'x'), 1)
test(get_multiple('3y+3=12', 'y'), 3)

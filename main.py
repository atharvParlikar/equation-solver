# look for the first element as x
# if not the first one, search the whole equation until you find x
# give it proper sign
# make a clean equation, by excluding variable from dirty equationself.

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

print(clean_equation('3+x+2=6'))

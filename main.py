def clean_eqn(dirty_equation):
    variable = ''
    clean_eq = ''
    for i, j in enumerate(dirty_equation):
        if j.isalpha():
            variable = dirty_equation[i - 1] + dirty_equation[i]
            clean_eq = dirty_equation[:i-1] + dirty_equation[i+1:]
            clean_eq = clean_eq.split("=")
            #clean_eq[0] = eval(clean_eq[0])
            #clean_eq[1] = eval(clean_eq[1])
            return str(clean_eq[0]) + variable + '=' + str(clean_eq[1])

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

print(clean_eqn('x+3+2=6'))

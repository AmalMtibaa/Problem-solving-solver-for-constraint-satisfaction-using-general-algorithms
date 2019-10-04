def verif(a, b, c):
    if b == ">":
        return a > c
    if b == "<":
        return a < c
    if b == ">=":
        return a >= c
    if b == "<=":
        return a <= c
    if b == "==":
        return a == c
    if b == "!=":
        return a != c


def verifContrainte(cond, a, csp):
    if cond[0].islower() and not cond[0].replace('.', '', 1).isdigit() and cond[2].islower() \
            and not cond[2].replace('.', '', 1).isdigit():
        if verif(a[csp.variables.index(cond[0])], cond[1], a[csp.variables.index(cond[2])]):
            return True
        else:
            return False

    elif cond[0].islower() and not cond[0].replace('.', '', 1).isdigit() and (
            cond[2].isupper() or cond[2].replace('.', '', 1).isdigit()):
        if verif(a[csp.variables.index(cond[0])], cond[1], cond[2]):
            return True
        else:
            return False
    elif (cond[0].isupper() or cond[0].replace('.', '', 1).isdigit()) and cond[2].isupper() and not cond[2].replace(
            '.', '', 1).isdigit():
        if verif(cond[0], cond[1], a[csp.variables.index(cond[2])]):
            return True
        else:
            return False
    return True


def verifContraintes(a, i, var, csp, ):
    inif = 0
    actif = 0
    contraintes = csp.contraintes[i]
    for c in contraintes:
        cond = c.split(" ")
        if cond[0] == "}":
            inif = 0
            actif = 0
        elif cond[0] == "if":
            inif = 1
            if cond[len(cond) - 1] == "{":
                cond = cond[0:len(cond) - 1]
            else:
                cond[len(cond) - 1] = cond[len(cond) - 1][0:len(cond[len(cond) - 1]) - 1]
            if verifContrainte(cond[1:], a, csp):
                actif = 1
        else:
            if inif == 1 and actif == 1:
                if not verifContrainte(cond, a, csp):
                    return False
            elif inif == 1 and actif == 0:
                continue
            elif not verifContrainte(cond, a, csp):
                return False
    return True


def complete(a, csp, nq):
    if nq == 1:
        cnt = 0
        for i in range(0, 64):
            if a[i] == '1':
                cnt += 1
        if cnt != 8:
            return False
    for i in range(0, len(a)):
        if a[i] is None:
            return False
        test = verifContraintes(a, i, csp.variables[i], csp)
        if not test:
            return False

    return True

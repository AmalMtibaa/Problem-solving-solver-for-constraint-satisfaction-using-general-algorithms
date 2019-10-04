from Affichage import AffichageSudoku
from cspUtil import *
from csp import *


def choisirVarNonAffecterMRV(a, csp):
    min = 100000000
    pos = -1
    for i in range(0, len(a)):
        if a[i] is None:
            if len(csp.domaines[i]) < min:
                min = len(csp.domaines[i])
                pos = i
    return pos


def consistant(tmp, csp, nq):
    for i in range(0, len(tmp)):
        if tmp[i] is not None:
            test = verifContraintes(tmp, i, tmp[i], csp)
            if not test:
                return False
    if nq == 1:
        boo = True
        for i in range(0, 64):
            if tmp[i] is None:
                boo = False
                break
        if boo:
            cnt = 0
            for i in range(0, 64):
                if tmp[i] == '1':
                    cnt += 1
            if cnt == 8:
                return True
            else:
                return False
    return True

#delete from the domains of varX's neighbors
def DeleteFromDomaines(a, v, csp, varX):
    for i in csp.contraintes[varX]:
        ji = i.split(" ")
        if ji[0] == 'if' or ji[0] == '}':
            return
        var = ji[2]
        k = csp.variables.index(var)
        if a[k] is None:
            if v in csp.domaines[k]:
                csp.domaines[k].remove(v)


def AddtoDomain(a, v, csp, varX):
    for i in csp.contraintes[varX]:
        i = i.split(" ")
        var = i[2]
        k = csp.variables.index(var)
        if a[k] is None:
            if v not in csp.domaines[k]:
                csp.domaines[k].append(v)


def Forward(a, csp, nq):
    if complete(a, csp, nq):
        return [1, a]

    varX = choisirVarNonAffecterMRV(a, csp)
    valD = csp.domaines[varX]

    for v in valD:
        tmp = a.copy()
        tmp[varX] = v
        if consistant(tmp, csp, nq):
            a[varX] = v
            print(a)
            DeleteFromDomaines(a, v, csp, varX)
            result = Forward(a, csp, nq)
            if result[0] == 1:
                return result
            a[varX] = None
            AddtoDomain(a, v, csp, varX)
    return [0, None]

#
# t = csp()
# file = open("CSP\Sudoku\Variables", "r")
# ch = file.read().rstrip('\n')
# t.ajoutVariable(ch)
# file.close()
# file = open("CSP\Sudoku\Domaines", "r")
# for i in range(0, 81):
#     ch = file.readline().rstrip('\n').split(" ")[1]
#     tmp = ch.split(",")
#     tmp[0] = tmp[0][1:]
#     tmp[len(tmp) - 1] = tmp[len(tmp) - 1][0:(len(tmp[len(tmp) - 1]) - 1)]
#     t.ajoutDomaine(t.variables[i], tmp)
# file.close()
# file = open("CSP\Sudoku\Contraintes", "r")
# for i in range(0, 81):
#     ch = file.readline().rstrip('\n')
#     while ch != "##":
#         t.ajoutContrainte(t.variables[i], ch)
#         ch = file.readline().rstrip('\n')
# file.close()
# a = []
# for i in range(0, len(t.variables)):
#     if len(t.domaines[i]) == 1:
#         a.append(t.domaines[i][0])
#     else:
#         a.append(None)
# for i in range(0, len(t.variables)):
#     if len(t.domaines[i]) == 1:
#         DeleteFromDomaines(a, t.domaines[i][0], t, i)
#
# Forward(a, t, 0)
# AffichageSudoku(a, 9)

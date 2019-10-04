from csp import *
from cspUtil import *

#Choose Variables that have less contraints
def choisirVarNonAffecterLCV(a,csp):
    min = 100000000
    pos = -1
    for i in range(0,len(a)):
        if a[i] is None:
            if len(csp.contraintes[i])<min:
                min=len(csp.contraintes[i])
                pos=i
    return pos


def choisirVarNonAffecter(a):
    for i in range(0, len(a)):
        if a[i] is None:
            return i


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

def Bactracking(a, csp, nq):
    if complete(a, csp, nq):
        return [1, a]

    varX = choisirVarNonAffecterLCV(a,csp)
    valD = csp.domaines[varX]

    for v in valD:
        tmp = a.copy()
        tmp[varX] = v

        if consistant(tmp, csp, nq):
            a[varX] = v
            print(a)
            result = Bactracking(a, csp, nq)
            if result[0] == 1:
                return result
            a[varX] = None
    return [0, None]


t = csp()


def setBacktracking():
    t=csp()
    file = open("CSP\Sudoku\Variables", "r")
    ch = file.read().rstrip('\n')
    t.ajoutVariable(ch)
    file.close()
    file = open("CSP\Sudoku\Domaines", "r")
    for i in range(0, 81):
        ch = file.readline().rstrip('\n').split(" ")[1]
        tmp = ch.split(",")
        tmp[0] = tmp[0][1:]
        tmp[len(tmp) - 1] = tmp[len(tmp) - 1][0:(len(tmp[len(tmp) - 1]) - 1)]
        t.ajoutDomaine(t.variables[i], tmp)
    file.close()
    file = open("CSP\Sudoku\Contraintes", "r")
    for i in range(0, 81):
        ch = file.readline().rstrip('\n')
        while ch != "##":
            t.ajoutContrainte(t.variables[i], ch)
            ch = file.readline().rstrip('\n')
    file.close()
    return t

def setBactraking8Queens():
    t=csp()
    file = open("CSP\\N-Reines\Variables", "r")
    ch = file.read().rstrip('\n')
    t.ajoutVariable(ch)
    file.close()
    file = open("CSP\\N-Reines\Domaines", "r")
    for i in range(0, 64):
        ch = file.readline().rstrip('\n').split(" ")[1]
        tmp = ch.split(",")
        tmp[0] = tmp[0][1:]
        tmp[len(tmp) - 1] = tmp[len(tmp) - 1][0:(len(tmp[len(tmp) - 1]) - 1)]
        t.ajoutDomaine(t.variables[i], tmp)
    file.close()
    file = open("CSP\\N-Reines\Contraintes", "r")
    for i in range(0, 64):
        ch = file.readline().rstrip('\n')
        while ch != "##":
            t.ajoutContrainte(t.variables[i], ch)
            ch = file.readline().rstrip('\n')
    file.close()


    return t


from csp import *
from ARC import *
from cspUtil import *
from ForwardCheck import *
def forward_CheckAC3(a,csp):
    if complete(a, csp, 0):
        return [1, a]
    AC3Domains=ARC3(csp)
    for i in range(0,len(csp.variables)):
        csp.ajoutDomaine(csp.variables[i],AC3Domains[i])

    varX = choisirVarNonAffecterMRV(a, csp)
    valD = csp.domaines[varX]

    for v in valD:
        tmp = a.copy()
        tmp[varX] = v
        if consistant(tmp, csp, 0):
            a[varX] = v
            print(a)
            DeleteFromDomaines(a, v, csp, varX)
            result = forward_CheckAC3(a, csp)
            if result[0] == 1:
                return result
            a[varX] = None
            AddtoDomain(a, v, csp, varX)
    return [0, None]




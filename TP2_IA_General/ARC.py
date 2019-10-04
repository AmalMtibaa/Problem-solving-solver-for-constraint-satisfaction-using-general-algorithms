from csp import *
def ARC3(csp):
    for varX in csp.variables:
        R1=csp.getUnariContraints(varX)
        domainX=csp.getDomaineRespectingR1(varX,R1) #list of domain that satisfy R1
        csp.ajoutDomaine(varX,domainX)
        list=variables_connected_to_X(csp,varX)
        list_of_Y=list[0] #R2
        workList=[]
        for y in list_of_Y:
            workList.append((varX,y))
        while workList!=[]:
            arc=chooseArcFromWorkList(workList)
            workList=[item for item in workList if item not in [arc] ]
            if arc_reduce(arc,csp,list[1]):
                if csp.getDomaine(arc[0])==[]: #x = arc[0]
                    return None
                else:
                    list_of_Z=variables_connected_but_y(csp,arc[0],arc[1]) #{(z, x)| z != y and there exists a R2(x, z) or R2(z, x) }
                    workList=workList+list_of_Z
        return csp.domaines


def variables_connected_but_y(csp,x,y):
    result = []
    var_constraints = csp.getContraintes(x)
    for constraint in var_constraints:
        cons = constraint.split(" ")
        if (cons != ['']):

            if cons[0] == x and cons[2]!=y and cons[2] not in csp.getDomaine(x):
                result.append(cons[2])
            if cons[2] == x and cons[0]!=y and cons[0] not in csp.getDomaine(x):
                result.append(cons[0])
    return result


def chooseArcFromWorkList(workList): #will be changed by Heureustic later
    return workList[0]

def arc_reduce (arc,csp,r2):
     change = False
     for vx in csp.getDomaine(arc[0]):
         list_of_Y = vy_with_vxAndvy_satisf_r2(csp, arc[0],arc[1],r2)

         if list_of_Y==False:
             domainX=csp.getDomaine(arc[0])
             csp.ajoutDomaine(arc[0],[d for d in domainX if d not in [vx]])
             change=True
     return change

def vy_with_vxAndvy_satisf_r2(csp,x,y,r2):
    domainY=csp.getDomaine(y)
    domainX=csp.getDomaine(x)
    for dy in domainY:
        for r in r2:
            cons=r.split(" ")
            if (cons[1] == "="):
                if dy in domainX:
                    return False
            if (cons[1]=="!="):
                if dy not in domainX:
                    return False
    return True







def variables_connected_to_X(csp,varX):
    result = [] #Variables
    usedContraints=[]
    var_constraints = csp.getContraintes(varX)
    for constraint in var_constraints:
        cons = constraint.split(" ")
        if (cons != ['']):
            if cons[0] == varX and cons[2] not in csp.getDomaine(varX):
                result.append(cons[2])
                usedContraints.append(constraint)
            if cons[2] == varX and cons[0] not in csp.getDomaine(varX):
                result.append(cons[0])
                usedContraints.append(constraint)
    return [result,usedContraints]

#
# t = csp()
# t.ajoutVariable("wa nt sa qu nsw vi ta")
# for v in t.variables:
#     t.ajoutDomaine(v, ["Blue", "Green", "Red"])
#
# t.ajoutContrainte(t.variables[0], t.variables[0] + " != " + t.variables[1])
# t.ajoutContrainte(t.variables[0], t.variables[0] + " != " + t.variables[2])
# t.ajoutContrainte(t.variables[1], t.variables[1] + " != " + t.variables[0])
# t.ajoutContrainte(t.variables[1], t.variables[1] + " != " + t.variables[2])
# t.ajoutContrainte(t.variables[1], t.variables[1] + " != " + t.variables[3])
# t.ajoutContrainte(t.variables[2], t.variables[2] + " != " + t.variables[0])
# t.ajoutContrainte(t.variables[2], t.variables[2] + " != " + t.variables[1])
# t.ajoutContrainte(t.variables[2], t.variables[2] + " != " + t.variables[3])
# t.ajoutContrainte(t.variables[2], t.variables[2] + " != " + t.variables[4])
# t.ajoutContrainte(t.variables[2], t.variables[2] + " != " + t.variables[5])
# t.ajoutContrainte(t.variables[3], t.variables[3] + " != " + t.variables[1])
# t.ajoutContrainte(t.variables[3], t.variables[3] + " != " + t.variables[2])
# t.ajoutContrainte(t.variables[3], t.variables[3] + " != " + t.variables[4])
# t.ajoutContrainte(t.variables[4], t.variables[4] + " != " + t.variables[2])
# t.ajoutContrainte(t.variables[4], t.variables[4] + " != " + t.variables[3])
# t.ajoutContrainte(t.variables[4], t.variables[4] + " != " + t.variables[5])
# t.ajoutContrainte(t.variables[5], t.variables[5] + " != " + t.variables[2])
# t.ajoutContrainte(t.variables[5], t.variables[5] + " != " + t.variables[4])
#
#
#
#
# ARC3(t)
# print(t.domaines)
class csp:
    def __init__(self):
        self.variables = []
        self.domaines = []
        self.contraintes = []

    def ajoutVariable(self, ch):
        self.variables = ch.split(" ")
        for i in range(0, self.variables.__len__()):
            self.domaines.append([])
            self.contraintes.append([])

    def ajoutDomaine(self, var, domaine):
        self.domaines[self.variables.index(var)] = domaine

    def ajoutContrainte(self, var, contrainte):
        self.contraintes[self.variables.index(var)].append(contrainte)



    def getDomaine(self, var):
            return self.domaines[self.variables.index(var)]

    def getContraintes(self, var):
        return self.contraintes[self.variables.index(var)]

    def toString(self):
        print("Variables : ", end="")
        for v in self.variables:
            print(v, " ", end="")
        print()
        print("Domaine de chaque variable :")
        for i in range(0, self.variables.__len__()):
            print(self.variables[i], " : ", self.domaines[i])

        print("Contraintes de chaque variable :")
        for i in range(0, self.variables.__len__()):
            print(self.variables[i], ": ")
            for c in self.contraintes[i]:
                print("\t", c)

    def getUnariContraints(self, var):
        var_contraints = self.getContraintes(var)
        result = []
        for cons in var_contraints:
            c = cons.split(" ")
            if (c != ['']):
                if c[0] == var and c[2] in self.getDomaine(var):
                    result.append(c[2])
                if c[2] == var and c[0] not in self.getDomaine(var):
                    result.append(c[0])
        return result

    def getDomaineRespectingR1(self, varX, R1):
        domainX = self.getDomaine(varX)
        resultedDomain = domainX
        for r in R1:
            condition = r.split(" ")
            if condition[0] != varX:
                if condition[1] == "=":
                    resultedDomain = condition[0]
                    return resultedDomain
                if condition[1] == "!=":
                    resultedDomain = list(set(resultedDomain) - set(condition[0]))
                if condition[1] == ">":
                    resultedDomain = [x for x in resultedDomain if x < condition[0]]
                if condition[1] == "<":
                    resultedDomain = [x for x in resultedDomain if x > condition[0]]
            if condition[2] != varX:
                if condition[1] == "=":
                    resultedDomain = condition[2]
                    return resultedDomain
                if condition[1] == "!=":
                    resultedDomain = list(set(resultedDomain) - set(condition[2]))
                if condition[1] == ">":
                    resultedDomain = [x for x in resultedDomain if x > condition[2]]
                if condition[1] == "<":
                    resultedDomain = [x for x in resultedDomain if x < condition[0]]
        return resultedDomain



# Accepted
# Runtime 54 ms Beats 53.21%
# Memory 20.87 MB Beats 9.70%


class no:
    def __init__(self):
        self.pre_requisitos = set()


class Solution:
    def get_prerequisitos(self, n):
        if n in self.pre_requisitos:
            temp = set()
            temp.add(n)
            temp.update(self.pre_requisitos[n])
            return temp
        if not self.materias[n].pre_requisitos:
            self.pre_requisitos[n] = set()
            temp = set()
            temp.add(n)
            return temp
        pre_requisitos = set()
        for pre_req in self.materias[n].pre_requisitos:
            lista_pre_req = self.get_prerequisitos(pre_req)
            if lista_pre_req:
                pre_requisitos.update(lista_pre_req)
        self.pre_requisitos[n] = pre_requisitos
        temp = set()
        temp.add(n)
        temp.update(self.pre_requisitos[n])
        return temp

    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        self.materias = [no() for i in range(numCourses)]
        self.pre_requisitos = dict()

        for pre_req, mat in prerequisites:
            self.materias[mat].pre_requisitos.add(pre_req)

        for i in range(numCourses):
            self.get_prerequisitos(i)
            if len(self.pre_requisitos) == numCourses:
                break
        retorno = list()
        for u, v in queries:
            retorno.append(u in self.pre_requisitos[v])

        return retorno

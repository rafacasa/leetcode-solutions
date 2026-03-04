# Accepted
# Runtime 10 ms Beats 24.60%
# Memory 19.72 MB Beats 85.11%


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        linhas = {}
        colunas = {}
        special = 0

        for i, linha in enumerate(mat):
            linhas[i] = sum(linha)
            for j, item in enumerate(linha):
                colunas[j] = colunas.get(j, 0) + item
        
        for i, linha in enumerate(mat):
            linhas[i] = sum(linha)
            for j, item in enumerate(linha):
                if item:
                    if linhas[i] < 2 and colunas[j] < 2:
                        special += 1
        
        return special
    
print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print(Solution().numSpecial([[1,0,0],[0,1,0],[0,0,1]]))

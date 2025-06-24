# Accepted
# Runtime 26 ms Beats 26.88%
# Memory 19.99 MB Beats 15.41%


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        conjunto = set()
        qtd_linhas = len(grid)
        qtd_colunas = len(grid[0])

        linhas_com_comunicacao = [i for i in range(qtd_linhas) if sum(grid[i]) > 1]

        colunas = [[linha[i] for linha in grid] for i in range(qtd_colunas)]

        colunas_com_comunicacao = [i for i in range(qtd_colunas) if sum(colunas[i]) > 1]

        for i in linhas_com_comunicacao:
            for j, item in enumerate(grid[i]):
                if item:
                    conjunto.add((i, j))

        for j in colunas_com_comunicacao:
            for i, item in enumerate(colunas[j]):
                if item:
                    conjunto.add((i, j))

        return len(conjunto)

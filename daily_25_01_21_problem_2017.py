# Accepted
# Runtime 111 ms Beats 31.37%
# Memory 31.35 MB Beats 5.63%


class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        soma1 = [0] * (n + 1)
        soma2 = [0] * (n + 1)

        for i in range(1, n + 1):
            soma1[i] = soma1[i - 1] + grid[0][i - 1]
            soma2[i] = soma2[i - 1] + grid[1][i - 1]

        pontosB = []

        for i in range(n):
            pontos1 = soma1[n] - soma1[i + 1]
            pontos2 = soma2[i]
            pontosB.append(max(pontos1, pontos2))

        return min(pontosB)

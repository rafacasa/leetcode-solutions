# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.95 MB Beats 15.61%


class Solution:
    def combinacoes(self, digitos, lista_combinacoes):
        if not digitos:
            return lista_combinacoes

        digito = digitos[0]

        if not lista_combinacoes:
            return self.combinacoes(digitos[1:], self.mapa[digito])

        nova_lista = []

        for palavra in lista_combinacoes:
            for letra in self.mapa[digito]:
                nova_lista.append(palavra + letra)

        return self.combinacoes(digitos[1:], nova_lista)

    def letterCombinations(self, digits: str) -> list[str]:
        self.mapa = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        return self.combinacoes(digits, [])

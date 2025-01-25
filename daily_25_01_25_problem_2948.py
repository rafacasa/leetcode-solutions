# Accepted
# Runtime 230 ms Beats 93.75%
# Memory 96.35 MB Beats 5.56%

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)

        anterior = None
        grupo_atual = 0
        mapa_num_grupo = dict()
        mapa_grupo_itens = {0: deque()}
        
        for num in nums_sorted:
            if not anterior:
                anterior = num
                mapa_num_grupo[num] = grupo_atual
                mapa_grupo_itens[grupo_atual].append(num)
                continue
            
            if num - anterior > limit:
                grupo_atual += 1
                mapa_grupo_itens[grupo_atual] = deque()
            
            mapa_num_grupo[num] = grupo_atual
            mapa_grupo_itens[grupo_atual].append(num)
            anterior = num
        
        for i in range(len(nums)):
            grupo = mapa_num_grupo[nums[i]]
            nums[i] = mapa_grupo_itens[grupo].popleft()
        
        return nums

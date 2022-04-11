from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        rowsPower = {i:sum(r) for i, r in enumerate(mat)}
        orderedTuple = sorted(rowsPower.items(), key=lambda tpl: (tpl[1], tpl[0]))
        for i in range(k):
            result.append(orderedTuple[i][0])
        return result


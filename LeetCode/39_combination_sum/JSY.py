# Note
# 1. Referred to this blog: https://velog.io/@eunseokim/36.-Combination-Sum 

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, _sum):
            if _sum > target:
                return
            if _sum == target: # Found the answer!
                answer.append(path[:])
                return

            for val in curr:
                path.append(val)
                i = candidates.index(val)
                # print(candidates[i:])
                backtrack(candidates[i:], sum(path))
                path.pop()

        path, answer = [], []
        backtrack(candidates, 0)

        return answer


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7

    print(Solution().combinationSum(candidates, target))
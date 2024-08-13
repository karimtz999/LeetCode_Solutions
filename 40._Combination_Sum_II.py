from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
        
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res

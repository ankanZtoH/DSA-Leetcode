class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def make_combination(idx, sol, target):
            if target == 0:
                res.append(sol[:])
                return
            if idx == len(candidates) or target < 0:
                return
            # Take the element
            sol.append(candidates[idx])
            make_combination(idx, sol, target - candidates[idx])
            sol.pop()
            # Skip the element
            make_combination(idx + 1, sol, target)
        
        make_combination(0, [], target)
        return res

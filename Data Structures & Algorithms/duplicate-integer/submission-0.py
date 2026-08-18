class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        dups = []
        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                dups.append(i)
        
        if len(dups) >= 1:
            return True
        return False
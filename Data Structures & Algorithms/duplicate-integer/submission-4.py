class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l2=set()
        for i in nums:
            if i in l2:
                return True
            l2.add(i)
        return False
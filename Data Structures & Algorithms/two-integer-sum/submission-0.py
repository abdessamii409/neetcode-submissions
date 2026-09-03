class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #d=dict(nums)
        #for i in d:
        #    for j in 
        c=0
        d={}
        for i in nums:
            d[c]=i
            c+=1
        
        i = 0
        while i < c:
            j = i + 1
            while j < c:
                if d[i] + d[j] == target:
                    return [i,j]
                j+=1
            i+=1
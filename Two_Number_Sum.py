class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        x = 0
        y = 0
        
        for num in nums:
            if target - num in nums_dict:
                x = target-num
                y = num
            else:
                nums_dict[num] = True
        
        a = nums.index(x)
        b = nums.index(y)
        
        if a == b:
            for j in range(len(nums)):
                if nums[j] == y and j!=a:
                    b = j
        return [a,b]

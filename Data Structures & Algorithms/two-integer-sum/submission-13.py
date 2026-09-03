class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_nums = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in dict_nums:
                return [dict_nums[remainder], i]
            dict_nums[nums[i]] = i
        
        #target - nums[i] = nums[j]
        #{3: 0 , 4: 1, ....}

        return []
        


         
        
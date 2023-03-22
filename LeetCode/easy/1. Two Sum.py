class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = nums.copy()
        for i in range(len(nums) - 1):
            num = num_list.pop()
            try:
                idx = num_list.index(target - num)
                return [idx, len(nums) - i - 1]
            except:
                pass

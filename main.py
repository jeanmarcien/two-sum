nums = [3,2,4]

target = 6

class TwoSum:
    '''A simple way to find the sum of a number from a list'''

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum(self):
        for first_item in self.nums:

            first_index = self.nums.index(first_item)
            second_item = self.target - first_item

            for lookup_value in self.nums:
                if lookup_value == second_item:
                    second_index = self.nums.index(second_item)
                    print(f"{self.target} can be obtained from the item {first_index} and {second_index} of the list: {self.nums}" )
                else:
                    continue

solve = TwoSum(nums, target)
solve.two_sum()

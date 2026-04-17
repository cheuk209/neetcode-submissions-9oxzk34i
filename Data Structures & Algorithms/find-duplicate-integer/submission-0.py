class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        meet = slow
        slow = 0
        while True:
            slow = nums[slow]
            meet = nums[meet]
            if slow == meet:
                return slow
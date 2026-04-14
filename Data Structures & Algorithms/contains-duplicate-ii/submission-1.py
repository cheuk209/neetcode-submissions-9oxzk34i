class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_set = set()
        for index, value in enumerate(nums):
            if len(duplicate_set) == k + 1:
                print("what are we removing", nums[index - k - 1])
                duplicate_set.remove(nums[index - k - 1])
            if value in duplicate_set:
                return True
            else:
                duplicate_set.add(value)
        return False

            



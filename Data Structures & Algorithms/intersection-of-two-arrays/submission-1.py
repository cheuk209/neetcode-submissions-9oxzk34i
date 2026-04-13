class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_hashset = set(nums1)
        result = []
        for num in nums2:
            if num in num1_hashset and num not in result:
                result.append(num)
        return result
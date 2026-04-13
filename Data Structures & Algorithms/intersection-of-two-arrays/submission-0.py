class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_result = []
        for num in nums1:
            if num in nums2 and num not in intersect_result:
                intersect_result.append(num)
        return intersect_result
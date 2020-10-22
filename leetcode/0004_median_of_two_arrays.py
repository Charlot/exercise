from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        nums3 = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])
        if len(nums3)%2==0:
            return (nums3[len(nums3)//2-1] + nums3[len(nums3)//2])/2
        else:
            return nums3[len(nums3)//2]


print(Solution().findMedianSortedArrays([1,2],[3]))
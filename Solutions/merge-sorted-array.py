class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while n>0:
            if m-1<0: 
                nums1[0:n] = nums2[0:n]
                break
            if nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n-=1
            else:
                nums1[m+n-1] = nums1[m-1]
                nums1[m-1] = 0
                m-=1
                

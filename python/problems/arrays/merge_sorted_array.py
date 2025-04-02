class Solution:

        def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

            left, right = m - 1, n - 1
            index = m + n - 1
            while left >= 0 and right >= 0:
                 
                 if nums1[left] >= nums2[right]:
                      nums1[index] = nums1[left]
                      left -= 1
                 else:
                      nums1[index] = nums2[right]
                      right -= 1
                 
                 index -= 1

            while right >= 0:
                 nums1[index] = nums2[right]
                 right -= 1
                 index -= 1

            print(nums1)

            return None
        

if __name__ == '__main__':
    s = Solution()
    examples = [
        [[1,2,3,0,0,0], 3, [2,5,6], 3],
        [[1], 1, [], 0],
        [[0], 0, [1], 1]
    ]
    
    for ex in examples:
        print(s.merge(*ex))
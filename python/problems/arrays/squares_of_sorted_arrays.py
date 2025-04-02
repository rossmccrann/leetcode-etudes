class Solution:

    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        return sorted([num ** 2 for num in nums])
    
    def sortedSquaresWithMap(self, nums: list[int]) -> list[int]:

        return sorted(map(lambda x: x ** 2, nums))
    
    def sortedSquaresTwoPointer(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n-1

        index = n - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1


        return result


if __name__ == '__main__':
    s = Solution()
    examples = [
        [-4,-1,0,3,10],
        [-7,-3,2,3,11]
    ]
    
    for ex in examples:
        print(s.sortedSquares(ex))


"""

def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1

    return result
"""
class Solution:

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1

            else:
                if max_count < current_count:
                    max_count = current_count
                current_count = 0
                
        if max_count < current_count:
                max_count = current_count

        return max_count


if __name__ == '__main__':
    s = Solution()
    examples = [
    [1,1,0,1,1,1],
    [1,0,1,1,0,1]
    ]
    
    for ex in examples:
        print(s.findMaxConsecutiveOnes(ex))


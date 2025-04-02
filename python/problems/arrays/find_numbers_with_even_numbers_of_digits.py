class Solution:

    def findNumbers(self, nums: list[int]) -> int:
        evenNumberedDigitCount = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                evenNumberedDigitCount += 1
        return evenNumberedDigitCount


if __name__ == '__main__':
    s = Solution()
    examples = [
        [12,345,2,6,7896],
        [555,901,482,1771]
    ]
    
    for ex in examples:
        print(s.findNumbers(ex))


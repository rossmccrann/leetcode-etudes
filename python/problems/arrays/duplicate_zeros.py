class Solution:

    def duplicateZeros(self, arr: list[int]) -> None:
       n = len(arr)
       zeros = arr.count(0)

       for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]

            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0 
 
       return None
    
if __name__ == '__main__':
    s = Solution()
    examples = [
        [1,0,2,3,0,4,5],
        [1,2,3],
        [1,0,0,0,2]
    ]
    
    for ex in examples[:1]:
        print(s.duplicateZeros(ex))
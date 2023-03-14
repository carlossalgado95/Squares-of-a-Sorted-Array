class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        vet = []
        l=0
        r= len(nums)-1

        while(l<=r):
            if nums[l]*nums[l] > nums[r]*nums[r]:
                vet.append(nums[l]*nums[l])
                l += 1
            else:
                vet.append(nums[r]*nums[r])
                r -= 1
        return vet[::-1]

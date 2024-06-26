class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[left] == nums[mid] == nums[right]:
                ans = min(ans, nums[left])
                left = left + 1
                right = right -1
            elif nums[left]<= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans
# Without using elif 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[left] == nums[mid] == nums[right]:
                ans = min(ans, nums[left])
                left = left + 1
                right = right -1
                continue
            if nums[left]<= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans
# Another solution added
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[left] == nums[mid] == nums[right]:
                ans = min(ans, nums[left])
                left = left + 1
                right = right -1
                continue
            # if search space already sorted 
            # then nums[left ] is always smaller in that search space
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break
            if nums[left]<= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans


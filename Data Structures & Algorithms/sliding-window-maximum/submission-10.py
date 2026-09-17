class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

      
        output = []
        dq = deque([])

        for i in range(0, len(nums)):
            if i > k-1:
                l = i - k + 1
                if l > dq[0]:
                    dq.popleft()
           
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            if i >= k-1:
                output.append(nums[dq[0]])
            
        return output
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        vol = 0
        cu = 0
        leftmax = [height[0]]
        for i in range(1, len(height)):
            leftmax.append(max(leftmax[i-1], height[i]))
        rightmax = [height[-1]]
        for j in range(len(height) - 2, 0, -1):
            rightmax.append(max(height[j], rightmax[-1]))
        rightmax.reverse()

        for h in range(1, len(height)-1):
            cu = height[h]
            water = max(min(leftmax[h],rightmax[h])-cu, 0)
            vol += water
        return vol
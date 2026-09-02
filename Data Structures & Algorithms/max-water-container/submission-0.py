class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1 #start and end
        biggest = 0 #where i will store my val of area
        while i < j:
            dist = j - i
            area = min(heights[i],heights[j]) * dist #formula for area
            if area > biggest: #compare and store
                biggest = area
            if heights[i] > heights[j]: # if height of right smaller, right move down
                j -= 1
            else: #if height same/right bigger, left move up
                i += 1
        return biggest


        
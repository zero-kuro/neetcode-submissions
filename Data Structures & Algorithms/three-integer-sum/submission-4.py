class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        foutput = []
        i = 0
        j = i + 1
        k = len(nums) - 1

        while i < len(nums) - 1: #starting off with moving j and i keep still
            if nums[i] > 0:
                break

            while j < k: #creating a loop where i can move my j and k

                total = nums[i] + nums[j] + nums[k] #constantly updating my total
            #out of loop means no more possible combi for the i

                if total < 0: #since smaller, j increase
                    j += 1
                elif total > 0: #bigger, k decrease
                    k -= 1
                else: #found, so append, then increase j position to continue search for more)
                    foutput.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

    
                
            i += 1 #increase position of i by , reset position of j and k to restart loop, until i reaches a position i - 2 = j - 1 = k (last three position)
            while i < len(nums) - 1 and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            
        
        return foutput
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        highest = 0
        longest = 0
        for r in range(0, len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            highest = max(counts.values())
            windowlength = r - l + 1
            while windowlength - highest > k:
                counts[s[l]] -= 1
                l += 1
                windowlength = r - l + 1

            longest = max(longest, windowlength)

        return longest
                

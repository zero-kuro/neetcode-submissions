class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        array = {}
        output = []
        for i, letter in enumerate(s[::-1]):
            if letter not in array:
                array[letter] = len(s) - (i+1)
    
        j = 0
        while j < len(s):
            end = array[s[j]]

            i = j
            while i <= end:
                end = max(end, array[s[i]])
                i += 1
            
            size = end - j + 1
            j = end + 1
            output.append(size)
        return output
    
    

                

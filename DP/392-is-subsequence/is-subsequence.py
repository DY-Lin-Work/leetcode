class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subLen = len(s)
        if subLen == 0:
            return True
            
        subIdx = 0
        subChar = s[subIdx]
        

        for idx in range(len(t)):
            if subChar == t[idx]:
                subIdx += 1

                if subIdx == subLen:
                    return True
                
                subChar = s[subIdx]
        return False
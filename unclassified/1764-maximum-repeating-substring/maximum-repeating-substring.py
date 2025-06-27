class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maxCount = 0
        IdxList = []

        for charIdx in range(len(sequence)):
            IdxList.append([charIdx, 0, 0])

            newIL = []
            for wordIdx in IdxList:
                count = wordIdx[2]
                if word[wordIdx[1]] == sequence[charIdx]:
                    newWordIdx = 0
                    if wordIdx[1] == len(word) - 1:
                        count += 1
                    else:
                        newWordIdx = wordIdx[1] + 1
                    newIL.append([wordIdx[0], newWordIdx, count])

                if count > maxCount:
                    maxCount = count
            IdxList = newIL
                    
        return maxCount

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        for idx in range(1, len(words)):
            if groups[idx - 1] == groups[idx]:
                pass         
            else:
                ans.append(words[idx])

        return ans
        




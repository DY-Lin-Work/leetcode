class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        cur_max_len = 1
        cur_max_str = s[0]

        for idx in range(length):
            if length - idx <= cur_max_len:
                break

            for neg_idx in range(-1, idx-length, -1):
                cur_len = length + neg_idx - idx + 1
                if  cur_len <= cur_max_len:
                    break
                
                it = 0
                fail = False
                while idx + it <= length + (neg_idx - it):
                    if s[idx + it] != s[neg_idx - it]:
                        fail = True
                        break
                    else:
                        it += 1
                
                if fail == False:
                    cur_max_len = cur_len
                    if neg_idx == -1:
                        cur_max_str = s[idx:]
                    else:
                        cur_max_str = s[idx: neg_idx + 1]
        return cur_max_str
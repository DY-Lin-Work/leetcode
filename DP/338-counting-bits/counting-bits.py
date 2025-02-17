import numpy as np
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            ans = np.array([0, 1])
            length = len(ans)
            while length <= n+1:
                ans = np.concatenate((ans, ans+1))
                length = len(ans)
                print(ans)
            return ans[:n+1].tolist()
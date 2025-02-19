class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            prev3 = 0
            prev2 = 1
            prev = 1
            ans = 0

            for idx in range(3, n+1):
                ans = prev + prev2 + prev3
                prev3 = prev2
                prev2 = prev
                prev = ans
            return ans

        
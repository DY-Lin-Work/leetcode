class Solution:

    def fib(self, n: int) -> int:
        if n == 0: # base case 0
            return 0
        elif n == 1: # base case 1
            return 1
        else: # sum up the prev 2 numbers and updates for the next iter
            prev2 = 0
            prev = 1
            ans = 0
            for idx in range(2, n+1):
                ans = prev2 + prev
                prev2 = prev
                prev = ans
            return ans


        
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [None for _ in range(n + 1)]
        power = 1

        if len(ans) > 0:
            ans[0] = 0
        if len(ans) > 1:
            ans[1] = 1

        for i in range(n + 1):
            if i == power * 2:
                ans[i] = 1
                power *= 2
            elif i > power:
                ans[i] = ans[i - power] + 1
        
        return ans

        
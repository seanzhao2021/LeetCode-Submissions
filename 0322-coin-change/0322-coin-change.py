class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        

        dp = {}

        def dfs(total):
            #base case:
            #subtracting coin from our current total ends with less than 0 --> fail
            #ends with 0 --> pass
            
            if total == 0:
                return 0
            
            if total in dp:
                return dp[total]

            current_best = float("inf")

            #for each choice in coins list
            for coin in coins:
                if total - coin >= 0:
                    current_best = min(1 + dfs(total - coin), current_best)

            dp[total] = current_best

            return current_best
        
        ans = dfs(amount)

        if ans == float("inf"):
            return - 1
        else:
            return ans

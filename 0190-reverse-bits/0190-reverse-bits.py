class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #2 ^ 31
        power = 2147483648
        res = 0

        for i in range(32):
            if n == 0:
                continue
            temp = n % 2
            if temp == 1:
                res += (power * temp)
            n = n / 2
            power = power / 2
        
        return res

        
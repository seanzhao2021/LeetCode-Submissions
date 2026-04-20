class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        l, r = 0, 0

        ans_len = len(s) + 2
        ans = ""

        sMap, tMap = {}, {}
        
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1


        def isValid(sMap, tMap):

            for key in tMap:
                if key in sMap and sMap[key] >= tMap[key]:
                    continue
                else:
                    return False
            return True

        while r < len(s):

            if s[r] not in sMap:
                sMap[s[r]] = 1
            else:
                sMap[s[r]] += 1
            
            #if current substring is valid
            #shrink left window until no longer valid?
            while isValid(sMap, tMap):
                #save ans_len and ans
                if r - l + 1 < ans_len:
                    ans_len = r - l + 1
                    ans = s[l : r + 1]
                sMap[s[l]] -= 1
                l += 1
            
            r += 1
        
        return ans
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + ":"
            encoded += string

        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        cnt, i = 0, 0
        temp = ""
        while i < len(s):
            if cnt == 0:
                temp = ""
                while s[i] != ":":
                    cnt *= 10
                    cnt += int(s[i])
                    i += 1

            else:
                temp += s[i]
                cnt -= 1
            
            if cnt == 0:
                decoded.append(temp)
            
            i += 1
        return decoded
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
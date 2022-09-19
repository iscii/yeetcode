# 9/19/2022
# Runtime: 19 ms
# Memory Usage: 13.7 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"(": 0,"[": 0,"{": 0}
        complements = {")": "(","]": "[","}": "{"}
        cur = []

        for i in range(len(s)):
            if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
                brackets[s[i]]+=1
                cur.append(s[i])
            if(s[i] == ")" or s[i] == "]" or s[i] == "}"):
                if(brackets[complements[s[i]]] == 0 or cur[-1] != complements[s[i]]):
                    return False
                brackets[complements[s[i]]]-=1
                cur.pop()
        for bracket in brackets:
            if(brackets[bracket] > 0):
                return False
        return True
        

s = Solution
print(s.isValid(s, "(){}[]"))
print(s.isValid(s, "([)]"))
print(s.isValid(s, "([])"))
        
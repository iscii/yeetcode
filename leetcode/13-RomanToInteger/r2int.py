#9/19/2022
# Runtime: 73 ms
# Memory Usage: 13.3 MB

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversions = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        num = 0
        i=0
        
        while i < len(s):
            if(i!=len(s)-1 and s[i]+s[i+1] in conversions):
                num+=conversions[s[i:i+2]]
                i+=2
            else:
                num+=conversions[s[i]]
                i+=1
        return num
    
s = Solution
print(s.romanToInt(s, "III"))
print(s.romanToInt(s, "LVIII"))
print(s.romanToInt(s, "MCMXCIV"))
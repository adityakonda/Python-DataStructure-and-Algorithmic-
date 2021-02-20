class Solution:

    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            a = rom_val[s[i]]
            b = rom_val[s[i - 1]]
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val


    def romanToInt(self, s):

        # MCMXCIV
        # 1994
        # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

        result = 0
        position = None
        symbol = {"I": (0,1), "V": (1,5), "X": (2,10), "L": (3,50), "C": (4,100), "D": (5,500), "M": (6,1000)}

        for ch in s:

            if position is None:
                position = symbol[ch][0]

            if symbol[ch][0] > position:
                result -= symbol[ch][1]
                position = symbol[ch][0]
            else:
                result += symbol[ch][1]
                position = symbol[ch][0]

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("XCVI"))
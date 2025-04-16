class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        i = 0
        while i < len(s):
            if s[i] in roman:
                number = number + roman[s[i]]
                if roman[s[i]] > roman[s[i-1]]:
                    print(s[i-1:i+1])
                    if s[i-1:i+1] == "IV":
                        number = number - 2
                    elif s[i-1:i+1] == "IX":
                        number = number - 2
                    elif s[i-1:i+1] == "XL":
                        number = number - 20
                    elif s[i-1:i+1] == "XC":
                        number = number - 20
                    elif s[i-1:i+1] == "CD":
                        number = number - 200
                    elif s[i-1:i+1] == "CM":
                        number = number - 200
            i += 1
        return number

<<<<<<< HEAD
class numbertoroman:
    def toRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(numbertoroman().toRoman(1))
print(numbertoroman().toRoman(4000))
=======
import roman;
n=roman.fromRoman("X"); 
>>>>>>> d700edb24eb5c3a61afa54a665cdfc945bc16d89

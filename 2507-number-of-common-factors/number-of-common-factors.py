from math import sqrt
class Solution(object):
    def commonFactors(self, a, b):
        result = []
        resul2 = []
        for i in range (1,int(sqrt(a)+1)):
            if a % i == 0:
                result.append(i)
                if a//i != 0:
                    result.append(a//i)
        for i in range (1,int(sqrt(b)+1)):
            if b % i == 0:
                resul2.append(i)
                if b//i != 0:
                    resul2.append(b//i)
        common = set(result).intersection(resul2)
        return len(common)
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
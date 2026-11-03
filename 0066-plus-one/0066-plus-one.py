class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = digits
        carry = 1
        i = -1
        add = []
        while carry:
            print(res)    
            if len(digits) < abs(i):
                res.insert(0, carry)
                carry = 0
            else:
                add = [int(x) for x in str(digits[i] + carry)]
                if len(add) == 1:
                    res[i] = add[0]
                    carry = 0
                elif len(add) == 2:
                    res[i] = add[1]
                    i -= 1
        return res
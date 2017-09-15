class Ten():
    def summ(self, one_numb, two_numb):
        if one_numb in range(0,11) and two_numb in range(0,11):
            result = one_numb + two_numb
            return result
        else:
            return -1

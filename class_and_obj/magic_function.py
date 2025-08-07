class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        add_num=self.num*other.den+other.num*self.den
        add_den=self.den*other.den
        return "{}/{}".format(add_num,add_den)

    def __sub__(self,other):
        sub_num=self.num*other.den-other.num*self.den
        sub_den=self.den*other.den
        return "{}/{}".format(sub_num,sub_den)

    def __mul__(self,other):
        mul_num=self.num*other.num
        mul_den=self.den*other.den
        return "{}/{}".format(mul_num,mul_den)

    def __truediv__(self,other):
        div_num=self.num*other.den
        div_den=other.den*self.num
        return "{}/{}".format(div_num,div_den)



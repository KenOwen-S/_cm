import numpy as np

class FiniteField:
    def __init__(self, p, n=1):
        self.p = p  # 素數
        self.n = n  # 次數
        self.q = p ** n  # 元素個數
        self.elements = np.arange(self.q)  # 元素集合

    def add(self, a, b):
        return (a + b) % self.p  # 加法 mod p

    def multiply(self, a, b):
        return (a * b) % self.p  # 乘法 mod p

    def additive_inverse(self, a):
        return (-a) % self.p  # 加法逆元

    def multiplicative_inverse(self, a):
        if a == 0:
            return None
        for x in self.elements[1:]:  # 忽略 0
            if self.multiply(a, x) == 1:
                return x
        return None

    def is_additive_group(self):
        # 驗證加法群封閉性、結合律、單位元、逆元
        zero = 0
        # 檢查封閉性
        for a in self.elements:
            for b in self.elements:
                if self.add(a, b) not in self.elements:
                    return False
        # 檢查結合律
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self.add(self.add(a, b), c) != self.add(a, self.add(b, c)):
                        return False
        # 檢查單位元
        for a in self.elements:
            if self.add(a, zero) != a:
                return False
        # 檢查逆元
        for a in self.elements:
            if self.add(a, self.additive_inverse(a)) != zero:
                return False
        return True

# 範例使用
F = FiniteField(5)  # GF(5)
print("Elements:", F.elements)
print("Additive group valid?", F.is_additive_group())
print("Additive inverse of 3:", F.additive_inverse(3))
print("Multiplicative inverse of 3:", F.multiplicative_inverse(3))

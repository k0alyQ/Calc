import math

class TFrac:
    def __init__(self, a, b=None):
        if isinstance(a, str):
            # Если входное значение - строка вида 'a\b'
            try:
                self.numerator, self.denominator = map(int, a.split('\\'))
            except ValueError:
                self.numerator, self.denominator = int(a), 1
        else:
            # Если переданы два числа: числитель и знаменатель
            self.numerator = a
            self.denominator = b
        # Сокращаем дробь при инициализации
        self.simplify()

    def simplify(self):
        # Сокращение дроби
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        # Обеспечиваем, чтобы знаменатель был всегда положительным
        #if self.denominator < 0:
            #self.numerator = -self.numerator
            #self.denominator = -self.denominator

    def copy(self):
        # Копируем текущую дробь
        return TFrac(self.numerator, self.denominator)

    def add(self, other):
        # Сложение дробей
        num = self.numerator * other.denominator + other.numerator * self.denominator
        denom = self.denominator * other.denominator
        return TFrac(num, denom)

    def multiply(self, other):
        # Умножение дробей
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return TFrac(num, denom)

    def subtract(self, other):
        # Вычитание дробей
        num = self.numerator * other.denominator - other.numerator * self.denominator
        denom = self.denominator * other.denominator
        return TFrac(num, denom)

    def divide(self, other):
        # Деление дробей
        if other.numerator == 0:
            return 1 # Ошибка: деление на ноль
        num = self.numerator * other.denominator
        denom = self.denominator * other.numerator
        return TFrac(num, denom)

    def square(self):
        # Квадрат дроби
        num = self.numerator ** 2
        denom = self.denominator ** 2
        return TFrac(num, denom)

    def reciprocal(self):
        # Обратная дробь
        if self.numerator == 0:
            return 1 # Ошибка: обратной дроби не существует
        return TFrac(self.denominator, self.numerator)

    def negate(self):
        # Минус дроби
        return TFrac(-self.numerator, self.denominator)

    def equals(self, other):
        # Проверка на равенство дробей
        return self.numerator == other.numerator and self.denominator == other.denominator

    def greater_than(self, other):
        # Проверка больше ли дробь другой
        return self.numerator * other.denominator > self.denominator * other.numerator

    def numerator_number(self):
        # Числитель в числовом формате
        return float(self.numerator)

    def denominator_number(self):
        # Знаменатель в числовом формате
        return float(self.denominator)

    def numerator_string(self):
        # Числитель в строковом формате
        return str(self.numerator)

    def denominator_string(self):
        # Знаменатель в строковом формате
        return str(self.denominator)

    def fraction_string(self):
        # Строковое представление дроби
        return f"{self.numerator}\\{self.denominator}"

    def __str__(self):
        return f"{self.numerator}\\{self.denominator}"

'''
# Пример использования
q = TFrac(6, 3) #2/1
d = TFrac(1, 2) #1/2
r = TFrac("7\\9") # 7/9
result = q.add(d) # 5/2
r_copy = r.copy() # 7/9
result2 = q.multiply(d) # 1/1
result3 = q.subtract(d) # 3/2
qq = TFrac("1\\2") # 1/2
result4 = d.subtract(qq) # 0/1
result5 = r.square() # 49/81
result5 = r.reciprocal() # 9/7
result6 = q.negate() #-2/1
result7 = q.divide(d) # 4/1
print(d.equals(q))
print(d.greater_than(result)) # d > result 1/2 > 5/2 False
print(q.numerator_number())
print(q.denominator_string())
print(q.fraction_string())
'''

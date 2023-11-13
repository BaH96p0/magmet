import math


class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.hypotenuse = math.sqrt(base**2 + height**2)

    def increase_side(self, percent):
        self.base *= 1 + percent / 100
        self.height *= 1 + percent / 100
        self.hypotenuse = math.sqrt(self.base**2 + self.height**2)
        return percent

    def decrease_side(self, percent):
        self.base *= 1 - percent / 100
        self.height *= 1 - percent / 100
        self.hypotenuse = math.sqrt(self.base**2 + self.height**2)

    def calculate_circumradius(self):
        return self.hypotenuse / 2

    def calculate_perimeter(self):
        return self.base + self.height + self.hypotenuse

    def calculate_angles(self):
        angle_a = math.degrees(math.asin(self.height / self.hypotenuse))
        angle_b = math.degrees(math.asin(self.base / self.hypotenuse))
        angle_c = 90
        return angle_a, angle_b, angle_c


triangle = RightTriangle(base=3, height=4)
print("Исходные значения:")
print("Base:", triangle.base)
print("Height:", triangle.height)
print("Hypotenuse:", triangle.hypotenuse)


a = triangle.increase_side(20)
print(f"\nПосле увеличения сторон на {a}%:")
print("Base:", triangle.base)
print("Height:", triangle.height)
print("Hypotenuse:", triangle.hypotenuse)

print("\nРадиус описанной окружности:", triangle.calculate_circumradius())
print("Периметр треугольника:", triangle.calculate_perimeter())
print("Углы треугольника:", triangle.calculate_angles())
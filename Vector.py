class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def read(self):
        self.x = float(input("Введите x: "))
        self.y = float(input("Введите y: "))
        self.z = float(input("Введите z: "))

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )


v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)

v4 = v1 + v2
print("Сложение v1 и v2:")
v4.display()

a = v4 * v3
print("Скалярное произведение v4 и v3:", a)

v4 = v1 * 10
print("Умножение v1 на скаляр 10:")
v4.display()

v4 = v1 @ v3
print("Векторное произведение v1 и v3:")
v4.display()
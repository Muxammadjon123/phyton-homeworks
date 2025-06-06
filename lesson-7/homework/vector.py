import math
class Vector:
    def __init__(self,*components):
        self.compenents=components
    def __str__(self):
        return f"Vector({','.join(map(str,self.components))})"
    def __len__(self):
        return len(self)
    def __add__(self, other):
        if len(self)!=len(other):
            raise ValueError("Vectors should be with the same dimensions")
        return Vector(*(a+b for a,b in zip(self.components,other.components)))
    def __sub__(self,other):
        if len(self)!=len(other):
            raise ValueError("Vectors should be with the same dimensions")
        return Vector(*(a-b for a,b in zip(self.components,other.components)))
    def __mul__(self,other):
        if isinstance(other,Vector):
            if len(self)!=len(other):import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be of same dimension for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            return Vector(*(a * other for a in self.components))

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(a / mag for a in self.components))

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)              
print(v1 + v2)         
print(v2 - v1)         
print(v1 * v2)       
print(3 * v1)          
print(v1.magnitude())   
print(v1.normalize())   

              
# "__init__": used to initialize the module, or used to contract or create a new object

class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

Rect(2, 3)

#  __str__ is used to define a string representation of the object
class str:
    def __str__(self):
        return f"Rect({self.x}, {self.y})"

# __add__ is used to define the behavior of the addition operator
class add:
    def __add__(self, other):
        return Rect(self.x + other.x, self.y + other.y)
    
    str1 = "hello-"
    str2 = "world"

    new_str = str1.__add__(str2)
    print(new_str)
    
# __sub__ is used to define the behavior of the subtraction operator
class sub:
    def __sub__(self, other):
        return Rect(self.x - other.x, self.y - other.y)
    
    str1 = "hello-"
    str2 = "hello"

    new_str = str1.__sub__(str2)
    print(new_str)

# __mul__ is used to define the behavior of the multiplication operator
class mul:
    def __mul__(self, other):
        return Rect(self.x * other.x, self.y * other.y)
    
    num1 = 2
    num2 = 4

    new_str = num1.__mul__(num2)
    print(new_str)

# __truediv__ is used to define the behavior of the division operator
class truediv:
    def __truediv__(self, other):
        return Rect(self.x / other.x, self.y / other.y)
    
    num1 = 8
    num2 = 4

    new_str = num1.__truediv__(num2)
    print(new_str)

# __floordiv__ is used to define the behavior of the floor division operator
class floordiv:
    def __floordiv__(self, other):
        return Rect(self.x // other.x, self.y // other.y)
    
    num1 = 8
    num2 = 4

    new_str = num1.__floordiv__(num2)
    print(new_str)

# __mod__ is used to define the behavior of the modulo operator
class mod:
    def __mod__(self, other):
        return Rect(self.x % other.x, self.y % other.y)
    
    num1 = 8
    num2 = 4

    new_str = num1.__mod__(num2)
    print(new_str)

# __pow__ is used to define the behavior of the power operator
class pow:
    def __pow__(self, other):
        return Rect(self.x ** other.x, self.y ** other.y)
    
    num1 = 2
    num2 = 4

    new_str = num1.__pow__(num2)
    print(new_str)

# __getitem__ is used to define the behavior of indexing
class getitem:
    def __getitem__(self, index):
        return self.str1[index]
    
    str1 = "hello"
    str2 = "world"

    new_str = str1.__getitem__(0)
    print(new_str)

# __len__ is used to define the behavior of the len() function
class len:
    def __len__(self):
        return len(self.str1)
    
    str1 = "hello"
    str2 = "world"

    new_str = str1.__len__()
    print(new_str)
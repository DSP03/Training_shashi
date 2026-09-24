"""
Master Class 4 — The Java Bridge
Topic: Dunder Methods — Python's toString() / equals()

Run me directly:  python 10_dunder_methods.py
"""


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):             # like toString()
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):            # toString(), but debug-oriented
        return f"Vector(x={self.x!r}, y={self.y!r})"

    def __eq__(self, other):       # like equals()
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):      # operator overloading — no Java equivalent!
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):             # powers len(vector)
        return 2   # a 2D vector always has 2 components


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)                # uses __str__: Vector(1, 2)
print(str(v1))            # same thing, explicit
print(repr(v1))           # uses __repr__: Vector(x=1, y=2)

print("v1 == Vector(1, 2):", v1 == Vector(1, 2))   # uses __eq__
print("v1 == v2:", v1 == v2)

v3 = v1 + v2               # uses __add__
print("v1 + v2 =", v3)

print("len(v1):", len(v1))   # uses __len__

# Without __str__, print() would show something like:
#   <__main__.Vector object at 0x7f...>
# Try commenting out __str__ above and re-running to see the difference.


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Comment out __str__ and re-run to show Python's ugly default repr —")
    print("then restore it. Ask trainees which single dunder they'd add first")
    print("to any new class they write (usually __repr__, for debuggability).")

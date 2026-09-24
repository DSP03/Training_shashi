"""
Master Class 4 — The Java Bridge
Topic: Inheritance & Method Overriding

Run me directly:  python 04_inheritance_overriding.py
"""


class BaseModel:
    def __init__(self):
        print("BaseModel.__init__ called")

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward()")

    def describe(self):
        return "I am a model."


class LinearModel(BaseModel):
    def __init__(self, w):
        super().__init__()          # calls BaseModel.__init__, like Java's super()
        self.w = w

    def forward(self, x):           # override
        return x * self.w

    def describe(self):             # override, but extend the parent's version too
        return super().describe() + f" Specifically, a linear model with w={self.w}."


lm = LinearModel(w=3)
print(lm.forward(10))       # 30
print(lm.describe())


# --- Live "gotcha" demo: no @Override, so a typo just creates a new method ---
class BrokenModel(BaseModel):
    def __init__(self, w):
        super().__init__()
        self.w = w

    def foward(self, x):        # <-- typo! Should be 'forward'
        return x * self.w


bm = BrokenModel(w=5)
try:
    bm.forward(10)              # calls BaseModel.forward — NOT the typo'd method
except NotImplementedError as e:
    print("\nBrokenModel.forward() was NEVER overridden:", e)
print("...but bm.forward(10) works fine and nobody warned us:", bm.foward(10))


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run this file, then intentionally rename 'forward' to 'foward' in")
    print("LinearModel and show that Python happily runs it with ZERO warnings —")
    print("this is exactly the class of bug @Override prevents at compile time in Java.")

"""
Master Class 4 — OOP Basics
Topic: Instance, Class & Static Methods

Run me directly:  python 03_method_types.py
"""


class Model:
    default_lr = 0.01     # class attribute, used as a default below

    def __init__(self, name, lr):
        self.name = name
        self.lr = lr

    # --- instance method: needs a specific object (self) ---
    def train(self):
        print(f"Training {self.name} at lr={self.lr}")

    # --- class method: an alternate constructor, works off the class (cls) ---
    @classmethod
    def from_config(cls, config: dict):
        return cls(config["name"], config.get("lr", cls.default_lr))

    # --- static method: doesn't need self OR cls, just lives in the class namespace ---
    @staticmethod
    def normalize(x):
        return max(0.0, min(1.0, x))


# Instance method — called on an object
m = Model("gpt-mini", 0.02)
m.train()

# Class method — called on the class itself, like a factory
m2 = Model.from_config({"name": "gpt-nano"})   # lr falls back to default_lr
m2.train()

# Static method — called on the class, no instance needed
print("normalize(1.7):", Model.normalize(1.7))
print("normalize(-0.3):", Model.normalize(-0.3))


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("cls inside from_config refers to Model itself — same idea as")
    print("referencing static members via ClassName in Java. Point out that")
    print("Model.normalize(...) needs no instance at all, just like a Java")
    print("'static void normalize(x)' helper.")

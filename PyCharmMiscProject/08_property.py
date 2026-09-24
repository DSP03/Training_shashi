"""
Master Class 4 — The Java Bridge
Topic: @property vs. Getters & Setters

Run me directly:  python 08_property.py
"""


class Model:
    def __init__(self, lr):
        self._lr = lr

    @property
    def lr(self):                # like getLr()
        return self._lr

    @lr.setter
    def lr(self, value):         # like setLr(v)
        if value <= 0:
            raise ValueError("lr must be > 0")
        self._lr = value


m = Model(0.01)
print("Initial lr:", m.lr)       # reads like a plain attribute — no parens

m.lr = 0.05                      # calls the setter automatically — no parens
print("Updated lr:", m.lr)

try:
    m.lr = -1                    # triggers the validation inside the setter
except ValueError as e:
    print("Setting m.lr = -1 raises:", e)


# --- Compare: what it would look like WITHOUT @property (the Java-ish way) ---
class ModelWithGetterSetter:
    def __init__(self, lr):
        self._lr = lr

    def get_lr(self):
        return self._lr

    def set_lr(self, value):
        if value <= 0:
            raise ValueError("lr must be > 0")
        self._lr = value


m2 = ModelWithGetterSetter(0.01)
m2.set_lr(0.05)
print("\nWithout @property:", m2.get_lr())


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run both versions side by side. Point out that m.lr = 0.05 and")
    print("m2.set_lr(0.05) do the exact same validation work — @property just")
    print("keeps the call-site syntax looking like plain attribute access.")

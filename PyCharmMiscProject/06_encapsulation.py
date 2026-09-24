"""
Master Class 4 — The Java Bridge
Topic: Encapsulation by Convention

Run me directly:  python 06_encapsulation.py
"""


class Account:
    def __init__(self, balance):
        self.owner = "Ada"          # public — no leading underscore
        self._balance = balance     # "protected" — convention, not enforced
        self.__pin = 1234           # "private" — name-mangled, not enforced


a = Account(100)

print("Public access works:", a.owner)
print("'_protected' access ALSO works — it's just a naming hint:", a._balance)

try:
    print(a.__pin)                  # this will raise
except AttributeError as e:
    print("a.__pin raises:", e)

# ...but the name-mangled attribute is still reachable if you know the trick:
print("a._Account__pin still works:", a._Account__pin)

# Proof of what actually happened under the hood:
print("\nAll instance attributes:", vars(a))


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run this file live and let trainees SEE the AttributeError happen,")
    print("then immediately show a._Account__pin succeeding right after.")
    print("Land the line: 'We're all consenting adults' — Python trusts the")
    print("developer instead of the compiler.")

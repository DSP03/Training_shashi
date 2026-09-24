"""
Master Class 4 — The Java Bridge
Topic: Multiple Inheritance & MRO

Run me directly:  python 05_multiple_inheritance_mro.py
"""


class Serializable:
    def to_json(self):
        return "{...serialized as JSON...}"


class Loggable:
    def log(self, msg):
        print(f"[LOG] {msg}")

    def to_json(self):
        # deliberately also defines to_json, to show MRO resolving the clash
        return "{...Loggable's own JSON...}"


class Pipeline(Serializable, Loggable):   # true multiple inheritance — no Java equivalent
    pass


p = Pipeline()
p.log("pipeline created")
print(p.to_json())              # which to_json wins? Determined by MRO.

print("\nMRO:")
for cls in Pipeline.__mro__:
    print(" ->", cls.__name__)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Because Serializable comes FIRST in 'class Pipeline(Serializable, Loggable)',")
    print("Python's C3 linearization puts Serializable.to_json() ahead of Loggable's.")
    print("Try swapping the order to 'class Pipeline(Loggable, Serializable)' and")
    print("re-run — p.to_json() output changes. print(Pipeline.__mro__) any time")
    print("multiple-inheritance behavior looks surprising.")

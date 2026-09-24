"""
Master Class 4 — OOP Basics
Topic: Instance vs. Class Attributes

Run me directly:  python 02_instance_vs_class_attrs.py
"""


class Agent:
    registry = []        # class attribute — shared by ALL instances (like Java 'static')

    def __init__(self, name):
        self.name = name  # instance attribute — belongs to this object only
        Agent.registry.append(name)


a = Agent("alpha")
b = Agent("beta")

print("Agent.registry:", Agent.registry)     # ['alpha', 'beta']
print("a.name:", a.name, "| b.name:", b.name)


# --- Live "gotcha" demo: mutable class attributes are SHARED ---
class Pipeline:
    steps = []   # BUG WAITING TO HAPPEN if trainees expect this to be per-instance

    def add_step(self, step):
        self.steps.append(step)


p1 = Pipeline()
p2 = Pipeline()
p1.add_step("clean")
p2.add_step("tokenize")

print("\np1.steps:", p1.steps)   # ['clean', 'tokenize'] — SHARED, probably not intended!
print("p2.steps:", p2.steps)     # same list object


# --- The fix: initialize mutable attributes inside __init__ ---
class FixedPipeline:
    def __init__(self):
        self.steps = []   # now a fresh list per instance

    def add_step(self, step):
        self.steps.append(step)


fp1 = FixedPipeline()
fp2 = FixedPipeline()
fp1.add_step("clean")
fp2.add_step("tokenize")

print("\nfp1.steps:", fp1.steps)  # ['clean'] only
print("fp2.steps:", fp2.steps)    # ['tokenize'] only


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run this whole file and point out how Pipeline.steps leaks across")
    print("instances, then show FixedPipeline solving it by assigning inside __init__.")

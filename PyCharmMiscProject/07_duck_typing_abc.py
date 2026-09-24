"""
Master Class 4 — The Java Bridge
Topic: Duck Typing vs. Interfaces (abc.ABC)

Run me directly:  python 07_duck_typing_abc.py
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------
# PART A — Duck typing: no interface required, just call the method
# ---------------------------------------------------------------------
def run_pipeline(step, data):
    return step.process(data)   # step just needs a .process() method — that's it


class Cleaner:
    def process(self, d):
        return d.strip()


class Tokenizer:
    def process(self, d):
        return d.split()


print("Duck typing:")
print(" Cleaner ->", run_pipeline(Cleaner(), "  hello world  "))
print(" Tokenizer ->", run_pipeline(Tokenizer(), "hello world"))
# Cleaner and Tokenizer share NO base class — they both just "quack"


# ---------------------------------------------------------------------
# PART B — abc.ABC: a strict, enforced contract (like a Java interface)
# ---------------------------------------------------------------------
class Step(ABC):
    @abstractmethod
    def process(self, d):
        ...


class UppercaseStep(Step):
    def process(self, d):
        return d.upper()


print("\nabc.ABC contract:")
print(" UppercaseStep ->", run_pipeline(UppercaseStep(), "hello"))

try:
    Step()   # cannot instantiate an abstract class
except TypeError as e:
    print(" Step() raises:", e)


# What happens if a subclass forgets to implement the abstract method?
class IncompleteStep(Step):
    pass


try:
    IncompleteStep()
except TypeError as e:
    print(" IncompleteStep() raises:", e)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run Part A first and stress that Cleaner/Tokenizer share zero code.")
    print("Then run Part B and show Step() and IncompleteStep() both failing —")
    print("this is Python's closest equivalent to a Java 'implements' contract.")
